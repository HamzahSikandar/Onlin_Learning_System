from django.shortcuts import render,redirect
from tutorials.models import Course,Topics
# Create your views here.
def tutorial (request):
    course=Course.objects.all()
    # print(course)
    context={'course':course}
    return render (request,'tutorials/about.html',context)


def title(request,sno):
    course=Course.objects.filter(sno=sno).first()
    topics=Topics.objects.filter(course=course)
    # print("Content=",topics,'\n',"Course=",course)
    context={'topics':topics,'course':course}
    return render(request,'tutorials/content.html',context)



def Contentpage(request,slug):
    topic=Topics.objects.filter(slug=slug).first()
    context={'topic':topic}
    # print(topic)
    return render(request,'tutorials/page.html',context)