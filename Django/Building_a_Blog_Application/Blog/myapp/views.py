from django.shortcuts import render,get_list_or_404
from.models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def post_list(request):
    posts=Post.published_at.all()
    return render(request,'myapp/post/list.html',{'posts':posts})


def post_detail(request,day,month,year,post):
    post=get_list_or_404(Post,slug=post,status="published",published__year=year,published__day=day,published__month=month)
    return render(request,'myapp/post/detail.html',{"posts":post})