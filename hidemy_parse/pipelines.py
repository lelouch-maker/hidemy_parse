# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HidemyParsePipeline:
    def process_item(self, item, spider):

        #print(item)
        self.f.write(item['protocol']+'://'+item['ip']+':'+item['port']+'\n')

        return item

    def __init__(self):
        self.f = open('text.txt','w')