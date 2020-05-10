'''
Created on 2020年5月10日

@author: 船长
'''
import requests
import re
import os
from urllib.request import urlretrieve
'''
1.分析梨视频网站
2.获取梨视频网页源代码
3.获取完整的梨视频视频播放地址
4.下载梨视频
'''
def downLoadVideo():
    
    #获取网页源代码(<Response [200]>表示成功！)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '+
            'Chrome/72.0.3610.2 Safari/537.36'
    }
    html = requests.get("https://www.pearvideo.com/category_8",headers = header).text;
    #print(html);
    
    #获取视频Id(根据正则表达式获取【(.*?)表示匹配所有】)
    reg = r'<a href="(.*?)" class="vervideo-lilink actplay">'
    videoIDs = re.findall(reg, html);
    #print(videoIDs)
    
    #拼接URL地址
    videoURL = []
    startURL = "https://www.pearvideo.com/"
    for videoID in videoIDs:
        newURL = startURL + videoID
        videoURL.append(newURL)

    #获取完整的视频播放地址
    for playURL in videoURL:
        html = requests.get(playURL,headers = header).text      #视频播放页页面源代码
        regMP4 = r'ldUrl="",srcUrl="(.*?)",vdoUrl'                 #通过re正则表达式匹配视频播放地址
        playMP4 = re.findall(regMP4, html)
        print(playMP4)
        regTitle = r'<h1 class="video-tt">(.*?)</h1>'
        videoName = re.findall(regTitle,html)
        print(videoName)
        print("正在下载视频：%s"%videoName[0])
        path = "E:/lishipin"
        if not os.path.exists(path):
            os.mkdir(path);
        filePath = path+"/%s.mp4"%videoName[0]
        urlretrieve(playMP4[0], filePath)
        
    
downLoadVideo()