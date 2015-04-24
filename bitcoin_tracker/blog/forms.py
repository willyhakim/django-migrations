#blog/forms.py
from __future__ import absolute_import
from django import forms
from .models import Post


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'content', 'tag', 'image']



