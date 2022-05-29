from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models

class BookListView(ListView):
	model = models.Book

class BookDetailView(DetailView):
	model = models.Book

class BookUpdateView(UpdateView):
	model = models.Book
	fields = "__all__"

class BookDeleteView(DeleteView):
	model = models.Book
	success_url = "/"

class BookCreateView(CreateView):
	model = models.Book
	fields = "__all__"
