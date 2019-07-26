class HtmlOutputer(object):
    # 输出器
    def __init__(self):
        self.datas = []

    # 收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 将收集好的数据放到HTML
    def output_html(self):
        fout = open("output.html", 'w', encoding='utf-8')
        fout.write("<!DOCTYPE html>")
        fout.write("<html>")
        fout.write('<meta charset="UTF-8">')
        fout.write("<body>")
        fout.write("<table>")
        # ascii
        for data in self.datas:
            title = data['title']
            summary = data['summary']
            fout.write("<tr>")
            fout.write("<td>%s</td>"% data['url'])
            fout.write("<td>%s</td>"% title)
            fout.write("<td>%s</td>"% summary)
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

