from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect

from django.urls import reverse

# Create your views here.

posts = [
     {
        "id": 1,
        "title": "Post 1 title",
        "content": "This is the content of post 1."
    },
     {
        "id": 2,
        "title": "Post 2 title",
        "content": "This is the content of post 2."
    },
     {
        "id": 3,
        "title": "Post 3 title",
        "content": "This is the content of post 3."
    }
]

# posts=[]

def helloWorld(request):
    
    html =""
    for post in posts:

        html += f'''

            <div>
                <a href="/post/{post['id']}/">
                <h1> {post['id']} - {post['title']}</h1></a>
                <p> {post['content']} </p>
            </div>

        '''

    return render(request,'posts/home.html',{"posts":posts,'username':'taranjot'})


def post(request, id):
    valid_post=False
    for post in posts:
        if post['id'] == id:
            post_dict=post
            valid_post=True
            print(post_dict)
            break
    if valid_post:
        return render(request,'posts/post.html',{'post_dict':post_dict})
    else:
        return HttpResponseNotFound("Post not Found")
    
def google(request,id):
    url = reverse('post',args=[id])
    print(url)
    return HttpResponseRedirect(url)