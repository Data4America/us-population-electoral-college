from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import argparse
import re

us_census_pop_wiki_link = 'https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_historical_population'

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def select_pop_tables(tag):
	"""
	Identify a tag pointing to a population table 

	Parameters
	----------
	tag : BeautifulSoup tag
		The tag to identify whether it is a population table

	Returns
	-------
	Boolean : Whether or not the tag is a population table
	"""
    header = tag.find_previous_sibling(lambda tag: 'h' in tag.name)
    
    if tag.name != 'table' or not header:
        return False
    else:
        headline = header.select('.mw-headline')[0].text.lower()
        return ('population' in headline or 'census' in headline) and 'enslaved' not in headline

def main(output):
	"""
	Crawl a page and extract data about each state's census population in the previous census years

	Parameters
	----------
	additional : output, optional
	    The path to output the data to (default is '/public_data')

	Returns
	-------
	None
	"""
	request = requests.get(us_census_pop_wiki_link)
	page = BeautifulSoup(request.text)

	# Find all population tables
	pop_tables = page.find_all(select_pop_tables)

	year_col = []
	state_col = []
	pop_col = []

	for table in pop_tables:
	    headers = table.find_all('th')
	    pop_rows = table.find_all('tr')[1:]
	    
	    for row in pop_rows:
	        columns = row.find_all('td')
	        
	        # Loop through columns to find the current state and its historical census population numbers
	        state = ''
	        for index, column in enumerate(columns):
	            if 'name' in headers[index].text.lower():
	                state = column.find('a').attrs['title']
	            elif headers[index].text[:4].isdigit():
	                state_col.append(state)
	                year_col.append(headers[index].text[:4])
	                pop_col.append(int(''.join(re.findall('\d+', column.text)) or '0'))

	df = pd.DataFrame({
	    'Year': year_col,
	    'State': state_col,
	    'Census population': pop_col
	})

	df.to_csv('../public_data/us_census_population.csv', index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', default='../public_data')
    args = parser.parse_args()

    main(args.output)
