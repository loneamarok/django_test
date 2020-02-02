from django.http import HttpResponse
from django.shortcuts import render
import operator 
def hello(request):
   return render(request, 'home.html', {"hi": 1})

def count(request):
   fulltext = request.GET["fulltext"]
   wordlist = fulltext.split()

   word_dict = {}
   for word in wordlist:
      if(word in word_dict):
         word_dict[word] += 1
      else:
         word_dict[word] = 1

   word_list = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

   return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'word_list':word_list})

def about(request):
      return render(request, 'about.html')