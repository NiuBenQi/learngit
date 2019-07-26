class UrlManager(object):
    # url管理器 维护两个list 1.带爬取的URL  2.已经爬取的URL
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    # 添加新的URL
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    # 添加新的URL（批量添加）
    def add_new_urls(self, urls):
        if urls is None or len(urls) ==0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        # pop 从list中获取一个URL 并移除一个URL
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
