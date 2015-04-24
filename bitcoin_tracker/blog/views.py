# blog/views.py
from __future__ import absolute_import
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
#Local imports
from .models import Post
from .forms import PostForm

def index(request):
	"Main page"
	latest_posts = Post.objects.all().order_by('-views')
	t = loader.get_template('blog/index.html')
	c = Context({'latest_posts': latest_posts})
	return HttpResponse(t.render(c))

def post(request, post_id):
	"Single post page"
	single_post = get_object_or_404(Post, pk=post_id)
	t = loader.get_template('blog/post.html')
	c = Context({'single_post': single_post})
	single_post.views += 1
	single_post.save()
	return HttpResponse(t.render(c))

def add_post(request):
	"Adding a new blog post"
	context = RequestContext(request)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=True)
			return redirect(index)
		else:
			print form.errors
	else:
		form = PostForm()
	context_dict = {'form':form}	
	return render_to_response('blog/add_post.html', context_dict, context)