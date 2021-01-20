from django.urls import path, include
from .views import ToDoList, ToDoDetail, ToDoCreate, ToDoDelete

urlpatterns = [
    # name引数で逆引きに対応
    path('list/', ToDoList.as_view(), name='list'),
    # DetailViewを用いる際は、urlにプライマリーキーを表記する必要がある django側にどの個別データを持ってくるか教えてあげるため
    path('detail/<int:pk>', ToDoDetail.as_view(), name='detail'),
    path('create/', ToDoCreate.as_view(), name='create'),
    # どのデータを消すのか指定する必要あるためpkを記載
    path('delete/<int:pk>', ToDoDelete.as_view(), name='delete'),

]
