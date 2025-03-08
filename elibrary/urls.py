from django.urls import path
from . import views

urlpatterns = [
    path('ebooks/', views.EBookListView.as_view(), name='ebook_list'),
    path('ebooks/<int:pk>/', views.EBookDetailView.as_view(), name='ebook_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ebooks/<int:pk>/borrow/', views.borrow_ebook, name='borrow_ebook'),
    path('ebooks/<int:pk>/download/', views.download_ebook, name='download_ebook'),
    path('ebooks/<int:pk>/return/', views.return_ebook, name='return_ebook'),
    path('ebooks/<int:pk>/rate/', views.rate_ebook, name='rate_ebook'),
]