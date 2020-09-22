"""
Author: Saeed Ketabi
Email: saeed.ketabi@gmail.com
Telegram: @Sbooki / @Sboooki
http://Boooki.ir

2020 september 21
"""

import requests
from lxml import html

from config.config import Config
from utilities.DataCleaner import DataCleaner
from utilities.utilities import Exporters

class DigikalaComments:

    def __init__(self,
                 clean_data=True):
        self.clean_data = clean_data
        self.exporter = Exporters()
        self.cleaner = DataCleaner()

    def get_comments(self,
                     product,
                     max_page=1000):
        """
        Get comments for a product
        :param product:
        :return:
        """
        page = 1
        while True:
            print("______________page:{page}______________".format(page=page))
            self._get_page_comments(product,page)
            page += 1
            if page > max_page:
                break

    def _get_page_comments(self,
                           product,
                           page):
        """
        ...
        :param product:
        :param page:
        :return:
        """
        url = "https://www.digikala.com/ajax/product/comments/list/{porduct}/?page={page}&mode=newest_comment".format(
            porduct=product, page=page)

        response = requests.request("GET", url, data={})

        text = response.text
        tree = html.fromstring(text)
        parent_tags = tree.xpath('//ul[@class="c-comments__list"]/li')
        for parent_tag in parent_tags:
            data = {}
            data['comment'] = " ".join(parent_tag.xpath(".//p/text()"))
            data['positives'] = parent_tag.xpath('.//div[@class="c-comments__evaluation-positive"]//li/text()')
            data['negatives'] = parent_tag.xpath('.//div[@class="c-comments__evaluation-negative"]//li/text()')
            data['opinion'] = " ".join(parent_tag.xpath('.//div[contains(@class,"c-message-light--opinion")]//text()'))
            if self.clean_data:
                data = self.cleaner.process(data)
            self.exporter.publish(data=data,file_name=product)


if __name__ == '__main__':
    crawler = DigikalaComments()
    crawler.get_comments("3168416",max_page=10)
