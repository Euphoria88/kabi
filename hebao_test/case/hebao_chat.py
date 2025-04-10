import requests
import yaml
import os

from hebao_test.case.hebao_login import Login

token = Login("+8618716202139")

header = {
    "Content-Type":"application/json",
    "Authorization": f'Bearer {token}'
}

def read_yaml_file(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        data = yaml.load(file,Loader=yaml.FullLoader)
        return data

data = read_yaml_file('D:\pythonProject\hebao_test\static\chat_meaasge.yaml')
param = data['message']
for message in param:
    print(message)


def KeeperChat(param):
    chat_url = "http://124.220.33.63:8705/api/keeper/chat"
    chat_data = {
        "message": param
    }
    chat_resp = requests.post(url=chat_url, headers=header, json=chat_data)
    print(param)
    return


if __name__ =='__main__':
    KeeperChat(param)