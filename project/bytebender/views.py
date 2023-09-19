from django.shortcuts import render ,redirect
from bytebender.models import registration,feedback

# Create your views here.
def index(request):
    return render(request, 'index.html')
def contactus(request):
    return render(request, 'contactus.html')

def register(request):
     if request.method == "POST":
         firstname = request.POST.get('fname')
         lastname = request.POST.get('lname')
         email = request.POST.get('email')
         password = request.POST.get('password')
         gender = request.POST.get('gender')
         sports = request.POST.get('sports')
         data = registration(firstname = firstname , lastname = lastname , password = password, email = email , gender = gender , sport =sports)
         data.save()
     return render (request, 'index.html')

def login(request):
     error_msg = None
     if request.method == "POST":
         emails = request.POST.get('email')
         password = request.POST.get('password')
         try:
             logindata = registration.objects.get(email=emails , password = password)
             if logindata:
                 request.session['email'] = emails
                 request.session['sports'] = logindata.sport
                 request.session['username'] = logindata.firstname 
                 request.session['lastname'] = logindata.lastname
                 request.session['la'] = logindata.lastname
                 return redirect('profile')    
         except:
             error_msg = "please check email or password"
             return render(request, 'invalid.html', {'error_msg': error_msg})
def logout(request):
     request.session.clear()
     return redirect('index')


def calc(request):
    if request.method == 'POST':
        weight = request.POST['weight']
        height = request.POST['height']
        age = request.POST['age']
        gender = request.POST['gender']
        print("weight: ",weight)
        print("height: ",height)
        print("age: ",age)
        print("gender: ",gender)
        if gender == 'male':
            result = 66.47 + (13.75 * int(weight)) + (5.003 * int(height)) - (6.755 * int(age))
            print(result,"######################")
            return render(request,'calculator.html',{'result':result})
        if gender == 'female':
            result = 655.1 + (9.563 * int(weight)) + (1.850 * int(height)) - (4.676 * int(age))
            print(result,"######################") 
            return render(request,'calculator.html',{'result':result})
    c = request.session['email']
    username = registration.objects.filter(email= c)
 
    return render(request, 'calculator.html',{'username':username})

def meal(request):
    c = request.session['email']
    username = registration.objects.filter(email= c)
    return render(request,'meal.html',{'username':username})
def injury(request):
    c = request.session['email']
    username = registration.objects.filter(email= c)
    return render(request,'injury.html',{'username':username})

def profile(request):
    c = request.session['email']
    username = registration.objects.filter(email= c)
    return render(request , 'profile.html',{'username':username})

def feed(request):
    c = request.session['username']
    if request.method =="POST":
        feed = request.POST.get('feedback')
        user_feed = feedback(userfeedback = feed,username = c)
        user_feed.save()
    a = feedback.objects.all()
    data= feedback.objects.filter(username = c)
    context = {
        'a':a
    }
    c = request.session['email']
    username = registration.objects.filter(email= c)
    # return render(request , 'feedback.html',{'username':username})
    data = {
        'username':username
    }
    return render(request ,'feedback.html',{'a':a , 'username':username , 'data':data})
def feedback1(request):
    a = feedback.objects.all()
    context = {
        'a':a
    }
    return render(request,'feedback.html',context)

def cricket(request):
    return render(request,'cricket.html')
def hockey(request):
    return render(request,'hockey.html')
def football(request):
    return render(request,'football.html')
def basketball(request):
    return render(request,'basketball.html')
def invalid(request):
    return render(request,'invalid.html')