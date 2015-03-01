
'''

@author: wangcongjun
'''
import requests
from bs4 import BeautifulSoup
class Spider(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def getInfo(self):

        response = requests.get("http://jecvay.com")
        soup = BeautifulSoup(response.text)
        for x in soup.findAll("a"):
            print(x['href'])
#         print(soup.body.text)
        
if __name__ == '__main__':
    s = Spider()
    s.getInfo()