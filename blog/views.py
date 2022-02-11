from django.shortcuts import render, get_object_or_404

from django.utils import timezone

from .models import Post
""" Точка перед models означает текущую директорию или текущее приложение. 
	Поскольку views.py и models.py находятся в одной директории, мы можем использовать точку . и имя файла (без расширения .py). 
	Затем мы импортируем модель (Post).
"""

from .forms import PostForm

from django.shortcuts import redirect
"""
	Добавь эту строку в начало файла.
	Теперь мы можем сделать переадресацию на страницу 
	post_detail для созданной записи:
"""

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte = timezone.now()).order_by("published_date")
	return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
	post = get_object_or_404(Post, pk = pk)
	#rev = pos.delete()
	#return redirect('post_detail', pk = post.pk)
	if(request.method == "POST"):
		post.delete()
		return redirect("post_list")

	return render(request, 'blog/post_detail.html', {"post": post})


def post_new(request):
	if(request.method == "POST"):
		form = PostForm(request.POST)

		if(form.is_valid()):
			post = form.save(commit =False)
			post.author = request.user
			post.published_date= timezone.now()
			post.save()
			return redirect("post_detail", pk = post.pk)
	else:
		form = PostForm()

	
	return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
	post = get_object_or_404(Post, pk = pk)

	if(request.method == "POST"):
		form = PostForm(request.POST, instance= post)

		if(form.is_valid()):
			post = form.save(commit = False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk = post.pk)

	else:
		form = PostForm(instance = post)

	return render(request, 'blog/post_edit.html', {'form': form})