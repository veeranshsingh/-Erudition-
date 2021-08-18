from django.shortcuts import render
from .models import Upload_video,videoComment,Upload_file
from .forms import Video_form,Upload_form
from django.apps import apps
Teacher = apps.get_model('teacher', 'Teacher_Detail')
from .templatetags import extras


# Create your views here.
def t_homepage(request):

    print(request.user)
    inputid = request.user
    try:
        detail = Teacher.objects.get(username = inputid)
    except Teacher.DoesNotExist:
        detail = None
    print(detail)
    #print(d)
    context = {'d':detail}



    return render(request, 'teacher/homepagetr.html', context)

def t_about(request):
    return render(request,'teacher/abouttr.html')

def t_contact(request):
    return render(request,'teacher/contacttr.html')

def t_grade1sm(request):
    return render(request,'teacher/grade1smtr.html')

def t_grade1(request):


    return render(request,'teacher/grade1tr.html')

def t_grade2(request):
    return render(request,'teacher/grade2tr.html')

def t_grade3(request):
    return render(request,'teacher/grade3tr.html')

def t_grade4(request):
    return render(request,'teacher/grade4tr.html')

def t_grade5(request):
    return render(request,'teacher/grade5tr.html')

def t_video(request):

    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postsno')
        try:
            post =  Upload_video.objects.get(id=postSno)
        except Upload_video.DoesNotExist:
            post = None
            if post is not None:
                comment = videoComment(comment=comment,user=user,post=post)
                comment.save()

    form = Video_form
    form = Video_form(data=request.POST or None)

    if request.method == 'POST':
        form = Video_form(data=request.POST or None, files=request.FILES)
        if form.is_valid():
            form.save()

    if request.method == 'POST':
        d = request.POST.get('abcd')
        try:
            video = Upload_video.objects.get(id=d)
        except Upload_video.DoesNotExist:
            video = None
        if video is not None:
            video.delete()


    videos = Upload_video.objects.filter(detail__username=request.user)
    context = {"forms":form,"videos":videos}


    return render(request, 'teacher/video.html', context)

def t_video1(request):
    videos = Upload_video.objects.filter(grade = '1')
    context = {"videos": videos}
    return render(request,'teacher/videotr1.html',context)

def t_video2(request):
    videos = Upload_video.objects.filter(grade='2')
    context = {"videos": videos}
    return render(request,'teacher/videotr2.html',context)

def t_video3(request):
    videos = Upload_video.objects.filter(grade='3')
    context = {"videos": videos}
    return render(request,'teacher/videotr3.html',context)

def t_video4(request):
    videos = Upload_video.objects.filter(grade='4')
    context = {"videos": videos}
    return render(request,'teacher/videotr4.html',context)

def t_video5(request):
    videos = Upload_video.objects.filter(grade='5')
    context = {"videos": videos}
    return render(request,'teacher/videotr5.html',context)

def handleComment(request,pk):
    news = pk
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postsno')
        parentsno = request.POST.get('parentsno')
        print(parentsno)
        post =  Upload_video.objects.get(id=pk)
        if parentsno == '':
            comment = videoComment(comment=comment,user=user,post=post)
            comment.save()
        else:
            parent = videoComment.objects.get(sno=parentsno)
            comment = videoComment(comment=comment, user=user, post=post,parent=parent)
            comment.save()
    video = Upload_video.objects.get(id=pk)
    comment = videoComment.objects.filter(post = video,parent = None)
    replies = videoComment.objects.filter(post = video).exclude(parent=None)
    replyDict= {}
    for reply in replies:
        if reply.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    print(replyDict)
    return render(request, 'teacher/comment.html', {'comments': comment, 'id':news, 'replyDict': replyDict})

def handleFile(request):
    form1 = Upload_form
    form1 = Upload_form(data=request.POST or None)
    if request.method == 'POST':
        form1 = Upload_form(data=request.POST or None, files=request.FILES)
        print(form1)
        if form1.is_valid():
            form1.save()
    videos = Upload_file.objects.filter(detail__username=request.user)

    if request.method == 'POST':
        d = request.POST.get('abcd')

        try:
            video = Upload_video.objects.get(id=d)
            print(video)
        except Upload_video.DoesNotExist:
            video = None
        if video is not None:
            video.delete()

    context1 = {'forms': form1,"videos":videos}
    return render(request, 'teacher/file.html', context1)