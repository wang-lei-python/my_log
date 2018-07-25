from django.shortcuts import render,HttpResponse
from django.views.generic import View
from .models import Article
from django.http import Http404

# Create your views here.

# def test(request):
#     return HttpResponse('just a test')

class TestView(View):
    def get(self,request):
        post=Article.objects.all()
        content=post[0].content
        pub_date=post[0].pub_date

        return HttpResponse(content,pub_date)


class HomeView(View):
    def get(self,request):
        post_list=Article.objects.all()
        return render(request,'home.html',{'post_list':post_list})

def Detail(request,id):
    try:
        post=Article.objects.get(id =str(id))
    except Article.DoesNotExist:
        raise http404
    return render(request,'post.html',{'post':post})




        # return HttpResponse ('just a test')


