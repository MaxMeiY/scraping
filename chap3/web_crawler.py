from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.Now())

# Retrieves a list of all Internal links found on a page
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme,
                                  urlparse(includeUrl).netloc)
    internalLinks = []
    # Finds all lnks that begin with a "/"
    for link in bs.find_all(
            'a',href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.atts['href'] not in internalLinks:
                if (link.attrs['href'].startswith('/')):
                    internalLinks.append(
                        includeUrl + link.atts['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks
