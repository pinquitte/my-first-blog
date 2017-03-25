from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):     
    posts = Post.objects.order_by('yayinlanma_tarihi')
    return render(request, 'blogging/post_list.html', {'posts':posts})

# Create your views here.