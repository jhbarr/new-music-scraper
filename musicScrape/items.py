# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicscrapeItem(scrapy.Item):
    song_name = scrapy.Field()
    artist = scrapy.Field()
    genre = scrapy.Field()


