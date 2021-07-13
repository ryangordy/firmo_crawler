import scrapy
import requests
import pandas as pd
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import LinkCrawlerItems
from urllib.parse import urlparse


class ExperianSpider(scrapy.Spider):
    name = 'LinkCrawler'
    df = pd.read_csv("C:/Users/Fungui/PycharmProjects/Webscraper/experian_test/experian_test/clean_restaurants_1000.csv"
                     )
    df = df.loc[df['status'] == 200]
    start_urls = df['url'].values.tolist()
    print(start_urls)
    # start_urls = ['http://www.hbsugarshack.com']
    rules = [Rule(LinkExtractor(allow=()), callback='parse_obj', follow=True), ]
    DOWNLOAD_DELAY = 2

    def parse(self, response):
        items = LinkCrawlerItems()
        try:
            urls_all = []
            extractor = LinkExtractor()
            links = extractor.extract_links(response)
            parsed_uri = urlparse(response.url)
            domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
            items['domain'] = domain
            for link in links:
                urls_all.append(link.url)
                items['links'] = urls_all
            yield items
        except:
            # items['valid'] = 0
            items['link'] = response
            yield items
