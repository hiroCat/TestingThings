import urllib2
import logging
import time

class Spider:
    def __init__(self,starting_url,crawl_domain,max_iter):
        self.crawl_domain = crawl_domain
        self.max_iter = max_iter
        self.links_to_crawl=[]
        self.links_to_crawl.append(starting_url)
        self.links_visited=[]
        self.collection=[]
        
    def retrieveHtml(self):
        try:
            socket = urllib2.urlopen(self.url);
            self.html = socket.read()
            return 0
        except urllib2.HTTPError as ex:
            logging.exception("WrongUrl", ex.message)
            return -1
             
    def run(self):
        while (len(self.links_to_crawl)>0 and len(self.collection)<self.max_iter):
            self.url = self.links_to_crawl.pop(0)
            print self.links_to_crawl
            self.links_visited.append(self.url)
            if self.retrieveHtml()>=0:
                self.storeHtml()
                self.retrieveAndValidateLinks()
    
    def retrieveAndValidateLinks(self):
        tmpList=[]
        items = getLinks(self.html)
        # Check the validity of a link
        for item in items:
            item = item.strip('"')
            if self.crawl_domain in item:
                tmpList.append(item)
            if not(":") in item: #Take care of http:// https:// and mailto:
                tmpList.append(self.crawl_domain+item)
        # Check that the link has not been previously retrieved or is currently on the links_to_crawl list
        for item in tmpList:
            if item not in self.links_visited:
                if item not in self.links_to_crawl:
                    self.links_to_crawl.append(item)
                    print 'Adding: '+item
                
    def storeHtml(self):
        doc = {}
        doc['url'] = self.url
        doc['date'] = time.strftime("%d/%m/%Y")
        doc['html'] = self.html
        self.collection.append(doc)
       