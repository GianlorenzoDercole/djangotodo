from django.shortcuts import render

from .forms import AssignmentForm
from .models import Assignment
# Create your views here.

def index(request):
    if request.method == "POST":
        assignment = AssignmentForm(request.POST)
        if assignment.is_valid():
            assignment.save()

    assignments = Assignment.objects.all()
    assignment_form = AssignmentForm()
    return render(request,'myapp/index.html',{'assignment_form':assignment_form,'assignments':assignments})
