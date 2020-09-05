import os
import json
import urllib.parse
import boto3
import cv2

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    s3 = boto3.client('s3')

    file_name = 'test.jpg'

    bucket_name = 'dex3w'
    key = 'cv-test/' + file_name

    # ローカルのファイル保存先を設定
    tmp_file_path = '/tmp/' + file_name

    try:
        # S3からファイルをダウンロード
        s3.download_file(bucket_name, key, tmp_file_path)

        # ダウンロードされているか確認
        print(os.listdir('/tmp'))

        # 画像処理
        orgImage = cv2.imread(tmp_file_path)
        grayImage = cv2.cvtColor(orgImage, cv2.COLOR_RGB2GRAY)
        gray_file_path = '/tmp/cv-test/processed-' + file_name
        cv2.imwrite(gray_file_path, grayImage)
        print('imwrite!: ' + gray_file_path)

        # S3にアップロード
        upload_key = 'cv-test/processed-' + file_name
        s3.upload_file(gray_file_path, bucket_name, upload_key)
        print('Upload!: ' + upload_key)

    except Exception as e:
        print(e)

    finally:
        # 後処理
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)
            print('Deleted!: ' + upload_key)

        if os.path.exists(gray_file_path):
            os.remove(gray_file_path)
            print('Deleted!: ' + gray_file_path)
