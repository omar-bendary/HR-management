from django.urls import path
from .views import RecordList, RecordDetail

urlpatterns = [
    path('<int:pk>/', RecordDetail.as_view()),
    path('', RecordList.as_view()),
]
