from bs4 import BeautifulSoup
import requests
import os
import sys

def getSoup(url : str) :
    # URL Initialization Check
        if len(url) > 0 :
            pass
        else :
            return "No URL specifed"
        
        # URL Integration Check
        if url.find("http://") > -1 or url.find("https://") > -1 :
            pass
        else :
            return "False URL"

        # Try Connection 
        response = requests.get(url)

        #Connection Failure Check
        if response:
            pass
        else :
            return "Connection Failure:" + response.status_code

        #Parsing HTML to BS4
        return BeautifulSoup(response.text, 'lxml')

class ImageDownloader:
    def __init__(self, url : str = "", saveDirectory : str = "./temp", verbose : bool = False):
        self.url : str = url
        self.path : str = saveDirectory
        self.verbose : bool = verbose

    def setSoup(self):
        self.soup = getSoup(self.url)

    def setImgTags(self):
        self.imgTags = self.soup.body.find_all("img")

    def download(self):

        #Count img tag
        img_count = len(self.imgTags)
        work_count = 0
        fail_count = 0

        #Create directory if not exist

        if not os.path.exists(self.path) :
            os.mkdir(self.path)#, 0o777)

        # Do download
        for i in self.imgTags:
            work_count += 1
            print("[", work_count, "/", img_count, "]")
            if i.has_attr('src') :
                str = i['src']
                index = str.rfind('/')
                filePath = self.path + "/" + str[index + 1:]
                
                try:
                    response = requests.get(str, stream=True)
                except :
                    print("Img URL connection fail:", response)
                    fail_count += 1
                else :
                    with open(filePath, "wb") as fp:
                        content = response.content
                        fp.write(content)
                        print("file saved:",filePath)
                
                    fp.close()
            
            else :
                fail_count += 1
                print("No img url")

        print("Download finished")
        print(fail_count ," out of ", img_count, " failed")

    def start(self) :
        self.setSoup()
        self.setImgTags()
        self.download()

    def start(self, url : str) :
        self.url = url
        self.setSoup()
        self.setImgTags()
        self.download()

    def start(self, url : str, path : str) :
        self.url = url

        if len(path) > 0 :
            self.path = path
        else :
            pass

        self.setSoup()
        self.setImgTags()
        self.download()
