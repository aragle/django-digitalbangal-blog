# Description: This file contains the views for the post app.

from django.shortcuts import render


# Create your views here.
def post(request):
    post = {'title': 'Post', 'content': 'This is the post page.', 'date_posted': 'August 27, 2018', 'author': 'John Doe', 'tags': ['city', 'bug', 'solve', 'law', 'code', 'python', 'django', 'html', 'css', 'javascript', 'java', 'c++', 'c', 'c#', 'php', 'sql', 'database', 'data', 'science', 'machine', 'learning', 'artificial', 'intelligence'], 'comments': [
        {'author': 'Jane Doe', 'content': 'This is a comment.', 'date_posted': 'August 27, 2018'}, {'author': 'Jane Doe', 'content': 'This is a comment.', 'date_posted': 'August 27, 2018'}, {'author': 'Jane Doe', 'content': 'This is a comment.', 'date_posted': 'August 27, 2018'}], 'likes': 0, 'time_to_read': '5'}
    return render(request, 'post/post.html', post)
