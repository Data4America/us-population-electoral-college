from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import argparse

us_electoral_college_wiki_link = 'https://en.wikipedia.org/wiki/United_States_Electoral_College'

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def map_links_to_election_years(links):
    return list(map(lambda x: int(x.attrs['title'][:4]), links))

def main(output):
	"""
	Crawl a page and extract data about each state's electorla college in the previous election years

	Parameters
	----------
	additional : output, optional
	    The path to output the data to (default is '/public_data')

	Returns
	-------
	None
	"""
	request = requests.get(us_electoral_college_wiki_link)
	page = BeautifulSoup(request.text)

	# Find the table that contains the data
	table = page.find(lambda tag: tag.name == 'big' and 'presidential electors' in tag.text).find_parent('table', class_='wikitable sortable')

	# Extract the election year headers/columns
	years_headers = table.find_all(lambda tag: tag.name == 'th' and bool(tag.find('a')) and '\'' in tag.find('a').text)
	years_headers = list(map(lambda x: map_links_to_election_years(x.find_all('a')), years_headers))

	# Extract the state index
	first_state_row = table.find(lambda tag: tag.name == 'a' and tag.attrs['href'] == '/wiki/Alabama').find_parent('tr')
	state_rows = [first_state_row] + first_state_row.find_next_siblings(lambda tag: tag.name == 'tr' and bool(tag.find('a')))

	electoral_college_vote_count_col = []
	year_col = []
	state_col = []

	# Loop the states and find the vote counts associated with each historical year 
	for state in state_rows:
	    state_name = state.select('th a')[0].text
	    count_numbers = state.find_all('td')
	    
	    for index, count_ele in enumerate(count_numbers):
	        years = years_headers[index]
	        year_count = len(years)
	        vote_count = int(count_ele.text.strip() or 0)
	    
	        year_col += years
	        electoral_college_vote_count_col += ([vote_count] * year_count)
	        state_col += ([state_name] * year_count)

	df = pd.DataFrame({
	    'Year': year_col,
	    'Electoral college vote count': electoral_college_vote_count_col,
	    'State': state_col
	})

	df.to_csv(f"{output}/electoral_college_vote.csv", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', default='../public_data')
    args = parser.parse_args()

    main(args.output)
