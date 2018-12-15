# -*- coding: utf-8 -*-
import scrapy
import json

from python_lagou.agent_helper import get_random_agent
from python_lagou.items import PythonLagouItem


# 通过网页分析，拉钩职位详情是ajax请求渲染后的数据，爬取方式为模拟ajax请求得到返回的json数据
class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['www.lagou.com/']

    def start_requests(self):
        # 设置请求头
        headers = {
            'User-Agent': get_random_agent(),
            'Host': 'www.lagou.com',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'Content - Length': '25',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        }
        # 爬取的目标网址，为成都Python职位
        url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false'
        # 设置cookies值，拉勾网在请求中设置了反爬，经过反复研究，在request请求中传入浏览器cookies值可破解反爬
        cookies = {
            'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1544846652',
            'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1544838537',
            'JSESSIONID': 'ABAAABAAAIAACBICFE5234BA15FDC627B4BC2AC26939066',
            'LGRID': '20181215120410-79e6580f-001e-11e9-9214-525400f775ce',
            'LGSID': '20181215114422-b5d98d8b-001b-11e9-9212-525400f775ce',
            'LGUID': '20181113163647-4256c742-e71f-11e8-889d-5254005c3644',
            'PRE_HOST': '',
            'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
            'PRE_SITE': '',
            'PRE_UTM': '',
            'SEARCH_ID': '5cf112be57c84094aa5e7e3eb0deaa2f',
            'TG-TRACK-CODE': 'index_search',
            'X_HTTP_TOKEN': '5a8cf754b1f5597b17e1feba754901fa',
            '_ga': 'GA1.2.2050831025.1542098234',
            '_gat': '1',
            '_gid': 'GA1.2.1994034343.1544838556',
            'index_location_city': '%E6%88%90%E9%83%BD',
            'sajssdk_2015_cross_new_user': '1',
            'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22167affba6bc38-05c40b1abf0805-323b5b03-1296000-167affba6bf216%22%2C%22%24device_id%22%3A%22167affba6bc38-05c40b1abf0805-323b5b03-1296000-167affba6bf216%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
            'user_trace_token': '20181113163647-4256c3ab-e71f-11e8-889d-5254005c3644',

        }
        # 爬取30个页面
        for page in range(1, 31):
            # POST请求参数设置
            post_data = {
                'first': 'true',
                'pn': str(page),
                'kd': 'python',
            }
            # 构建POST请求
            yield scrapy.FormRequest(url=url,
                                     callback=self.parse,
                                     headers=headers,
                                     method='POST',
                                     formdata=post_data,
                                     cookies=cookies,
                                     )

    # 页面解析
    def parse(self, response):
        request_json = json.loads(response.text)['content']['positionResult']['result']
        print(request_json)
        for j_item in request_json:
            item = PythonLagouItem()
            item['companyFullName'] = j_item.get('companyFullName')
            item['companyLabelList'] = j_item.get('companyLabelList')
            item['companyShortName'] = j_item.get('companyShortName')
            item['companySize'] = j_item.get('companySize')
            item['createTime'] = j_item.get('createTime')
            item['district'] = j_item.get('district')
            item['education'] = j_item.get('education')
            item['financeStage'] = j_item.get('financeStage')
            item['firstType'] = j_item.get('firstType')
            item['formatCreateTime'] = j_item.get('formatCreateTime')
            item['imState'] = j_item.get('imState')
            item['industryField'] = j_item.get('industryField')
            item['positionAdvantage'] = j_item.get('positionAdvantage')
            item['positionLables'] = j_item.get('positionLables')
            item['positionName'] = j_item.get('positionName')
            item['salary'] = j_item.get('salary')
            item['thirdType'] = j_item.get('thirdType')
            item['workYear'] = j_item.get('workYear')
            yield item
