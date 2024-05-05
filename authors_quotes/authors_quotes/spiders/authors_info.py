from typing import Iterable
import scrapy
import json
import os
from scrapy.http import Response

if os.path.exists('authors_info.json'):
    os.remove('authors_info.json')

class AuthorsInfoSpider(scrapy.Spider):
    name = "authors_info"
    custom_settings = {"FEED_FORMAT": "json",
                        "FEED_URI": "./authors_info.json",
                        "FEED_EXPORT_TRUNCATE": True,
                        "FEED_EXPORT_ENCODING": "utf-8"
                    }
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            author_link = quote.xpath("span/a/@href").extract()[0]
            yield response.follow(author_link, self.parse_author)

    def parse_author(self, response):
        for author in response.xpath("//div[@class='author-details']"):
            yield {
                    'fullname': author.xpath("//h3[@class='author-title']/text()").extract(),
                    'born_date': author.xpath("//p/span[@class='author-born-date']/text()").extract(),
                    'born_location': author.xpath("//p/span[@class='author-born-location']/text()").extract(),
                    'description': author.xpath("//div[@class='author-description']/text()").extract()[0].strip(),
                }
