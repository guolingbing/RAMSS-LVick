from scrapy.selector import XmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy import log

class HackernewsSpider(BaseSpider):

    name = 'hackernews'
    
    start_urls = ['http://news.ycombinator.com/bigrss']
    
    def parse(self, response):
        xxs = XmlXPathSelector(response)
        for title in xxs.select("//item/title/text()").extract()
            log.msg(title)