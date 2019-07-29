from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def main(request):
  try:
    post = Post.objects.all()
  except:
    print("Error")
    return redirect("main")

  context = {
    'post_list': post
  }

  return render(request, "main.html", context)


def create_post(request):
  if request.method == "POST":
    nickname = request.POST.get("nickname")
    title = request.POST.get("title")
    content = request.POST.get("content")
    password = request.POST.get("password")

    try:
      post = Post(nickname=nickname, title=title, content=content, password=password)
      post.save()
    except:
      print("Error")
      return redirect("create_post")
    
    return redirect("main")
  else:
    return render(request, "create_post.html")


def view_post(request, post_id):
  try:
    post = Post.objects.get(id=post_id)
  except:
    print("No Post")
    return redirect("main")
  
  context = { 'post': post }

  return render(request, "view_post.html", context)


def delete_post(request, post_id):
  if request.method == "POST":
    password = request.POST.get("password")

    try:
      post = Post.objects.get(id=post_id)
      if post.password == password:
        post.delete()
      raise Error
    except:
      return redirect("view_post", post_id)

  return redirect("main")