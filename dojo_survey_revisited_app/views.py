from django.shortcuts import render, redirect
def index(request):
    return render(request,'index.html')

def process(request):
    if request.method=="POST":
        for key, value in request.POST.items():
            print('Key: %s' % (key) ) 
            # print(f'Key: {key}') in Python >= 3.7
            print('Value %s' % (value) )
            # print(f'Value: {value}') in Python >= 3.7 
        request.session['name'] = request.POST.get('name')
        request.session['location'] = request.POST.get('location')
        request.session['language'] = request.POST.get('language')
        request.session['gender'] = request.POST.get('gender')
        request.session['comment'] = request.POST.get('comment')
        request.session['email'] = request.POST.get('email')
    return redirect("/result")

def result(request):
    
    return render(request,'result.html')