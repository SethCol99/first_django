from django.shortcuts import render

def home(request):
  return render(request, 'atomic_struct/landing.html')