from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from customer.chat import get_response,bot_name
from datetime import date, timedelta
import speech_recognition as sr
from django.db.models import Q
from django.core.mail import send_mail
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from Text_to_SQL_App import models as CMODEL
from Text_to_SQL_App import forms as CFORM
from googletrans import Translator
from translate import Translator as trans
from django.views.generic import TemplateView
from django.contrib.auth.models import User
import datetime
import time
import winsound



class eng(TemplateView):
    Template_view="customer/eng.html"
    def get(self,request):
        context = {
            "user": "",
            "text": "Hi, how can I assist you?"
        }
        return render(request, self.Template_view, context)
        #return render(request,self.Template_view)
    def post(self,request):
        if request.method == 'POST':
            
            user = request.POST.get('input',False)
            bot_response = get_response(user)
            if bot_response is None:
                bot_response = "I'm sorry, I don't understand your question. Please contact this number: 9828798798"
            context={"user":user,"bot":bot_response} 	
        return render(request,self.Template_view,context)
    







@login_required(login_url='customerlogin')
def customer_dashboard_view(request):
    

    dict={
        'customer':models.Customer.objects.get(user_id=request.user.id),
       
    }
    if request.method == 'POST':
        user = request.POST.get('input',False)
        context1={"user":user,"bot":get_response(user)}
			
		
    return render(request,'customer/customer_dashboard.html',context=dict)
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#Develop by Haseeb Asghar
#https://www.linkedin.com/in/infohaseeb/
#https://github.com/infohaseeb

def LoginUser(request):
    if request.user.username=="":
        return render(request,"customer/login.html")
    else:
        return HttpResponseRedirect("/homepage")

@login_required(login_url="/loginuser/")
def HomePage(request):
    return render(request, "medical/home.html")

def clicklogin(request):
    if request.method!="POST":
        return HttpResponse("<h1> Methoid not allowed<h1>")
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        
        user=authenticate(username=username,password=password)
        if user!=None:
            login(request,user)
            return HttpResponseRedirect('/homepage')
        else:
            messages.error(request, "Invalid Login")
            return HttpResponseRedirect('/loginuser')

def LogoutUser(request):
    logout(request)
    request.user=None
    return HttpResponseRedirect("/loginuser")       




def RegisterUser(request):
    if request.user==None or request.user =="" or request.user.username=="":
        return render(request,"customer/register.html")
    else:
        return HttpResponseRedirect("/homepage")        


def ClickRegister(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username, email, password)
            messages.success(request, "User Created Successfully")
            return HttpResponseRedirect('/register_user')
        else:
            messages.error(request, "Email or Username Already Exist")
            return HttpResponseRedirect('/register_user')
''' 
class home(TemplateView):
	Template_view="index.html"

	def get(self,request):
		return render(request,self.Template_view)

	def post(self,request):
		if request.method == 'POST':
			user = request.POST.get('input',False)
			context={"user":user,"bot":get_response(user)}
			
		return render(request,self.Template_view,context)
      
class hindi(TemplateView):
	Template_view="customer/hindi.html"

	def get(self,request):
		return render(request,self.Template_view)

	def post(self,request):
		if request.method == 'POST':
                        r = sr.Recognizer()
                        print("Please talk")
                        with sr.Microphone() as source:
                        # read the audio data from the default microphone
                                audio_data = r.record(source, duration=10)
                                print("Recognizing...")
                                # convert speech to text
                                text = r.recognize_google(audio_data)
                                print("Recognised Speech:" + text)
                                a=text
                                translator = Translator()
                                source_lan = "hi"
                                translated_to= "en"
                                translated_text = translator.translate(text, src=source_lan, dest = translated_to)
                                res=translated_text.text
                                print(translated_text.text)
                                translator5 = trans(from_lang="en", to_lang="hi")
                                data3 = translator5.translate(text)
                                print(data3)
                                result=get_response(res)
                                translator6 = trans(from_lang="en", to_lang="hi")
                                r = translator5.translate(result)
                                print(r)
                                context={"user":data3,"bot":r}
                        return render(request,self.Template_view,context)
class marathi(TemplateView):
	Template_view="customer/marathi.html"

	def get(self,request):
		return render(request,self.Template_view)

	def post(self,request):
		if request.method == 'POST':
			user = request.POST.get('input',False)
			context={"user":user,"bot":get_response(user)}
			
		return render(request,self.Template_view,context)
        '''
'''
class engm(TemplateView):
    Template_view="customer/engm.html"
    def get(self,request):
        return render(request,self.Template_view)
    def post(self,request):
        if request.method == 'POST':
                        r = sr.Recognizer()
                        print("Please talk")
                        with sr.Microphone() as source:
                        # read the audio data from the default microphone
                                audio_data = r.record(source, duration=10)
                                print("Recognizing...")
                                # convert speech to text
                                text = r.recognize_google(audio_data)
                                print("Recognised Speech:" + text)
                                a=text
                                translator = Translator()
                                source_lan = "mr"
                                translated_to= "hi"
                                translated_text = translator.translate(text, src=source_lan, dest = translated_to)
                                res=translated_text.text
                                print(translated_text.text)
                                translator1 = Translator()
                                source_lan1 = "hi"
                                translated_to1= "en"
                                translated_text1 = translator1.translate(res, src=source_lan1, dest = translated_to1)
                        
                                print(translated_text1.text)
                                a_res=translated_text1.text
                                #translator5 = trans(from_lang="en", to_lang="hi")
                                #data3 = translator5.translate(text)
                                #print(data3)
                                result=get_response(a_res)
                                print(result)
                                translator2 = Translator()
                                source_lan2 = "en"
                                translated_to2= "mr"
                                translated_text2 = translator2.translate(result, src=source_lan2, dest = translated_to2)
                        
                                print(translated_text2.text)
                                final=translated_text2.text
                                
                                #print(r)
                                context={"user":res,"bot":final}
                        
                        return render(request,self.Template_view,context)


'''