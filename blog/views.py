from django.shortcuts import render, redirect

from .forms import OrderForm  #CommentForm
from blog.forms import OrderForm  #CommentForm
from blog.models import Post, Order, Product  #Comment

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts}
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
                    '-created_on'
                    )
    context = {"category": category, "posts": posts}
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = OrderForm()
    if request.method == "POST":
       form = OrderForm(request.POST)
       if form.is_valid():
           order = Order(
                   author = form.cleaned_data["author"],
                   quantity = form.cleaned_data["quantity"],
                   email = form.cleaned_data["email"],
                   phone = form.cleaned_data["phone"],
                   message_store = form.cleaned_data["message_store"],
                   post=post,
                   )
           order.save()
           return redirect("/blog/")
    orders = Order.objects.filter(post=post)
    context = {"post":post, "orders":orders, "form":form}
    return render(request, "blog_detail.html", context)

#def order(request)

#Create your views here.

#Archives
#def blog_detail(request, pk):
#    post = Post.objects.get(pk=pk)

    #form = CommentForm()
    #if request.method == "POST":
    #   form = CommentForm(request.POST)
    #   if form.is_valid():
    #       comment = Comment(
    #               author=form.cleaned_data["author"],
    #               body=form.cleaned_data["body"],
    #               post=post,
    #               )
    #       comment.save()
    #       return redirect("/blog/")
       #edit url to redirect
    #comments = Comment.objects.filter(post=post)
    #context = {"post":post, "comments":comments, "form":form,}
    #return render(request, "blog_detail.html", context)

#def blog_detail(request, pk):
#    post = Post.objects.get(pk=pk)

    #form = CommentForm()
    #if request.method == "POST":
    #   form = CommentForm(request.POST)
    #   if form.is_valid():
    #       comment = Comment(
    #               author=form.cleaned_data["author"],
    #               body=form.cleaned_data["body"],
    #               post=post,
    #               )
    #       comment.save()
    #       return redirect("/blog/")
       #edit url to redirect
    #comments = Comment.objects.filter(post=post)
    #context = {"post":post, "comments":comments, "form":form,}
    #return render(request, "blog_detail.html", context)

