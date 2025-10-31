from django.shortcuts import render,redirect
from myapp.models import News,Study
from mainapp.models import Student
from .models import Feedback
# Create your views here.
def parent(request):
    return render(request,'stuparent.html')

def stunews(request):
    if request.method == "POST":
        title = request.POST['title']
        desc=request.POST['desc']
        news=News.objects.create(title=title,desc=desc)
        return redirect('myapp:stunews')
    news=News.objects.all()
    return render(request,'stunews.html',{"news":news})

def stuhome(request):
    try:
        if request.session['student'] == None:
            return redirect('mainapp:login')
        else:
            stu = Student.objects.get(id = request.session['student'])
            st = Study.objects.filter(course=stu.course,branch=stu.branch,session=stu.session)
            stl=len(st)
            fe = Feedback.objects.filter(sid = stu.id,feedtype="Feedback")
            fel = len(fe)
            co = Feedback.objects.filter(sid=stu.id,feedtype="Complain")
            col=len(co)
            su = Feedback.objects.filter(sid=stu.id,feedtype="Suggestion")
            sul = len(su)
            n = News.objects.all()
            nl = len(n)
            return render(request,'stuhome.html',locals())
    except:
        return redirect('mainapp:login')

def stustudy(request):
    st = Study.objects.all()
    return render(request,'stustudy.html',locals())

def stufeedback(request):
    if request.method=="POST":
        feedtype = request.POST['feedtype']
        title = request.POST['title']
        desc = request.POST['desc']
        sid = request.session.get('student')
        # if not sid:   # matlab login nahi hai
        #     return redirect('mainapp:login')
        Feedback.objects.create(feedtype=feedtype,title=title,desc=desc,sid=sid)
        return redirect('studentapp:stufeedback')
    return render(request,'stufeedback.html')

def viewfeedback(request):
    stu = Feedback.objects.all()
    return render(request,'viewfeedback.html',locals())