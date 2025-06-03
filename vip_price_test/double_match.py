import requests
from RegistLogin import EnrollLogin
from match import GetMatchCode

match_code = GetMatchCode('+8613520201010')

#注册新账号去匹配
def AutoMatch():
    token = EnrollLogin('+8613510102020')
    match_url = 'http://124.220.33.63:8705/api/match'
    header = {
        "Content_Type": "application/json",
        "Authorization": f'Bearer {token}',
    }
    match_data={
        "code" : match_code
    }
    match_res = requests.post(url=match_url,headers=header,json=match_data)
    print(match_res.json())
    return


if __name__ == '__main__':
     AutoMatch()