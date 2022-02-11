from django.shortcuts import redirect, render,HttpResponse
from bloging.models import Post,BlogComment
from django.contrib import messages
from bloging.templatetags import extras
# Create your views here.
def bloghome(request):
    allposts=Post.objects.all()
    # print(allposts)
    context={'allposts':allposts}
    return render(request,'bloging/blogHome.html',context)


def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    # Here We will take comments coresponding to post
    comments=BlogComment.objects.filter(post=post,parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)
    # print("This is reply",replies)
    # print("This is Comments",comments)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            # Here we are adding serial number corresponding to reply
            replyDict[reply.parent.sno]=[reply]
        else:
            # Here we are appending reply serial number correspondin
            # to his reply
            replyDict[reply.parent.sno].append(reply)
    # print("This is reply dictionary",replyDict)
        



    
    context={'post':post,'comments':comments,'user':request.user,'replyDict':replyDict}
    return render(request,'bloging/blogPost.html',context)
    
# This method used for post a Comments
def postComment(request):
    if request.method=='POST':
        comment=request.POST.get("comment")
        user=request.user
        postSno=request.POST.get("postSno")
        post=Post.objects.get(sno=postSno)
        parentSno=request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,"Your Comment has been posted successfully")
            
        else:
            parent=BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment=comment,user=user,post=post,parent=parent)
            messages.success(request,"Your Reply has been posted successfully")
            comment.save()
    return redirect(f'/blog/{post.slug}')






