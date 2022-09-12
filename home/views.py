from django.shortcuts import redirect, render
from .models import Students
from .forms import StudentForm
from django.contrib import messages

def form(request):
 
    if request.method == 'POST':
        std1 = StudentForm(request.POST)
        if std1.is_valid():
            if Students.objects.filter(student_id=request.POST['student_id']).exists():
                  messages.error(request,'studentid already exits')
                  return redirect("/")
            else:
                new_student=Students(student_id=request.POST['student_id'],name=request.POST['name'],email=request.POST['email'],phone=request.POST['phone'])
                new_student.save()
                student=Students.objects.all()
                return render(request,'show.html',{'form':student})
    else:
        std1=StudentForm()
    return render(request,'form.html',{'form':std1})
       

def show(request):
    student=Students.objects.all()
    return render(request,'show.html',{'form':student})
       

def delete(request):
    edit1=request.GET['delete']
    Students.objects.filter(student_id=edit1).delete()
    student=Students.objects.all()
    return render(request,'show.html',{'form':student})
       

def edit(request):
    edit1=request.GET['delete']
    if request.method == 'POST':
        if Students.objects.filter(student_id=edit1).exists():
          if request.POST['student_id']:
            Students.objects.filter(student_id=edit1).update(student_id=request.POST['student_id'])
          if request.POST['name']:
            Students.objects.filter(student_id=edit1).update(name=request.POST['name'])
          if request.POST['email']:
            Students.objects.filter(student_id=edit1).update(email=request.POST['email'])
          if request.POST['phone']:
            Students.objects.filter(student_id=edit1).update(phone=request.POST['phone'])
          student=Students.objects.all()
          return render(request,'show.html',{'form':student})
    edit=Students.objects.filter(student_id=edit1)
    return render(request,'edit.html',{'forms':edit})
# Create your views here.
