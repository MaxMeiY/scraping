import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = 'downloaded'
baseUrl = 'http://pythonscraping.com'

def getAbsoluteURL(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://{}'.format(source[11:])
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = source[4:]
        url = 'http://{}'.format(source)
    else:
        url = '{}/{}'.format(source)
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, dowloadDirectory):
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl, '')
    path = downloadDirectory + path
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

if __name__ == '__main__':
    html = urlopen('http://www.pythonscraping.com')
    bs = BeautifulSoup(html, 'html.parser')
    downloadList = bs.findAll(src=True)

    for download in downloadList:
        fileUrl = getAbsoluteURL(baseUrl, download['src'])
        if fileUrl is not None:
            print(fileUrl)
    urlretrieve(fileUrl, getDownloadPath(baseUrl,
                                         fileUrl,
                                         downloadDirectory))

