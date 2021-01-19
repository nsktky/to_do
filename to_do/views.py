from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import ToDoModel
from django.urls import reverse_lazy

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

# データを作成するのに適したクラス
# どのモデルのフィールドに即してデータを作成するかdjangoに教えてあげる必要があるためmodelを指定
class ToDoCreate(CreateView):
    template_name = 'create.html'
    model = ToDoModel
    # fieldsはmodelのどのフィールドを入力させるかを記載
    fields = ('title', 'memo', 'priority', 'duedate')
    # listと言う名前に対応したurlを逆引きする。reverseはurls→viewsの逆順
    # lazyは入力されたデータに基づきオブジェクトが作成された後reverseするという意味
    success_url = reverse_lazy('list')