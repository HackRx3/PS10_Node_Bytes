# Search based Recommendation Engine
An advanced search based semantic Recommendation System by utilizing frameworks and tech for proper model training and give desired query.

## Objectives
1. Recommend keywords that are more relevant to user’s search query by **improving accuracy relevence and optimising** the time taken.
2. Improving the **transactional impact by comparative visualization** of the dataset scraped and the keywords/analytics provided. Then combining the relevant keys for a better output.
3. Inserting extra features like **input auto-correction, similar searches** etc.
## Tech 

**Stack:** Python, Pandas, Numpy, Faiss, Seaborn, HTML, CSS

**Model:** Bert (Bidirectional Encoder Representations from Transformers)


## Approach
1. Crawling the given site and scraping the data through Scrapy.

       Scraped Data : (2652,4) 


2. Pre-processing the scraped data along with keywords provided and then calculating frequency i.e. finding most searched.
3. **Implementing S Bert model leading to :**

     a) Semantic Search (eg. insurance -> vehicle).

     b) Paraphrase Mining (i.e. Text with identical/similar meaning).

     c) Writing Search function -> Analyzing Query Vector ->Fetch into top k_ids.

