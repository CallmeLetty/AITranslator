# -*- encoding: utf-8 -*-
import sys
import requests
import json
from qiniu import qiniu_client as qiniu

class OutputUploader(object):
    def upload(self,local_file_path,zip_name):
        remote_file_path = 'ai_translator/' + zip_name + '.zip'
        qiniu.qiniu_upload(local_file_path, remote_file_path)
        download_url = 'https://s.bongmi.com/' + remote_file_path
        print("download_url: " + download_url)
        return download_url


    def notifyToFeishu(self,path):
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
        myobj = {'app_id': 'cli_a4f7fd9a0d3bd013', "app_secret": "baSbQ0YI86ZySbiRsPzvBjRZ5QyWzY4m"}
        raw_text = requests.post(url, data = myobj).text
        dict = json.loads(raw_text)
        token = dict['tenant_access_token']
        
        # 发通知给飞书机器人
        url = 'https://www.feishu.cn/flow/api/trigger-webhook/d5d92a505be9890b1d2e18c43a541197'
        headers = {'Content-Type':'application/json',
                   'Authorization': "Bearer %s" % token}
        
        data = {"zip_path": path}
        # data = {"name":"hello"}
        
        res= requests.request("POST",url=url,headers=headers,json=data)
        
        dict = json.loads(res.content)
        print(dict)
        print(res.json())

if __name__ == '__main__':
    #要压缩的文件夹路径
    # local_file_path = '/Users/lettyliu/Downloads/2023-06-05-11-02-18.zip'
    # zip_name = '2023-06-05-11-02-18.zip'
    uploader = OutputUploader()
    # url = uploader.upload(local_file_path,zip_name)
    url = 'https://s.bongmi.com/ai_translator/2023-06-05-11-02-18.zip'
    uploader.notifyToFeishu(url)
