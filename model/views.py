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
                response = render(request, "prediction/predictionpage.html", {"msg":msg})
                response.set_cookie('Signin', email ,max_age=1*24*60*60)
                return response
            else:
                return render(request, 'index.html', {'msg':"Email and password don't match"})
            
        except Exception as e:
            if str(e) == "user matching query does not exist.":
                msg = "This email is not registered. Please Signup first."
            else:
                msg = str(e)
    return render(request, 'index.html',{'msg':msg})

def predictionpage(request):
    try:
        value = request.COOKIES['Signin']
        return render(request, 'prediction/predictionpage.html')
    except KeyError:
        return render(request, 'index.html', {'msg':"Please Signin to check the predictions."})


def predict(request):
    import joblib,os
    import numpy as np
    from django.conf import settings
    from sklearn.preprocessing import MinMaxScaler
    import warnings
    warnings.simplefilter("ignore")
    
    if request.method == "POST":
        Age = int(request.POST["Age"])
        Gender = int(request.POST["Gender"])
        Stream = int(request.POST["Stream"])
        NumOfInternships = int(request.POST["Internships"])
        CGPA = int(request.POST["CGPA"])
        Backlogs = int(request.POST["Backlogs"])

        with open(os.path.join(settings.BASE_DIR, 'model/model_campus_placement.pkl'),'rb') as f:
            model = joblib.load(f)
            pred = model.predict([[Age,Gender,Stream,NumOfInternships,CGPA,Backlogs]])[0]

        if pred:
            print("prediction is ", pred)
            # db = personality(name=name,gender=gender,age=age,openness=openness,neuroticism=neuroticism,conscientiousness=conscientiousness,agreeableness=agreeableness,extraversion=extraversion,result=pred[0])
            # db.save()
            return render(request, 'prediction/result.html', {'prediction':pred})


        return render(request, 'prediction/result.html')
    else:
        return render(request, 'prediction/result.html', {'prediction':0})

def report(request):
    data = user.objects.all
    return render(request, 'prediction/database.html', {'data':data})

def front(request):
    return render(request, 'prediction/front.html')