from django.shortcuts import render
from random import choice
def home(request):
   return render(request, 'generator/home.html')

def about(request):
   return render(request, 'generator/about.html')

def password(request):
   characters = list('abcdefghijklmnopqrstuvwxyz')
   generate_password = ''
   legth= int(request.GET.get('length'))
   
   if request.GET.get('uppercase'):
      characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

   if request.GET.get('special'):
      characters.extend(list('!"·$%&/()=?¿¡-_+*~:;,\{\}[]'))

   if request.GET.get('numbers'):
      characters.extend(list('0123456789'))

   for char in range(legth): 
      generate_password += choice(characters) 
   return render(request, 'generator/password.html', {'password': generate_password}) 
