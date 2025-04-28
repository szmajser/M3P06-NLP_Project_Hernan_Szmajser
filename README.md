# M3P06-NLP_Project- Hernan Szmajser

## Description

Perform NLP on an online dataset that you will obtain from an API or scraping.

## Dataset
Information from Wikipedia with endpoint got random publications.
- File used for webScrapping - "wikipedia_webscrapping.py"
- Wikipedia Endpoint used: "http://en.wikipedia.org/wiki/Special:Random"
- CSV File generated "wikipedia_random_intro.csv"

## Model
Pretrained model Sentence Transformer 'all-MiniLM-L6-v2'.
Cluster classification with DBSCAN. 

## Clusters Result
**Cluster 0:**
- **Category:** Species Descriptions (Plants, Insects, Animals)

**Cluster 1:**
- **Category:** Russia places?

**Cluster 2:**
- **Category:** Athletes, Sports Events

**Cluster 3:**
- **Category:** Historical Figures, Politicians, and Academics

**Cluster 4:**
- **Category:** Military ?? 

**Cluster 5:**
- **Category:** Sports Players / Biographies ?

**Cluster 6:**
- **Category:** Sports Players ?? - near cluster 5

**Cluster 7:**
- **Category:** Sports Teams

**Cluster 8:**
- **Category:** Political Figures ?

**Cluster 9:**
- **Category:** Tournaments (sports)

**Cluster 10:**
- **Category:** Leagues and Teams ?
