import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def extract_number(text):
    return int(''.join(filter(str.isdigit, text)))

class LemongymBusynessScraperItem(scrapy.Item):
    antakalnis = scrapy.Field(input_processor=MapCompose(remove_tags, extract_number),
                            output_processor=TakeFirst()) 
    banginis = scrapy.Field(input_processor=MapCompose(remove_tags, extract_number),
                            output_processor=TakeFirst())
    europa = scrapy.Field(input_processor=MapCompose(remove_tags, extract_number),
                            output_processor=TakeFirst())
    fabijoniskes = scrapy.Field(input_processor=MapCompose(remove_tags, extract_number),
                            output_processor=TakeFirst())
    perkunkiemis = scrapy.Field(input_processor=MapCompose(remove_tags, extract_number),
                            output_processor=TakeFirst())
    pilaite = scrapy.Field(input_processor=MapCompose(remove_tags, extract_number),
                            output_processor=TakeFirst())
    savanoriai = scrapy.Field(input_processor=MapCompose(remove_tags, extract_number),
                            output_processor=TakeFirst())
    silainiai = scrapy.Field(input_processor=MapCompose(remove_tags, extract_number),
                            output_processor=TakeFirst())
    zalgirioArena = scrapy.Field(input_processor=MapCompose(remove_tags, extract_number),
                            output_processor=TakeFirst())
    timeStamp = scrapy.Field(output_processor=TakeFirst())