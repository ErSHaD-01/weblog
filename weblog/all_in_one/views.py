from django.shortcuts import render
from .models import post , comment , like , category , save , user
# Create your views here.

def show_post(request):
    posts = post.objects.filter(is_published = True)
    return render(request , 'home.html' , {'post' : posts})


def post_detail(request , post_id):
    detail = post.objects.get(post_id = post_id)
    comments = comment.objects.filter(post_id = post_id)
    likes = like.objects.filter(post_id = post_id).count()
    return render(request , 'home.html' , {'detail' : detail , 'comments' : comments , 'likes' : likes})


def categorys(request):  
    categoryy = category.objects.all() 
    return render(request, 'home2.html', {'category': categoryy}) 
 
def post_list(request, cat_id):  
    categoryss = category.objects.get(id = cat_id) 
    posts = post.objects.filter(post_category = categoryss) 
    return render(request, 'home3.html', {'posts' : posts, 'category' : categoryss})


def show_user(request):
    users = user.objects.all()
    return render(request , 'saves.html' , {'users' : users})

def show_save_posts(request , user_id):
    save_users = save.objects.get(user_id = user_id)
    save_posts = save.objects.filter()
    return render(request , 'saves.html' , {'save_users' : save_users})