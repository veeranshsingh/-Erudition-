from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.apps import apps
Upload_file=apps.get_model('teacher', 'Upload_file')


Detail_student = apps.get_model('home', 'Detail')
Upload = apps.get_model('teacher','Upload_video')


# Create your views here.
def student(request):
    inputId = request.user
    detail = Detail_student.objects.get(username = inputId)
    print(detail)
    context = {'c': detail}
    return render(request, 'student/homepage.html',context)


def abc(request):
    return (request, 'student/abc.html')


def contact(request):
    return render(request, 'student/contact.html')


def grade1(request):
    detail = Upload.objects.filter(grade = '1')
    context = {'videos':detail}
    return render(request, 'student/grade1.html',context)


def grade2(request):
    detail = Upload.objects.filter(grade='2')
    context = {'videos': detail}

    return render(request, 'student/grade2.html',context)


def grade3(request):
    detail = Upload.objects.filter(grade='3')
    context = {'videos': detail}
    return render(request, 'student/grade3.html',context)


def grade4(request):
    detail = Upload.objects.filter(grade='4')
    context = {'videos': detail}
    return render(request, 'student/grade4.html',context)


def grade5(request):
    detail = Upload.objects.filter(grade='5')
    context = {'videos': detail}
    return render(request, 'student/grade5.html',context)


def grade1sm(request):
    videos = Upload_file.objects.filter(grade='1')
    context = {"videos": videos}

    return render(request, 'student/grade1sm.html',context)

def grade2sm(request):
    videos = Upload_file.objects.filter(grade='2')
    context = {"videos": videos}

    return render(request, 'student/grade2sm.html', context)


def grade3sm(request):
    videos = Upload_file.objects.filter(grade='3')
    context = {"videos": videos}

    return render(request, 'student/grade3sm.html', context)


def grade4sm(request):
    videos = Upload_file.objects.filter(grade='4')
    context = {"videos": videos}

    return render(request, 'student/grade4sm.html', context)


def grade5sm(request):
    videos = Upload_file.objects.filter(grade='5')
    context = {"videos": videos}

    return render(request, 'student/grade5sm.html',context)


def video1(request):
    detail = Upload.objects.filter(grade='1')
    print(detail)
    context = {'videos': detail}

    return render(request, 'student/video1.html',context)

def video2(request):
    detail = Upload.objects.filter(grade='2')
    print(detail)
    context = {'videos': detail}
    return render(request, 'student/video2.html',context)

def video3(request):
    detail = Upload.objects.filter(grade='3')
    print(detail)
    context = {'videos': detail}
    return render(request, 'student/video3.html',context)

def video4(request):
    detail = Upload.objects.filter(grade='4')
    print(detail)
    context = {'videos': detail}
    return render(request, 'student/video4.html',context)

def video5(request):
    detail = Upload.objects.filter(grade='5')
    print(detail)
    context = {'videos': detail}
    return render(request, 'student/video5.html',context)


def about(request):
    return render(request, 'student/about.html')


def logout_request(request):
    logout(request)
    messages.info(request, "chala ja bhosdhike")
    return redirect("home")

def showFile(request,pk):
    return (render,'student/show.html')