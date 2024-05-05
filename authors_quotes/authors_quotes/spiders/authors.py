import scrapy


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "authors_quotes/authors.json"}
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                    'author': quote.xpath("span/small/text()").extract(),
                    'author_info': self.start_urls[0]+quote.xpath("span/a/@href").extract()[0],
                }

