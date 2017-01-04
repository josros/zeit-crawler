import scrapy
from zeit.items import ZeitArticleItem

class ZeitSpider(scrapy.Spider):
    name = "zeit"
    allowed_domains = ["zeit.de"]
    start_urls = [
        "http://www.zeit.de/index"
    ]

    def parse(self, response):
        self.log('Received response from: %s' % response.url)
        for url in response.xpath('//article/div/h2/a/@href').extract():
            yield scrapy.Request(url, callback=self.parseArticle)

    def parseArticle(self, response):
        self.log('Received article response from: %s' % response.url)

        # if paging: show everyting on one page an parse complete article
        if(response.xpath('//li[@class="article-pager__all"]').extract_first() is not None):
            allOnOnePageUrl = response.xpath('//li[@class="article-pager__all"]/a/@href').extract_first()
            yield scrapy.Request(allOnOnePageUrl, callback=self.parseArticle)
        else:
            yield self.genZeitArticleItem(response)

    def genZeitArticleItem(self, response):
        item = ZeitArticleItem()
        item['link'] = response.url
        item['kicker'] = response.xpath('//span[@class="article-heading__kicker"]/text()').extract()
        item['dates'] = response.xpath('//time/@datetime').extract()
        item['header'] = response.xpath('//article/div/div/h1/span[@class="article-heading__title"]/text()').extract()
        item['summary'] = response.xpath('//article/div/div/div[@class="summary"]/text()').extract()
        item['body'] = response.xpath('//p[@class="paragraph article__item"]/text()').extract()
        item['subheaders'] = response.xpath('//h2[@class="article__subheading article__item"]/text()').extract()
        item['tags'] = response.xpath('//a[@class="article-tags__link"]/text()').extract()
        return item
