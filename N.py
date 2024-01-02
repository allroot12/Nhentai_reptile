# 爬虫
from DrissionPage import ChromiumPage
from time import sleep

def N(VarUrl,VarPath):
    num = 0                                                       #第0个开始
    url = VarUrl                                                  #网址
    path = VarPath                                                #本地地址

    # 跳过cloudflare的点击验证
    p = ChromiumPage()
    p.get(f'{url}')
    iframe = p.get_frame('@src^https://challenges.cloudflare.com/cdn-cgi')
    if iframe:
        sleep(0)
        iframe('.mark').click()

    #寻找并获取元素
    father = p.eles('xpath:/html/body/div[2]/div[2]/div[1]/div')
    lens = len(father)

    #进入详情页
    for i in range(num,lens):
        url2 = url+str(num+1)+"/"
        p.get(f'{url2}')
        img = p.ele('xpath:/html/body/div[2]/section[3]/a/img')
        img.save(path)                                              #保存地址
        num = num + 1