import pandas as pd
import numpy as np 
import altair as alt
import os
import argparse

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def main(input):
	"""
	Combine data of electoral college and census population

	Parameters
	----------
	input : string, optional
	    The path where the input data resides (default is '/public_data')

	Returns
	-------
	None
	"""
	college_data = pd.read_csv(f"{input}/electoral_college_vote.csv")
	census_pop_data = pd.read_csv(f"{input}/us_census_population.csv")

	college_data['Census year reference'] = (np.floor((college_data['Year'] - 1)/10)*10).astype(int)

	college_data_merged = college_data.merge(
	    census_pop_data, how='left', left_on=['Census year reference', 'State'], right_on=['Year', 'State']
	).dropna()
	college_data_merged = college_data_merged.drop(['Year_y'], axis=1).rename(columns={"Year_x": "Year"})
	college_data_merged['Census population'] = college_data_merged['Census population'].astype(int)

	college_data_merged.to_csv(f"{input}/electoral_college_population.csv", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default='../public_data')
    args = parser.parse_args()

    main(args.input)