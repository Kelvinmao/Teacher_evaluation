import requests
from urllib import parse
from lxml import etree
from bs4 import BeautifulSoup


def login():
    url = 'http://jwxt.bupt.edu.cn/jwLoginAction.do'
    p_url = 'http://jwxt.bupt.edu.cn/validateCodeAction.do?'
    session = requests.session()
    image_data = session.get(p_url).content
    dest_url = "D:\\"
    print("保存验证码到D盘")
    try:
        with open(dest_url + "captcha.jpg", "wb") as jpg:
            jpg.write(image_data)
    except IOError:
        print("保存验证码失败")
    captcha = input("请输入验证码")
    param = {'type': 'sso',
             'zjh': '',//这里填账号
             'mm': '',//这里填密码
             'v_yzm': captcha
             }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Referer': 'http://jwxt.bupt.edu.cn/menu/s_menu.jsp',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    }
    response = session.post(url, data=param)
    return session


def evaluation_page():
    session = login()
    response = session.get("http://jwxt.bupt.edu.cn/jxpgXsAction.do?oper=listWj").text
    soup = BeautifulSoup(response, "html5lib")
    content = soup.find_all("img")
    # content=soup.img.get("name")
    class_info = []
    class_info_splited = []
    for item in content:
        if len(str(item)) > 150:
            class_info.append(item.get("name"))
            # print("ITEM is:%s ,LEN is:%d"%(item.get("name"),len(str(item))))

    for classes in class_info:
        teacher_info = str(classes).split("#@")
        class_info_splited.append(teacher_info)
    # for item in class_info_splited:
    #     print(item)
    return class_info_splited, session


def evaluate():
    class_info_list, session = evaluation_page()
    cookie = requests.utils.dict_from_cookiejar(session.cookies)
    header = {
        'Host':'jwxt.bupt.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '147',
        'Referer': 'http://jwxt.bupt.edu.cn/jxpgXsAction.do',
        'Cookie':'JSESSIONID='+cookie['JSESSIONID']
    }
    target_url = "http://jwxt.bupt.edu.cn/jxpgXsAction.do?oper=wjpg"
    for item in class_info_list:
        print(item)
        data = {

        }
        pre_post_data={

        }
        pre_post_data['wjbm']=item[0]
        pre_post_data['bpr']=item[1]
        pre_post_data['pgnr']=item[5]
        pre_post_data['oper']='wjShow'
        pre_post_data['wjmc']=item[3]
        pre_post_data['bprm']=item[2]
        pre_post_data['pgnrm']=item[4]
        pre_post_data['pageSize']='20'
        pre_post_data['page']='1'
        pre_post_data['currentPage']='1'
        pre_post_data['pageNo']=''

        pre_post_data=parse.urlencode(pre_post_data)
        # print(pre_post_data)
        response=session.post(url='http://jwxt.bupt.edu.cn/jxpgXsAction.do',data=pre_post_data,headers=header)
        # print(response.text)

        data['wjbm'] = item[0]
        data['bpr'] = item[1]
        data['pgnr'] = item[5]
        data['0000000054'] = "20_0.99"
        data['0000000055'] = "20_0.99"
        data['0000000056'] = "20_0.99"
        data['0000000057'] = "20_0.99"
        data['0000000058'] = "20_0.99"
        data['zgpj'] = ""
        response = session.post(target_url, data=data, headers=header)
        print(response.text)
    print("评估成功")


def choose_class_page():
    session = login()
    response = session.get("http://jwxt.bupt.edu.cn/xkAction.do?actionType=-1").text
    print(response)


def choose_class():
    pass


if __name__ == '__main__':
    evaluate()
    # choose_class_page()
