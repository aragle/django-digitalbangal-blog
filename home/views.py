from django.shortcuts import render

# Create your views here.


def home(request):
    posts = {'post': {'id': 1,'title': 'Post is a good things', 'content': 'This is the post page.', 'date_posted': 'August 27, 2018', 'author': 'John Doe', 'tags': ['বিজ্ঞান', 'প্রযুক্তি', 'খবর', 'আইন', 'শিক্ষা', 'খেলাধুলা', 'স্বাস্থ্য', 'চিকিৎসা'], 'comments': [
        {'author': 'Jane Doe', 'content': 'This is a comment.', 'date_posted': 'August 27, 2018'}, {'author': 'Jane Doe', 'content': 'This is a comment.', 'date_posted': 'August 27, 2018'}, {'author': 'Jane Doe', 'content': 'This is a comment.', 'date_posted': 'August 27, 2018'}], 'likes': 0, 'time_to_read': '5'}}

    context = {'data': posts}
    return render(request, 'home/home.html', context)


