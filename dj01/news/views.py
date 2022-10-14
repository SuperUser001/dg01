from django.shortcuts import render
from django.http import HttpResponse
from .models import News

# Create your views here.

def index(request):
   # print(request ,'1111')
   news = News.objects.all()
   context = {'news':news, 'title': 'Список новостей'}
   return render(request, template_name='news/index.html', context=context)

def test(request):
   news = News.objects.all()
   res = '<h1>Lists news: </h1>'
   for item in news:
      res += f'<div>\n<p>{item.title}<p>\n<p>{item.content}<p>\n</div>\n'
   return HttpResponse(res)
