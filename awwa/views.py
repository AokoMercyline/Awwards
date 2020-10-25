from django.shortcuts import render
    
def index(request):
    context = {
        'posts': posts #list of dict details for all post
    }

    return render(request, 'awwa/index.html', context, {'title': title})

