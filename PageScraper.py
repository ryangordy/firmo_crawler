from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
from ..items import PageScraperItems


class PageScraper(CrawlSpider):
    name = 'PageScraper'
    start_urls = ['http://www.patricksgrille.com/contact-patricks-grille']
    DOWNLOAD_DELAY = 2

    def parse_item(self, response):
        items = PageScraperItems()
        items['url'] = response.url
        items['title'] = response.meta['link_text']
        # extracting basic body
        items['body'] = '\n'.join(response.xpath('//text()').extract())
        # or better just save whole source
        items['source'] = response.body
        return items
