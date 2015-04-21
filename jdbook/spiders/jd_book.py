from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from jdbook.items import JdbookItem


class MininovaSpider(CrawlSpider):

    name = 'jdbook'
    allowed_domains = ['jd.com']
    start_urls = ['http://search.jd.com/search?keyword=%E5%88%9B%E4%B8%9A&enc=utf-8&qrst=1&ps=addr&rt=1&stop=1&wtype=1&stock=1#keyword=%E5%88%9B%E4%B8%9A&enc=utf-8&qrst=1&ps=addr&rt=1&stop=1&stock=1&wtype=1&click=&psort=3']
    rules = [Rule(LinkExtractor(allow=['http://item.jd.com/\d+.html']), 'parse_book')]

    def parse_book(self, response):
        book = JdbookItem()
        # book['name'] = response.xpath('//div[@class="m psearch"]/ul[@class="list-h clearfix"]/li').extract()
        book['publication_by'] = response.xpath('//ul[@id="parameter2"]/li[1]/a/text()').extract()
        book['isbn_num'] = response.xpath('//ul[@id="parameter2"]/li[2]/text()').extract()
        book['book_name'] = response.xpath('//ul[@id="parameter2"]/li[7]/a/text()').extract()
        book['publication_time'] = response.xpath('//ul[@id="parameter2"]/li[9]/text()').extract()
        return book 
