# DSCI510_FinalProject

This project analyzes the relationship between cat breed characteristics and breed popularity using publicly available data.  
The goal is to investigate whether measurable behavioral and physical traits of cat breeds are associated with public interest.

The project demonstrates a complete data science workflow, including:
- Web scraping
- API data collection
- Data cleaning and integration
- Exploratory data analysis
- Correlation analysis
- Clustering and visualization

---

Data Sources
This project integrates data from three sources:

1. Wikipedia (Web Scraping)
   - Source: *List of cat breeds*  
   - Data collected: breed name, origin, body type, coat type

2. Wikimedia Pageviews API
   - Used to measure breed popularity  
   - Popularity is defined as aggregated Wikipedia pageviews over a recent time period

3. TheCatAPI
   - Provides standardized behavioral and physical traits  
   - Includes intelligence, energy level, affection level, grooming requirements, lifespan, and weight
  
structure
├── README.md
├── requirements.txt
├── project_proposal.pdf
├── results/
│ └── final_report.pdf
├── data/
│ ├── raw/
│ │ ├── wikipedia_breeds.json
│ │ ├── pageviews.json
│ │ └── catapi_breeds.json
│ └── processed/
│ ├── cats_final.csv
│ └── cats_with_clusters.csv
└── src/
├── catapi.py
└── pageviews_api.py
└── wiki_scraper.py
├── clean_data.py
├── run_analysis.py
├── visualize_results.py

##how to run this step by step
1. pip install -r requirements.txt
2. python src/catapi.py
3. python src/pageviews_api.py
4. python src/wiki_scraper.py
5. python src/clean_data.py
6. python src/run_analysis.py
7. python src/visualize_results.py
