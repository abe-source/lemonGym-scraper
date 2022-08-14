import scrapy
from scrapy.loader import ItemLoader
from lemongym_busyness_scraper.items import LemongymBusynessScraperItem
from scrapy.loader import ItemLoader
import datetime

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['https://lemongym.lt/']

    def parse(self, response):     
        il = ItemLoader(item=LemongymBusynessScraperItem(), selector=response)
        il.add_xpath('antakalnis', "(//div[contains(@class,'ipWidget-ClubMembersDisplayWidget')]//div[@class='row']/div/h2/text())[1]")
        il.add_xpath('banginis', "(//div[contains(@class,'ipWidget-ClubMembersDisplayWidget')]//div[@class='row']/div/h2/text())[2]")
        il.add_xpath('europa', "(//div[contains(@class,'ipWidget-ClubMembersDisplayWidget')]//div[@class='row']/div/h2/text())[3]")
        il.add_xpath('fabijoniskes', "(//div[contains(@class,'ipWidget-ClubMembersDisplayWidget')]//div[@class='row']/div/h2/text())[4]")
        il.add_xpath('perkunkiemis', "(//div[contains(@class,'ipWidget-ClubMembersDisplayWidget')]//div[@class='row']/div/h2/text())[5]")
        il.add_xpath('pilaite', "(//div[contains(@class,'ipWidget-ClubMembersDisplayWidget')]//div[@class='row']/div/h2/text())[6]")
        il.add_xpath('savanoriai', "(//div[contains(@class,'ipWidget-ClubMembersDisplayWidget')]//div[@class='row']/div/h2/text())[7]")
        il.add_xpath('silainiai', "(//div[contains(@class,'ipWidget-ClubMembersDisplayWidget')]//div[@class='row']/div/h2/text())[8]")
        il.add_xpath('zalgirioArena', "(//div[contains(@class,'ipWidget-ClubMembersDisplayWidget')]//div[@class='row']/div/h2/text())[9]")
        il.add_value('timeStamp', datetime.datetime.now().isoformat())
        yield il.load_item()