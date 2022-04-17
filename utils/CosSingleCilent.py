import requests
import json
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


class StorageClient:
    secret_id = ''
    secret_key = ''
    secret_token = ''
    ExpiredTime = 0
    region = 'ap-shanghai'
    bucket = '7072-prod-4gtr7e0o54f0f5ca-1309638607'
    secret_url = 'http://api.weixin.qq.com/_/cos/getauth'
    cos_config = None
    cos_client = None

    def FreshSecret(self):
        msg = json.loads(requests.get(self.secret_url).text)
        self.secret_id = msg["TmpSecretId"]
        self.secret_key = msg["TmpSecretKey"]
        self.secret_token = msg["Token"]
        self.ExpiredTime = int(msg["ExpiredTime"])
        self.cos_config = CosConfig(Region=self.region, SecretId=self.secret_id, SecretKey=self.secret_key,
                                    Token=self.secret_token)
        self.cos_client = CosS3Client(self.cos_config)

    def write_file(self, filepath, filename, localpath):
        self.FreshSecret()
        with open(localpath+filename, 'rb') as fp:
            response = self.cos_client.put_object(
                Bucket=self.bucket,
                Body=fp,
                Key=filepath+filename,
            )


cos = StorageClient()
