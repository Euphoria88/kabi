from urllib.parse import urljoin

import requests


header={
    "Content_type":"application/json",

}

# 注册-发送短信验证码
def RegistSms(phone):
    url = "http://124.220.33.63:8705/sms/login/send"
    register_data ={
        "to":phone
    }
    code_res = requests.post(url=url,headers=header,data=register_data)
    code = code_res.json().get('data').get('data').get('code')
    return code

def PhoneLogin(phone):
    code = RegistSms(phone)
    login_data = {
        "Phone": phone,
        "PhoneCode":code
    }
    url = "http://124.220.33.63:8705/login/phone"
    login_res = requests.post(url=url, headers=header,data=login_data )
    token = login_res.json().get('data')[0].get('token')
    id = login_res.json().get('data')[0].get('id')
    return token,id

# 获取用户信息--若用户未匹配则走匹配流程，若已匹配则忽略
def GetuserInfo(phone):
    token,id = PhoneLogin(phone)
    url = "http://124.220.33.63:8705/admin/user/{id}"
    header = {
        "Authorization": f'Bearer {token}'
    }
    res = requests.get(url=url,headers=header)
    match_id = res.json().get('data').get('matchID')
    if match_id == 0:
        url= "http://124.220.33.63:8705/api/match"
        match_data={
            "code":"123456"
        }
        match_res = requests.post(url=url,headers=header,data=match_data)
        return match_res.status_code
    else:
        return res.status_code

# 注销用户
def Deleteuser(phone):
    token, id = PhoneLogin(phone)
    url = "http://124.220.33.63:8705/admin/user/{id}"
    header = {
        "Authorization": f'Bearer {token}'
    }
    res = requests.get(url=url, headers=header)
    match_id = res.json().get('data').get('matchID')
    if match_id == 0:
        url = ""
        res = requests.delete(url=url,headers=header)
        print('注销成功')
    else:
        print('注销账号前需先解除匹配')


# 获取流水信息
def GetFlows():
    # 从哪里获取时间（年，月）的值
    # 传参：年，月的值传递url中
    url = "http://124.220.33.63:8705/api/flows"
    flows_res = requests.get(url=url,headers=header)
    flows_data = flows_res.json()
    print(flows_data)


#



if __name__ == '__main__':
     PhoneLogin('+86')
