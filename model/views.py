from django.shortcuts import render
from .models import user

# Create your views here.
def home(request):
    return render(request, "index1.html")

def signinup(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "index1.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def course(request):
    return render(request, "course.html")


def confirmsignup(request):
    msg = ""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        
        try: 
            user.objects.get(Email=email)
            msg = "Email is already taken. Use another or Login using same email"
            
        except Exception as e:
            if str(e) == "user matching query does not exist.":
                usr = user(Name=name, Email=email,Password=password) # create new model instance
                usr.save() #seve to db
                msg = "Registration completed. Please signin to continue."
            else:
                msg = str(e)
            

    return render(request, "index.html", {"msg":msg})

        
    

def confirmsignin(request):
    msg = ''
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password'] 

        try: 
            usr = user.objects.get(Email=email)
            if usr.Email==email and usr.Password==password:
                return render(request, "index1.html")
            else:
                return render(request, 'index.html', {'msg':"Email and password don't match"})
            
        except Exception as e:
            if str(e) == "user matching query does not exist.":
                msg = "This email is not registered. Please Signup first."
            else:
                msg = str(e)
    return render(request, 'index.html',{'msg':msg})
            
