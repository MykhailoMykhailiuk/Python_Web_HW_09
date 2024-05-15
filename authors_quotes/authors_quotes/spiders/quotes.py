import os
import scrapy


if os.path.exists('quotes.json'):
    os.remove('quotes.json')


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    custom_settings = {"FEED_FORMAT": "json",
                    "FEED_URI": "./quotes.json",
                    "FEED_EXPORT_TRUNCATE": True,
                    "FEED_EXPORT_ENCODING": "utf-8"
                    }
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            yield {
                "tags": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author": quote.xpath("span/small/text()").extract(),
                "quote": quote.xpath("span[@class='text']/text()").get()
            }

        yield from self.next_p(response)

    def next_p(self, response):
        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page:
            yield response.follow(next_page, self.parse)



  
