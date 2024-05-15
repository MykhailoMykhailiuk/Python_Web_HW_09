from scrapy.crawler import CrawlerProcess
from authors_quotes.authors_quotes.spiders import authors_info, quotes
from seed import load_authors, load_guotes


if __name__ == '__main__':

    process = CrawlerProcess()
    process.crawl(quotes.QuotesSpider)
    process.crawl(authors_info.AuthorsInfoSpider)
    process.start()
    
    load_authors('authors_info.json')
    load_guotes('quotes.json')