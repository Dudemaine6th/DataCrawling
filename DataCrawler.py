from bs4 import BeautifulSoup
import requests
import os
import sys

class ImageDownloader:
    def __init__(self, url : str = "", saveDirectory : str = "./temp", verbose : bool = False):
        self.url : str = url
        self.path : str = saveDirectory
        self.verbose : bool = verbose

    def setUrl(self, url : str):
        self.url = url

    def setSaveDirectory(self, saveDirectory : str):
        self.path = saveDirectory

    def setVerbose(self, verbose : bool):
        self.verbose = verbose

    def start(self):

        # URL Initialization Check
        if len(url) == 0 :
            return "No URL specifed"
        else :
            pass
        
        # URL Integration Check
        #if url.find("http://") < 0 || url.find("https://") < 0 :
        #    return "False URL"
        #else :
        #    pass

        # Try Connection 
        response = requests.get(self.url)

        #Connection Failure Check
        if response:
            pass
        else :
            return "Connection Failure:" + response.status_code

        #Parsing HTML to BS4
        soup = BeautifulSoup(response.text, 'lxml')
        
        #Specifying img tag
        soupBodyImg = soup.body.find_all("img")

        #Count img tag
        img_count = len(soupBodyImg)
        work_count = 0
        fail_count = 0

        #Create directory if not exist

        if not os.path.exists(self.path) :
            os.mkdir(self.path,0o777)

        # Do download
        for i in soupBodyImg:
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

if __name__== "__main__":
    imgDown = ImageDownloader()
    url = input('Enter url:')

    imgDown.setUrl(url)

    imgDown.start()
        