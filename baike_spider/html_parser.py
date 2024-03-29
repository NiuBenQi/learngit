from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse,urljoin
class HtmlParser(object):
    # HTML解析器
    # 获取新的URL
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /item/%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80/2317999
        # 使用正则表达式匹配页面中符合条件的链接
        links = soup.find_all('a',href = re.compile(r"/item/\S+/\d+"))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    # 获取新的数据
    def get_new_data(self, page_url, soup):
        res_data = {}
        #url
        res_data['url'] =page_url
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title']= title_node.get_text()
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        # print(res_data['url'],res_data['title'],res_data['summary'])
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self.get_new_data(page_url,soup)
        return new_urls,new_data