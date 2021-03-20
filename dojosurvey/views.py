from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'school_survey.html')
    print(request.POST)

def results(request):
    context = {
        "whole_name": request.POST['whole_name'],
        "location": request.POST['location'],
        "favorite_language": request.POST['language'],
        "comments": request.POST['comments']
    }
    if request.method == "POST":  
        whole_name = request.POST["whole_name"]
        location = request.POST["location"]
        favorite_language = request.POST['language']
        comments = request.POST['comments']
    return render(request, 'results.html', context)