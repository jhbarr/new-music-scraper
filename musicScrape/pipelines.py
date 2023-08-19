# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MusicscrapePipeline:

    #MUST use process_item function keyword
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        song_string = adapter.get('song_name')
        clean_string = [song_string[i] for i in range(1,len(song_string) - 1)]
        adapter['song_name'] = "".join(clean_string)

        return item

