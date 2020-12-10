# US Population & Electoral College

This project aims to look at the relationship between US electoral college votes and population historically

# Data

Data sources:

https://en.wikipedia.org/wiki/United_States_Electoral_College \
https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_historical_population 
https://en.wikipedia.org/wiki/List_of_United_States_counties_and_county_equivalents
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/VOQCHQ
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/42MVDX
https://www.kaggle.com/unanimad/us-election-2020?select=president_county_candidate.csv


To run the scripts:

```bash
python scripts/scrap_us_census_pop.py
```

```bash
python scripts/scrap_electoral_college_data.py
```

for extracting the raw data

```bash
python scripts/synthesize_data.py
```

for combining the raw data between electoral college and state population data

# Visualization

Look at `./notebooks/exploration.ipynb` for some initial exploration
