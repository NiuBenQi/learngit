# 爬虫总调度程序
from baike_spider import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        # 爬虫调度程序
        self.urls.add_new_url(root_url)
        # 循环当URL管理器当中的URL地址 然后把新的URL添加到URL管理器中
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s"%(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_url, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_url)
                # 收集数据，把新的数据放到datas
                self.outputer.collect_data(new_data)

                if count == 100:
                    break
                count = count + 1
            except:
                print("craw failed")
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)



