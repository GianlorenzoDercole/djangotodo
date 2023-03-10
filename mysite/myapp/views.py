from django.shortcuts import render

from .forms import AssignmentForm
# Create your views here.

def index(request):
    assignment_form = AssignmentForm()
    return render(request,'myapp/index.html',{'assignment_form':assignment_form})
