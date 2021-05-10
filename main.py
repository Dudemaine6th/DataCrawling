from DataCrawler import ImageDownloader as ImgDn

obj = ImgDn()

url = input('Enter url:')
path = input('Enter save path(press enter to set default path ./temp):')

obj.start(url, path)
