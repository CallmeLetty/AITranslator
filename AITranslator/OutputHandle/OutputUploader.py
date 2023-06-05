# -*- encoding: utf-8 -*-
import sys
import requests
import datetime
from qiniu import qiniu_client as qiniu

class OutputUploader(object):
    def upload(self,local_file_path,zip_name):
        remote_file_path = 'ai_translator/' + zip_name
        qiniu.qiniu_upload(local_file_path, remote_file_path)
        download_url = 'https://s.bongmi.com/' + remote_file_path
        return download_url


    def notifyToFeishu(self,path):
        # 发通知给飞书机器人
        url = 'https://www.feishu.cn/flow/api/trigger-webhook/d5d92a505be9890b1d2e18c43a541197'
        headers = {'Content-Type':'application/json'}
        
        data = {"zip_path": path}
        res= requests.request("POST",url=url,headers=headers,json=data)
        print(res)
        print(res.json())

if __name__ == '__main__':
    #要压缩的文件夹路径
    local_file_path = '/Users/lettyliu/Git/AITranslator/YKSwiftDemo.zip'
    zip_name = 'YKSwiftDemo.zip'
    uploader = OutputUploader()
    uploader.upload(local_file_path,zip_name)
