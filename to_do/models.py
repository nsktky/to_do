# データベースとviewsの橋渡しを行うのがmodels.py
from django.db import models

# models.Modelモジュールを継承し、作りたいdbのカラムを入力
# 新たなmodelclassを作成した場合はターミナルでmakemigrationsとmigrateの必要あり
# makemigrationsでmodelの作成・変更履歴を残す migrateでdb上にテーブルを作成できる
class ToDoModel(models.Model):
    # todoのタイトル　CharFieldは小・大サイズの文字列フィールド
    # max_lengthを引数に渡す必要あり
    title = models.CharField(max_length=100)
    # todoの内容　TextFieldは多量の文字列フィールド
    memo = models.TextField()
    
    # オブジェクト作成時に実行される関数　作成したオブジェクトのtitleを返すことで管理画面を見やすくしている
    def __str__(self):
        return self.title
    