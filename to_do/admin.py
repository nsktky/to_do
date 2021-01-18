# 管理画面（admin）で何をどのように表示するかを記載するファイル
from django.contrib import admin
from .models import ToDoModel

admin.site.register(ToDoModel)