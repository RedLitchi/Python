import pywifi
from pywifi import const                #引入定义


def gic():
    wifi = pywifi.PyWiFi();             #创建无线网卡对象
    ifaces = wifi.interfaces();         #获取无线网卡
    name = ifaces[0].name();            #获取无线网卡名称
    print("无线网卡名称:"+name);
    if ifaces.status() == const.IFACE_DISCONNECTED:         #判断WiFi是否连接 0是未连接
        print("WiFi未连接！")
    else:
        print("WiFi已连接！")
gic()


#扫描附近WiFi
def bies():
    wifi = pywifi.PyWiFi()              #创建无线网卡对象
    ifaces = wifi.interfaces()[0]       #获取无线网卡
    ifaces.scan()                       #扫描附近WiFi
    bessis = ifaces.scan_results()      #返回扫描结果
    print(bessis)                       #如果结果为空多执行几次就会出来了
    for wifi in bessis:
        print("附近所有WiFi的名称："+wifi.ssid)
    

bies() 