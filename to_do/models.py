# データベースとviewsの橋渡しを行うのがmodels.py
from django.db import models

# priorityのchoicesに入れる選択肢をタプルで入力。各タプルの左側がプログラム内の変数。右側が選択肢
CHOICE = (('danger', 'high'), ('warning', 'normal'), ('primary', 'low'))

# models.Modelモジュールを継承し、作りたいdbのカラムを入力
# 新たなmodelclassを作成した場合はターミナルでmakemigrationsとmigrateの必要あり
# makemigrationsでmodelの作成・変更履歴を残す migrateでdb上にテーブルを作成できる
class ToDoModel(models.Model):
    # todoのタイトル　CharFieldは小・大サイズの文字列フィールド
    # max_lengthを引数に渡す必要あり
    title = models.CharField(max_length=100)
    # todoの内容　TextFieldは多量の文字列フィールド
    memo = models.TextField()
    # priorityはtodoの優先度を表現.choicesに格納したタプルが選択肢となる
    priority = models.CharField(
        max_length=50,
        choices = CHOICE)
    # duedateはtodoの締め切りを表現
    duedate = models.DateField()
    # オブジェクト作成時に実行される関数　作成したオブジェクトのtitleを返すことで管理画面を見やすくしている
    def __str__(self):
        return self.title
    