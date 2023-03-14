from django.shortcuts import render,redirect
from .forms import AssignmentForm
from .models import Assignment
# Create your views here.
def index(request):
    if request.method == "POST":
        assignment = AssignmentForm(request.POST)
        if assignment.is_valid():
            assignment.save()
            return redirect('index')

    assignments = Assignment.objects.all()
    assignment_form = AssignmentForm()
    return render(request,'myapp/index.html',{'assignment_form':assignment_form,'assignments':assignments})






def delete(request,id):
    if request.method =='POST' and 'delete' in request.POST:
        assignment = Assignment.objects.get(id=id)
        assignment.delete()

    return redirect('index')
