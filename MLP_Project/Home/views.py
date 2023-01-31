from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
from WebsiteTextParser import TextParser
from SummarizingModel import summarizer
import json
from django.http import JsonResponse
from PIL import Image
import pytesseract
import requests
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout

# Create your views here.

def index(request):
    context={
        'variable':"Gurdaan Walia "
    }
    api_key = 'd099fc71486e4affa401d6a290b63631'
    url = 'https://newsapi.org/v2/top-headlines'
    params = {'country': 'us', 'apiKey': api_key}
    response = requests.get(url, params=params)
    data = response.json()
    return render(request, 'index.html', {'data': data})
    #return render(request,'index.html',context)

def url(request):
        
    context={'parsedText':'','summarizedText':''}  
    if request.method == 'POST':
        submit_values = request.POST.getlist('submit_button')
        if 'Submit 1' in submit_values:
            # Do something when 'Submit 1' is clicked
            urlData=request.POST.get('urlName')
            #messages.success(request, 'Extracting Text')
            soupObject=TextParser.parser(urlData)
            context['parsedText']=soupObject.get_text()
            dummyText=context['parsedText']
        else:
            data = json.loads(request.body)
            p_text = data['p_text']
            # Do something with the data
            summarizedData=summarizer.summarize(p_text)
            data = {'summarizedData': summarizedData}
            json_data = json.dumps(data)
            return JsonResponse(json_data, safe=False)
    return render(request,'url.html',context)


def text(request):
    return render(request,'text.html')

def fileUpload(request):
    return render(request,'fileUpload.html')

def contactUs(request):
    if request.method=="POST":
        # Request.POST gives the dictionary
        email=request.POST.get('email')
        text=request.POST.get('text')
        date=datetime.now()
        contact=Contact(email=email,text=text,date=date)
        contact.save()
        messages.success(request, 'Profile details updated.')
    
    return render(request,'contactUS.html')

def textFromImage(request):
    if request.method == 'POST':
        image = request.FILES['image']
        if request.method == 'POST':
            image = Image.open(image)
            text = pytesseract.image_to_string(image)
        print("AtBAckEnd")
        return JsonResponse({'data': 'text'})
    return render(request,'textFromImage.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    print(f"Username:{username}")
    print(f"Password:{password}")
    user=authenticate(username=username,password=password)
    print(user)
    if user is not None:
        return render(request,'index.html',{'user':user})
    return render(request,'login.html')

def loginlogoutbutton(request):
    if request.method == 'POST':
        # Handle button click
        if 'loginbutton' in request.POST:
            # Do something when button1 is clicked
            print("Login")
            return render(request,'login.html')
        else:
            # Do something when button2 is clicked
            logout(request)
            return render(request,'index.html')

def registeration(request):
    if request.method=='POST':
        print("Inside Registeration")
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print("username :",username)
        print("Password :",password)
        print("Email :",email)
        # Create a new user
        user = User.objects.create_user(username=username,
                                email=email,
                                password=password)
        return render(request,'login.html')
        # Save the user to the database
        user.save()
    return render(request,'registeration.html')

def summaryhistory(request):
    return render(request,'summaryhistory.html')


    
