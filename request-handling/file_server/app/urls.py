from django.urls import path, register_converter
from app.path_converter import DateConverter
from app.views import file_list, file_content


register_converter(DateConverter, 'yyyy-mm-dd')

urlpatterns = [
    path('', file_list, name='file_list'),
    path('<yyyy-mm-dd:date>/', file_list, name='file_list'),
    path('file/<str:name>', file_content, name='file_content'),
]
