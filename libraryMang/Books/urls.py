from . import views
from django.urls import path,include
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'', views.BooksViewset)

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.BooksListAPIView.as_view(), name='books'),
    # path('<int:pk>', views.BooksRetrieveAPIView.as_view(), name='Retrieve book'),
    path('add', views.BookCreateAPIView.as_view(), name='add book'),
    path('<int:pk>', views.BookRUDAPIView.as_view(), name='RUD book'),
    # path('', views.BookRUDAPIView.as_view(), name='RUD book'),
]