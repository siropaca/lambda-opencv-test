import os
import json
import urllib.parse
import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    s3 = boto3.client('s3')

    file_name = 'test.jpg'

    bucket_name = 'whitenote'
    key = 'test/' + file_name

    # ローカルのファイル保存先を設定
    tmp_file_path = '/tmp/' + file_name

    try:
        # S3からファイルをダウンロード
        s3.download_file(bucket_name, key, tmp_file_path)

        # ダウンロードされているか確認
        print(os.listdir('/tmp'))

        upload_key = 'test/processed-' + file_name
        s3.upload_file(tmp_file_path, bucket_name, upload_key)
        print('Upload!: ' + upload_key)

    except Exception as e:
        print(e)

    finally:
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)
            print('Removed!: ' + tmp_file_path)

    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!!!')
    # }