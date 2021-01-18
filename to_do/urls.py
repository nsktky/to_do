from django.urls import path, include
from .views import ToDoList, ToDoDetail

urlpatterns = [
    path('list/', ToDoList.as_view()),
    # DetailViewを用いる際は、urlにプライマリーキーを表記する必要がある
    # django側にどの個別データを持ってくるか教えてあげるため
    path('detail/<int:pk>', ToDoDetail.as_view()),

]
