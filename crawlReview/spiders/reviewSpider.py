from pathlib import Path
from bs4 import BeautifulSoup
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "crawlReview"
    allowed_domains = ['goodreads.com']

    def start_requests(self):
        urls = [
            "https://www.goodreads.com/book/show/4214.Life_of_Pi?ac=1&from_search=true&qid=GmMGOfW3lh&rank=1",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for review in response.css('article.ReviewCard'): # loop all review, extract reviewerName, content, tags of each review
            name = review.css("section.ReviewerProfile__info a::text").get()

            tags = review.css("section.ReviewCard__tags span.Button__labelItem::text").getall()
            
            content = review.css("section.ReviewText section.ReviewText__content span.Formatted").get()
            soup = BeautifulSoup(content, 'html.parser') # remove tag <br> in content of review
            content = soup.get_text()

            yield { # return object with 3 fields below
                "nameReviewer": name,
                "content": content,
                "tags": tags
            }