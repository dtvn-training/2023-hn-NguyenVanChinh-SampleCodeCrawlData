# Sample code crawl data from website
Overview: 
- This project use Scrapy (a library of Python) to crawl data  
- I will crawl review of user about a book from website [GoodRead](https://www.goodreads.com/book/show/4214.Life_of_Pi?ac=1&from_search=true&qid=GmMGOfW3lh&rank=1)   
- And extract some field as: reviewer name, content of review, tags of that review

To run project, crawl and export output data to file csv:  
```
    cd crawlReview
    scrapy crawl crawlReview -O reviews.csv
```