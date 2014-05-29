import HTMLParser
import basesixtyfour
import re
def allin1(template, out):
    class Parser(HTMLParser.HTMLParser):
        def __init__(self):
            self.icons = {}
            HTMLParser.HTMLParser.__init__(self)
        def handle_starttag(self, tag, attrs):
            if tag == 'img':
                for key, value in attrs:
                    if key == 'class' and value == 'icon':
                        for k, v in attrs:
                            if k == 'src':
                                self.icons[v] = basesixtyfour.encode(v)
    html = ''
    with open(template, 'rb') as index:
        html = index.read()
        index.close()
    p = Parser()
    p.feed(html)
    for key, value in p.icons.iteritems():
        html = html.replace('src="'+key+'"', 'src="data:image/x-icon;base64,'+value+'"')
    with open(out, 'wb') as index:
        index.write(html)
        index.close()
if __name__ == '__main__':
    allin1('index.standard.html', 'index.html')
