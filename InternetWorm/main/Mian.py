import urllib.request;
#import urllib.parse;
#from idlelib.iomenu import encoding
#data = bytes(urllib.parse.urlencode({"wd":"聂强"}),encoding="utf8");
response = urllib.request.urlopen("https://baike.baidu.com/item/%E8%81%82%E5%BC%BA/2399694?fr=aladdin");
html = response.read();
print(html);