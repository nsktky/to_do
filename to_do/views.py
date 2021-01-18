from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ToDoModel

# データの一覧をリストとして表示するクラス
# ListViewを継承しclass based viewで作成
class ToDoList(ListView):
    template_name = 'list.html'
    # models.py内のどのmodelを使うかを指定
    model = ToDoModel

# 個別のデータの詳細を表示するクラス
class ToDoDetail(DetailView):
    template_name = 'detail.html'
    model = ToDoModel