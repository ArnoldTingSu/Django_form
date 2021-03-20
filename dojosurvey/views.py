from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print("arrived via redirect!!")
    return render(request,'school_survey.html')

def process(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        return redirect('/results')

def results(request):
    return render(request, 'results.html')