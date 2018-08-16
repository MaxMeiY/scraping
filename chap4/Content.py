import requests
from bs4 import BeautifulSoup

class Content:
    """
    Common base class for all articles/pages
    """

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Flexible printing function controls output
        """
        print("URL: {}".format(self.url))
        print("TITLE: {}".format(self.title))
        print("BODY:\n{}".format(self.body))

class Website:
    """
    Contains information about website structure
    """

    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Crawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):

        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join(
            [elem.get_text() for elem in selectedElems])
        return ''

    def parse(self, site, url):
        """
        Extract content from a given page URL
        """
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()


if __name__ == "__main__":
    crawler = Crawler()

    siteData = [
        ['OReilly Media', 'http://oreilly.com',
         'h1', 'section#product-description'],
        ['Reuters', 'http://reuters.com','h1',
         'div.standardArticleBody_body_1gnLA'],
        ['Brookings', 'http://www.brookings.edu',
         'h1', 'div.post-body'],
        ['New York Times', 'http://nytimes.com',
         'h1', 'p.story-content']
    ]
    websites = []
    for row in siteData:
        websites.append(Website(row[0],row[1],row[2],row[3]))

    crawler.parse(websites[0], 'http://shop.oreilly.com/product/0636920028154.do')


