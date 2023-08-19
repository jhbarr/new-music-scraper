import scrapy
from musicScrape.items import MusicscrapeItem


class PitchforkspiderSpider(scrapy.Spider):
    name = "pitchforkSpider"
    allowed_domains = ["pitchfork.com"]
    start_urls = ["https://pitchfork.com/reviews/tracks/"]

    custom_settings = {
        'FEEDS' : {
            './newMusic.json' :{'format' : 'json', 'overwrite' : True}
        },
        'ITEM_PIPELINES' : {
            'musicScrape.pipelines.MusicscrapePipeline': 300,
        }

    }

    pages_counted = 0
    
    def parse(self, response):
        songs = response.css('div.track-collection-item')

        for track in songs:
            track_info_page = track.css('a.track-collection-item__track-link::attr(href)').get()

            track_info_url = 'https://pitchfork.com' + track_info_page
            yield response.follow(url=track_info_url, callback=self.parse_track_page)


        next_page = response.xpath('//link[@rel="next"]').attrib['href']
        if self.pages_counted < 2:
            next_page_url = next_page
            self.pages_counted += 1
            yield response.follow(url=next_page_url, callback=self.parse)

    def parse_track_page(self, response):
        track_item = MusicscrapeItem()

        track_item['song_name'] = response.xpath('//h1[@class="BaseWrap-sc-gjQpdd BaseText-ewhhUZ SplitScreenContentHeaderHed-lcUSuI iUEiRd fnwdMb fTtZlw"]/text()').get()
        track_item['artist'] = response.xpath('//div[@class="BaseWrap-sc-gjQpdd BaseText-ewhhUZ SplitScreenContentHeaderArtist-ftloCc iUEiRd jqOMmZ kRtQWW"]/text()').get()
        track_item['genre'] = response.xpath('//p[@class="BaseWrap-sc-gjQpdd BaseText-ewhhUZ InfoSliceValue-tfmqg iUEiRd dcTQYO fkSlPp"]/text()').get()

        yield track_item
