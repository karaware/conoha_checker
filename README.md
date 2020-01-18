# 概要
ConoHaのメンテナンス情報を取得してchatworkに投稿します。  

# 環境
Python  
## パッケージ
- requests  
- json  
- pprint  
- re   
- datetime  

# 利用準備
- tokens.py内の以下の各変数にConoHaの情報を記載します。  
    user : APIユーザ  
    passwd : APIパスワード  
    tid : テナントID  
    endpoint : トークン発行用エンドポイント  

- get_conoha.py内の以下の各変数にConoHaの情報を記載します。
    url : お知らせ情報取得用エンドポイント  

- chats.pyの以下の各変数にchatworkの情報を記載します。
    apikey : APIキー  
    endpoint : chatwork用エンドポイント  
    roomid : 投稿する対象のchatworkルームID  
    chattag : chatworkに投稿する際のタグ  

# 利用方法
main.pyを実行します。  
```
# python main.py
```

