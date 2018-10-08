from django.shortcuts import render
from AIApp.forms import UploadForm
from AIApp.models import UploadImg
from FakeNotesDetect.model import *

# Create your views here.

def hello(request):
   return render(request, "hello.html", {})


def SaveProfile(request):
   saved = False
   
   if request.method == "POST":
      #Get the posted form
      UForm = UploadForm(request.POST, request.FILES)
      
      if UForm.is_valid():
         uploaded = UploadImg()
         # uploaded.name = UForm.cleaned_data["name"]
         uploaded.picture = UForm.cleaned_data["picture"]
         uploaded.save()
         saved = True

      result = predict(uploaded.picture)
      print("predicted")
   '''else:
      UForm = UploadForm()'''
		
   return render(request, 'saved.html', {"result" : result}, locals())

