# -*- coding: utf-8 -*-
import json

import scrapy

from u17.agent_helper import get_random_agent
from u17.items import U17Item


class ManhuaSpider(scrapy.Spider):
    name = 'manhua'
    allowed_domains = ['www.u17.com']
    start_urls = ['http://www.u17.com/']

    def start_requests(self):
        headers = {
            'User-Agent': get_random_agent(),
            'Host': 'www.u17.com',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        url = 'http://www.u17.com/comic/ajax.php?mod=comic_list&act=comic_list_new_fun&a=get_comic_list'

        post_data = {
            'data[accredit]': 'no',
            'data[color]': 'no',
            'data[comic_type]': 'no',
            'data[group_id]': 'no',
            'data[is_vip]': 'no',
            'data[order]': '2',
            'data[page_num]': '1',
            'data[read_mode]': 'no',
            'data[series_status]': 'no',
            'data[theme_id]': 'no',
        }
        for i in range(1, 411):
            post_data['data[page_num]'] = str(i)
            yield scrapy.FormRequest(url=url,
                                     callback=self.parse,
                                     headers=headers,
                                     method='POST',
                                     formdata=post_data)

    def parse(self, response):
        request_json = json.loads(response.text)['comic_list']
        for j_item in request_json:
            item = U17Item()
            item['comic_id']= j_item.get('comic_id', '')
            item['title']= j_item.get('name', ''),
            item['cover'] = j_item.get('cover', '')
            item['classfy'] = item.get('line2', '')
            yield item


