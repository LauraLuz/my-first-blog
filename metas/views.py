from django.shortcuts import render

def post_list(request):
    return render(request, 'metas/post_list.html', {})