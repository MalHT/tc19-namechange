from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render_to_response
from django.shortcuts import render
from .models import Organisation 
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import os

#from project.models import Organisation, Task

def home(request):
    content = {
        'title' : 'Name Change Tracker',
        'author' : 'We',
        'date' : '14th June 2019',
        #'body' : my_custom_sql(),
    }
    return render_to_response('index.html', content)
  
  

@csrf_protect
def update_db(request):
  wiki_name = request.POST['name']
  wiki_body = request.POST['body']
  print('update_db')
  if request.method == 'POST':
    if request.POST.get('name') and request.POST.get('content'):
      wiki_page = WikiPage.objects.create(name=wiki_name, body=wiki_body)
     # with connection.cursor() as cursor:
        #cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
      #cursor.execute("INSERT OR REPLACE INTO Organisation(name, body) VALUES('TestOrg','This is a test org') ")
      return render(request, 'profile.html')
      #  cursor.execute("SELECT * FROM Organisation")
       #row = cursor.fetchone()
    #return row
    
    

def profile(request):
  print('Hello World 2 ')
  content = {
    'update' : 'Place Holder',
    'retrieve' : 'Place Holder 2',
  }
  return render(request, 'profile.html', content)

def login(request):
  return render_to_response('login.html')

@csrf_exempt
def validate_login(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)
  if user is not None:
      login(request, user)
      return render(request, 'index.html')
  else:
     return render(request, 'error.html')
