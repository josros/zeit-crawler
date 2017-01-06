# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from collections import Counter
import logging
import re

logger = logging.getLogger()

class ZeitDropEmptyPipeline(object):
    def process_item(self, item, spider):
        logger.log(logging.DEBUG, 'Called ZeitDropEmptyPipeline for %s' % item['link'])

        if item['body'] and item['dates']:
            return item
        else:
            logger.log(logging.DEBUG, 'Drop item %s' % item['link'])
            raise DropItem("Drop item without body and dates")

class WordCountPipeline(object):
    def process_item(self, item, spider):
        logger.log(logging.DEBUG, 'Called WordCountPipeline for %s' % item['link'])

        relevantText = item['body'] + item['summary'] + item['header'] + item['subheaders']
        counts = Counter()
        wordpattern = re.compile(r'\w+', flags=re.UNICODE)

        for sentence in relevantText:
            counts.update(wordpattern.findall(sentence.lower()))
        item['wordcount'] = counts

        return item
