import urllib2
import time

def commentExtraction(html):
    url = []
    # cursor = 0
    # nlinks=0
    # while (cursor>=0 and nlinks<max_links):
    #     start_link = html.find("a href",cursor)
    #     if start_link==-1:
    #         return url
    #     start_quote = html.find('"', start_link)
    #     end_quote = html.find('"', start_quote + 1)
    #     url.append(html[start_quote + 1: end_quote])
    #     cursor = end_quote+1
    #     nlinks = nlinks +1
    source = urllib2.urlopen('http://www.htmlcodetutorial.com/_33n45n45n.html').read()
    items = source.find("!--",0)
    items2 = source.find("--",0)
    
    print source[items:items2]
    
    return url

commentExtraction('http://google.com')