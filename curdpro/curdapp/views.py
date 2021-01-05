from django.shortcuts import render,redirect
from .models import StudentData
# Create your views here.

def home(request):
    students = StudentData.objects.all()
    return render(request,'student_home.html',{'students':students})
def add_student(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        section_name = request.POST.get('section')
        class_name = request.POST.get('cls')
        school_name = request.POST.get('school')
        telugu_marks = request.POST.get('telugu')
        hindi_marks = request.POST.get('hindi')
        english_marks = request.POST.get('english')
        maths_marks = request.POST.get('maths')
        science_marks = request.POST.get('science')
        social_marks = request.POST.get('social')
        studentdata = StudentData(
            first_name = first_name,
            last_name = last_name,
            section_name = section_name,
            class_name = class_name,
            school_name = school_name,
            telugu_marks = telugu_marks,
            hindi_marks = hindi_marks,
            english_marks = english_marks,
            maths_marks = maths_marks,
            science_marks = science_marks,
            social_marks = social_marks
        )
        studentdata.save()
        message = "Data Added Successfully"
        return render(request,'add_student.html',{'message':message})
    else:

        return render(request, 'add_student.html')


def updatedata(request,myid):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        section = request.POST['section']
        cls = request.POST['cls']
        mydata = StudentData.objects.get(id=myid)
        mydata.first_name = fname
        mydata.last_name = lname
        mydata.section_name = section
        mydata.class_name = cls
        mydata.save()
        students = StudentData.objects.all()
        return render(request,'student_home.html',{'students':students})
    else:
        mydata = StudentData.objects.get(id=myid)
        return render(request,'update.html',{'mydata':mydata})
def deletedata(request,myid2):
    if request.method == 'GET':
        ddata = StudentData.objects.get(id=myid2)
        ddata.delete()
        return redirect('/')
    else:
        return redirect('/')