from django.contrib import admin
from django.urls import path
from bookapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BookListView.as_view()),
    path('book/<int:pk>', views.BookDetailView.as_view()),
    path('book/<int:pk>/update', views.BookUpdateView.as_view()),
    path('new/', views.BookCreateView.as_view()),
    path('book/<int:pk>/delete', views.BookDeleteView.as_view()),
]
