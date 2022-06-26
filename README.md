# Search based Recommendation Engine
An advanced search query based Recommendation System built using BERT based sentence_transformer model to recommendations for user input query.
We implemented semantic search, question answering, summarization and document ranking and correcting spelling error in the search query.

----

## Objectives
1. Recommend keywords that are more relevant to user’s search query by **improving accuracy relevence and optimising** the time taken.
2. Improving the **transactional impact by comparative visualization** of the dataset scraped and the keywords/analytics provided. Then combining the relevant keys for a better output.
3. Inserting extra features like **input auto-correction, similar searches** etc.

----

## Tech 

**Stack:** Python, Pandas, Numpy, Faiss, Seaborn, django, HTML, CSS

**Model:** Implementing Bert (Bidirectional Encoder Representations from Transformers) using Sentence Transformers

## Flowchart


<img src="https://github.com/HackRx3/PS10_Node_Bytes/blob/master/Flowchart%20(3).jpg"/>

----

## Approach



1. Crawling the given site and scraping the data through Scrapy.

       Scraped Data : (2652,4) 
       

<img src="https://github.com/HackRx3/PS10_Node_Bytes/blob/master/datahead.jpg" />
<img src="https://github.com/HackRx3/PS10_Node_Bytes/blob/master/plot.jpeg" />

2. Pre-processing the scraped data along with keywords provided and then calculating frequency weightage i.e. finding most searched.

<img src="https://github.com/HackRx3/PS10_Node_Bytes/blob/master/scrapped%20data%20keywords.png" />
<img src="https://github.com/HackRx3/PS10_Node_Bytes/blob/master/search%20trends%20keywords.png" />

4. **Implementing SBert model leading to :**




     a) Semantic Search (eg. insurance -> vehicle).

     b) Paraphrase Mining (i.e. Text with identical/similar meaning).

     c) Writing Search function -> Analyzing Query Vector ->Fetch into top k_ids.

<img src="https://github.com/HackRx3/PS10_Node_Bytes/blob/master/Prototype.jpeg"/>


##UI Sample
<img src="https://github.com/HackRx3/PS10_Node_Bytes/blob/master/ui%20sample%202.png"/>
