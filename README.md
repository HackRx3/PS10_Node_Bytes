# Search based Recommendation Engine
An advanced search based semantic Recommendation System by utilizing frameworks and tech for proper model training and give desired query.

## Objectives
1. Recommend keywords that are more relevant to user’s search query by **improving accuracy relevence and optimising** the time taken.
2. Improving the **transactional impact by comparative visualization** of the dataset scraped and the keywords/analytics provided. Then combining the relevant keys for a better output.
3. Inserting extra features like **input auto-correction, similar searches** etc.
## Tech 

**Stack:** Python, Pandas, Numpy, Faiss, Seaborn, django, HTML, CSS

**Model:** Implementing Bert (Bidirectional Encoder Representations from Transformers) using Sentence Transformers


## Approach
1. Crawling the given site and scraping the data through Scrapy.

       Scraped Data : (2652,4) 
       

<img src="https://github.com/HackRx3/PS10_Node_Bytes/blob/master/datahead.jpg" />
<img src="https://github.com/HackRx3/PS10_Node_Bytes/blob/master/plot.jpeg" />

2. Pre-processing the scraped data along with keywords provided and then calculating frequency weightage i.e. finding most searched.
3. **Implementing SBert model leading to :**

     a) Semantic Search (eg. insurance -> vehicle).

     b) Paraphrase Mining (i.e. Text with identical/similar meaning).

     c) Writing Search function -> Analyzing Query Vector ->Fetch into top k_ids.

