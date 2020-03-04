from selenium import webdriver
from time import sleep,ctime
import time
import winsound
import threading

def login():
    browser.get("https://www.taobao.com")
    time.sleep(0)
    if browser.find_element_by_link_text ("亲，请登录"):
        browser.find_element_by_link_text ("亲，请登录").click ()
        time.sleep(10)

def mon(url):
    browser.get(url)
    global state
    js1 = '''Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) '''
    js2 = '''window.navigator.chrome = { runtime: {},  }; '''
    js3 = '''Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); '''
    js4 = '''Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); '''
    browser.execute_script(js1)
    browser.execute_script(js2)
    browser.execute_script(js3)
    browser.execute_script(js4)
    time.sleep(0)
    try:
        stock = browser.find_element_by_id("J_EmStock").text
        state=1
    except:
        print(f'没有找到库存信息')
        state=0

def clear ():
        drive .delete_all_cookies ()
        global times
        times =0
        print ("已清除缓冲区")

def buy():
    num=0
    while num<1:
        try:
            browser.find_element_by_id("J_LinkBuy").click()
            time.sleep(0.5)
            browser.find_element_by_class_name("go-btn").click()
            return 1
            break
        except:
            num=num+1
            print('库存:',num)

if __name__=='__main__':
    option=webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches',['enable-automation'])
    browser=webdriver.Chrome(chrome_options =option )
    times=1            
    print('输入抢购时间:')
    timeCheck = input()
    print('输入抢购网址:')
    url = input()
    login()
    i = True
    while i:
        t = time.strftime("%Y%m%d%H%M%S", time.localtime())
        print(t)
        if int(t) > int(timeCheck)-2:
            while True :
                mon (url)
                if state ==1 :
                    success =buy ()
                    if success ==1 :
                        print ('成功')
                        winsound .Beep (500 ,2000 )
                        break
                        break
                if times >=100 :
                    clear ()