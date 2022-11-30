from django.shortcuts import render

# Create your views here.
  
def atoms(request):
  return render(request, 'subatomics/atoms.html')

def electrons(request):
  return render(request, 'subatomics/electrons.html')

def protons(request):
  return render('subatomics')