import requests

#注册账号
def EnrollLogin(phone):
    """
    :param phone: 自己登录手机号
    :return: user_id
    """
    code_url = 'http://124.220.33.63:8705/sms/login/send'
    login_url = 'http://124.220.33.63:8705/login/phone'
    header = {
        'Content-Type': 'application/json'

    }
    code_data = {
        "to": phone
    }
    code_res = requests.post(url=code_url, headers=header, json=code_data)
    # print(code_res.json())
    code = code_res.json().get('data').get('code')
    # print(code)
    login_data = {
      "Phone": phone,
      "PhoneCode": code
    }
    login_res = requests.post(url=login_url, headers=header, json=login_data)
    # print(login_res.json())
    user_id, token = login_res.json().get('data')[0].get('user_id'), login_res.json().get('data')[0].get('token')
    # print(token)
    # return token
    print(user_id, token)
    return token, user_id


if __name__ == '__main__':
    EnrollLogin('+8619180684952')
                # EnrollLogin('+8615911111110',+8615911111111,+8615911111112,+8615911111113,+8615911111114,+8615911111115,+8615911111116,+8615911111117,+8615911111118,+8615911111119,+8615911111120,+8615911111121,+8615911111122,+8615911111123,+8615911111124,+8615911111125,+8615911111126,+8615911111127,+8615911111128,+8615911111129,+8615911111130,+8615911111131,+8615911111132,+8615911111133,+8615911111134,+8615911111135,+8615911111136,+8615911111137,+8615911111138,+8615911111139,+8615911111140,+8615911111141,+8615911111142,+8615911111143,+8615911111144,+8615911111145,+8615911111146,+8615911111147,+8615911111148,+8615911111149,+8615911111150,+8615911111151,+8615911111152,+8615911111153,+8615911111154,+8615911111155,+8615911111156,+8615911111157,+8615911111158,+8615911111159,+8615911111160,+8615911111161,+8615911111162,+8615911111163,+8615911111164,+8615911111165')
