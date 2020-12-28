# County Level Data

## US presidential election return data

2020 data [source](https://www.kaggle.com/unanimad/us-election-2020?select=president_county_candidate.csv)
2016-2000 data [source](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/VOQCHQ)
1996-1912 data [source](https://uselectionatlas.org/BOTTOM/store_data.php) (private)

For the 1996-1912 data, the state and candidate party columns are missing. But that can be fixed by joining any county-state data and US presidential candidate-party data from sources including:

https://en.wikipedia.org/wiki/List_of_United_States_presidential_candidates 
https://en.wikipedia.org/wiki/List_of_United_States_FIPS_codes_by_county 
https://github.com/kjhealy/fips-codes 

Some web scrapping might be needed, but it shouldn't be that bad.

## US county census population data

2019-1790 data [source](https://en.wikipedia.org/wiki/List_of_United_States_counties_and_county_equivalents) (from each county page)

After 2010, the data are estimates and not used in a US election.