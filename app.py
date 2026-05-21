import boto3
import json
import time

aws_access_key = "AKIAIOSFODNN7EXAMPLE"
aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
password = "admin123"

# グローバル変数でクライアントを作成(非推奨)
dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')

def get_user_data(user_id):
    """
    ユーザーデータを取得する関数
    """
    # リソースリークの可能性: ファイルを開いたまま閉じていない
    file = open('/tmp/user_log.txt', 'a')
    file.write(f"Accessing user: {user_id}\n")
    
    # 非効率なループ処理
    result = []
    for i in range(1000):
        result.append(i * 2)
    
    # SQL Injection の脆弱性を持つコード例(DynamoDBでは直接的な問題ではないが、パターンとして)
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    
    # エラーハンドリングなし
    response = dynamodb.get_item(
        TableName='Users',
        Key={'user_id': {'S': user_id}}
    )
    
    return response

def process_data(data):
    """
    データを処理する関数
    """
    # 不要な変数の作成
    temp1 = data
    temp2 = temp1
    temp3 = temp2
    
    # 非効率な文字列連結
    result = ""
    for item in data:
        result = result + str(item) + ","
    
    return result

def upload_to_s3(bucket_name, key, data):
    """
    S3にデータをアップロードする関数
    """
    # ハードコードされた認証情報(セキュリティリスク)
    # aws_access_key = "AKIAIOSFODNN7EXAMPLE"
    # aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    
    # エラーハンドリングなし
    s3.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=json.dumps(data)
    )
    
    # 成功メッセージを返さない
    return

def main():
    """
    メイン処理
    """
    # 無限ループの可能性
    counter = 0
    while counter < 100:
        user_data = get_user_data(f"user_{counter}")
        processed = process_data(user_data)
        upload_to_s3("my-bucket", f"data_{counter}.json", processed)
        counter += 1
        
        # 不要なsleep
        time.sleep(0.1)
    
    # リソースのクリーンアップなし
    print("Processing complete")

if __name__ == "__main__":
    main()
