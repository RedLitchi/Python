#‪coding:utf-8
import itertools as its             #‪迭代器
#words = "1234567890"
#r = its.product(words, repeat=11)   #‪生成密码本的位数，五位数，repeat=5
#‪保存在文件中，追加
#dic = open("D:/AWorkSpace/PythonWorkSpace/PythonStudy/src/nieqiang/password.txt", "a")
#‪i是元组
#for i in r:
#    dic.write("".join(i))           # jion空格链接
#    dic.write("".join("\n"))
#    print(i)
#dic.close()
#print("密码本已生成")



"""
电信号段：133/153/180/181/189/177;
联通号段：130/131/132/155/156/185/186/145/175;
移动号段：134/135/136/137/138/138/150/151/152/154/157/158/159/182/183/184/187/188/147/178;
第一位：1；
第二位：3，4，5，7，8
第三位：
3：【0，9】
4：【5，7】
5：【0，9】 ！4
7：【6，7，8】
8：【0-9】
"""
import random
def creatPhone():
    #第二位数
    second = [3,4,5,7,8][random.randint(0,4)]
    #第三位数
    third = {
        3:random.randint(0,9),
        4:[5,7][random.randint(0,1)],
        5:[i for i in range(0,10) if i != 4][random.randint(0,8)],
        7:[6, 7, 8][random.randint(0,2)],
        8:random.randint(0,9)
    }[second]
    
    #后八位数
    suffix = ''
    for j in range(0, 8):
        suffix = suffix + str(random.randint(0,9))
    #print("1{}{}{}".format(second, third, suffix))
    return "1{}{}{}".format(second, third, suffix)
    

output = int(input("请输入需要获取电话号码的个数："))
for i in range(output):
    print(creatPhone())
    dic = open("D:/AWorkSpace/PythonWorkSpace/PythonStudy/src/nieqiang/password.txt", "a")
    dic.write(creatPhone())           # jion空格链接
    dic.write("".join("\n"))
    dic.close()
print("密码本已生成")