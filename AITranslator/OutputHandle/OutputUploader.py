import os
from qiniu import qiniu_client as qiniu

class OutputUploader(object):
    def upload(self,local_file_path,zip_name):
        remote_file_path = 'ai_translator/' + zip_name
        qiniu.qiniu_upload(local_file_path, remote_file_path)
        download_url = 'https://s.bongmi.com/' + remote_file_path
        return download_url


if __name__ == '__main__':
    #要压缩的文件夹路径
    local_file_path = '/Users/lettyliu/Git/AITranslator/YKSwiftDemo.zip'
    zip_name = 'YKSwiftDemo.zip'
    uploader = OutputUploader()
    uploader.upload(local_file_path,zip_name)
