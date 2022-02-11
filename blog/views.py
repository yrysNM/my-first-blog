from django.shortcuts import render, get_object_or_404

from django.utils import timezone

from .models import Post
""" Точка перед models означает текущую директорию или текущее приложение. 
	Поскольку views.py и models.py находятся в одной директории, мы можем использовать точку . и имя файла (без расширения .py). 
	Затем мы импортируем модель (Post).
"""


# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte = timezone.now()).order_by("published_date")
	return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
	post = get_object_or_404(Post, pk = pk)
	return render(request, 'blog/post_detail.html', {"post": post})
