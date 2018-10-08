#-*- coding: utf-8 -*-
from django import forms

class UploadForm(forms.Form):
   # name = forms.CharField(max_length = 100)
   picture = forms.ImageField()
