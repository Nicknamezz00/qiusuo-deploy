import hashlib
import logging
import os
import sys

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


class StorageClient:
    secret_id = 'AKIDe8OPBhxyjEqFOIwLUO2RdbKo21lFVWHm'
    secret_key = 'JOEo9E4ez4vXt1uXu2uXu2uWt0rTpwoS'
    secret_token = None
    region = 'ap-guangzhou'
    bucket = 'qiusuo-1310314982'
    cos_config = None
    cos_client = None

    def FreshSecret(self):
        self.cos_config = CosConfig(
            Region=self.region,
            SecretId=self.secret_id,
            SecretKey=self.secret_key,
            Token=self.secret_token)
        self.cos_client = CosS3Client(self.cos_config)

    def write_file(self, filepath, filename, localpath):
        self.FreshSecret()
        print(self.cos_config)
        with open(localpath + filename, 'rb') as fp:
            data = fp.read()
        file_md5 = hashlib.md5(data).hexdigest()
        with open(localpath + filename, 'rb') as fp:
            response = self.cos_client.put_object(
                Bucket=self.bucket,
                Body=fp,
                Key=filepath + file_md5 + '.' + filename.split('.')[-1],
            )
        os.remove(localpath + filename)
        return filepath + file_md5 + '.' + filename.split('.')[-1]


cos = StorageClient()
