from django.shortcuts import render,redirect
import json
from datetime import datetime
from django.utils import timezone
# from weather.models import Todo

# from weather.form import TodoForm
from django.contrib.auth.models import User, auth

from django.contrib import messages

from django.contrib.auth import logout

import json

import urllib.request

from weatherdetector import settings                     #from base dir settings

from django.core.mail import send_mail                   #for mail services

from django.contrib.sites.shortcuts import get_current_site

from django.utils.http import urlsafe_base64_encode

from django.template.loader import render_to_string

from django.utils.encoding import force_bytes

from weather.tokens import generate_token

from django.core.mail import EmailMessage,send_mail 

from weather.form import Contactform
import requests
from django.shortcuts import render
import geocoder

API_KEY = '4e12830424ab4806a3445d9bab7c9101'
GEOLOCATION_API_URL = f'https://ipgeolocation.abstractapi.com/v1/?api_key={API_KEY}'

def get_ip_geolocation_data(ip_address):
    response = requests.get(GEOLOCATION_API_URL)
    return response.json()



def index(request):
    current_datetime = datetime.now()
    current_datetime_with_tz = timezone.now()

    context = {
        'current_datetime': current_datetime,
        'current_datetime_with_tz': current_datetime_with_tz,
    }
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:

       ip = x_forwarded_for.split(',')[0]

    else:

       ip = request.META.get('REMOTE_ADDR')
       
    geolocation_data = get_ip_geolocation_data(ip)
    country = geolocation_data.get('country')
    region = geolocation_data.get('region')
    lon=geolocation_data.get('longitude')
    lat=geolocation_data.get('latitude')
    # Fetch weather data using OpenWeatherMap API
    api_key = 'b79fe2651c79bf394d7bf6e84807b3b4'
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lon}&lon={lat}&appid={api_key}&units=metric'
    response = requests.get(weather_url)
    weather_data = response.json()

    # Extract relevant weather information from the API response
    temperature = weather_data['main']['temp']
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']

    # Pass the location and weather data to the template
    context = {
    'temperature': temperature,
    'pressure': pressure,
    'humidity': humidity,
    'description': description,
    'country': country,
    'region': region,
    'lon': lon,
    'lat': lat,
    'current_datetime': current_datetime,
    'current_datetime_with_tz': current_datetime_with_tz
    }

    return render(request, 'Templates/homepage.html', context)
    return render(request, 'Templates/homepage.html')
    




# Create your views here.
def landingPage(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=b79fe2651c79bf394d7bf6e84807b3b4').read() #get the city data using the api
        json_data = json.loads(res) #Loads the json data from the api
        data = {                                               #convert the json data into dictionary
            "country_code":str(json_data['sys']['country']),  
            "coordinate":str(json_data['coord']['lon']) + " " + str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp'])+'C',
            "pressure":str(json_data['main']['pressure']) + 'Pa',
            "humidity":str(json_data['main']['humidity']) + 'atm', 
                 
        }
          
    else:
        data = {}
        return render(request, 'index.html', data)  
        
    return render(request, 'index.html', data)    


def liveLocation(request):
    return redirect("https://www.meteoblue.com/en/weather/maps/index#coords=9.44/5.3307/-1.9138&map=windAnimation~rainbow~auto~10%20m%20above%20gnd~none")
    


def Sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
           if  User.objects.filter(username=username).exists():
               messages.info(request, 'Username Already Used')
               return redirect('Sign_up')
           elif User.objects.filter(email=email).exists():
               messages.info(request, 'Email Already Used')
               return redirect('Sign_up')
      
           else:
               user = User.objects.create_user(username=username,email = email,password=password)
               user.is_active = True
               user.save();
               return redirect('Log_in')
               #Email welcome
               
               subject = 'Welcome to Flint Weather App '
               
               message = 'Hello' + user.username + '!!' + 'Welcome to the Flint Weather App\n Thank you foe visting our website\n we have sent you a confirmation email\n Kindly confirm to activate your account\n Thank You\n The Flint weather Team'
               
               from_email = settings.EMAIL_HOST_USER
               
               to_list = [user.email]
               
               send_mail(subject,message,from_email,to_list,fail_silently = True )
               
               
               #Email Address Confirmation Email
               
            #    current_site = get_current_site
               
            #    message2 = render(request, 'email_confirmation.html',{
            #        'name':user.username,
            #        'domain':current_site,
            #        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #        'token':generate_token.make_token(user)
            #    })
            #    email = EmailMessage(
            #        subject,
            #        message2,
            #        settings.EMAIL_HOST_USER,
            #        [user.email],
            #    )
            #    email.fail_silently = True
               
            #    send_mail(subject,from_email,message, recipient_list)
               
               
            #    messages.info(request, 'Account Successfully created,\n We have sent a confirmation to your mail to activate your account')
               
            #    return redirect('Log_in')
           
                
        else:
            messages.info(request, 'Passwords Dont Match')
            return redirect('Sign_up')           
               
    return render(request, 'Sign_up.html')



def Log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'No such user')
            return redirect('Log_in')
    else:
        return render(request, 'Log_in.html')
        
        return render(request, 'Log_in.html')
        
def Log_out(request):
    auth.logout(request)
    return redirect('/')



# def todo(request):
#     item_list = Todo.objects.order_by('-date')
#     if request.method == POST:
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('todo')
#     form = TodoForm()    
            
        
#     page = {
#         'forms':form,
#         'list':item_list,
#         'Activity Name':'TODO-LIST'    
#     }
    
#     return render(request, 'todo.html', page)










# def todo(request):
#     if request.method == 'POST':
#         # todo_list = request.POST['text']
#         # todo_list = Todo.objects.create(todo_list = todo_list)
#         # todo_list.save()
#         # messages.info(request, 'Activity Created Successfully')
#         # return render(request, 'todo.html', {'todo_list':todo_list})
#         todo_name = Todo
#         todo_name = Todo.objects.all()  
#         messages.info(request, 'Activity Created Successfully')
#         return render(request, 'todo.html', {'Todo':todo_name})
#     else:
#         return render(request, 'todo.html')
#         return render(request, 'todo.html')

def Contact(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['body']
            messages.info(request, 'Message sent!')
            print(name , email, body)
        else:
            messages.info(request, 'Invalid Form')    
    else:
        return render(request, 'forms.html')        
    form = Contactform()
    return render(request, 'forms.html', {'form':form})
        