from typing import Iterable
import scrapy
import json


class AuthorsInfoSpider(scrapy.Spider):
    name = "authors_info"
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "authors_quotes/authors_info.json"}
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = []

    def start_requests(self):
        with open('authors_quotes/authors.json', 'r') as file:
            authors = json.load(file)
            for i in authors:
                yield scrapy.Request(url=i['author_info'], callback=self.parse)

    def parse(self, response):
        for author in response.xpath("//div[@class='author-details']"):
            yield {
                    'fullname': author.xpath("//h3[@class='author-title']/text()").extract(),
                    'born_date': author.xpath("//p/span[@class='author-born-date']/text()").extract(),
                    'born_location': author.xpath("//p/span[@class='author-born-location']/text()").extract(),
                    'description': author.xpath("//div[@class='author-description']/text()").extract()[0].strip(),
                }
