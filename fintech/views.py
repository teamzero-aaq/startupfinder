from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from fintech.models import user_profile11,register_user11,register_investor11,add_idea11,watchlist1
from requests import get
from bs4 import BeautifulSoup
import re
types=""
emaill=""
# Create your views here.
def gethome(request):
    global types
    global eamill

    if(request.method=='POST'):
            uname=request.POST["uname"]
            pas=request.POST["password"]
            #user = user_profile1.objects.all()
            user = register_user11.objects.all()
            invest = register_investor11.objects.all()
            for u in user:
                if u.email == uname and u.password ==pas:
                    if u.typeof == "1":
                        types="1"
                        emaill=u.email
                    return HttpResponseRedirect("home")
                else:
                    for v in invest:
                        if v.email == uname and v.password ==pas:
                            if v.typeof == "2":
                                types="2"
                                emaill=u.email
                            return HttpResponseRedirect("home") 
    
    return render(request,"login.html")
def addidea(request):
    if(request.method=='post'):
        title=request.POST("title")
        domain=request.POST("domain")

        number=request.POST("ncollab")
        link=request.POST("link")
        about=request.POST("about")
        u=user_profile11(title=title,domain=domain,ncollab=number,link=link,about=about)
        u.save()
        return HttpResponseRedirect("home")
    else:
        return render(request,"add_ideas.html")    
        
def r_investor(request):
    if(request.method=='POST'):
        cname=request.POST["cname"]
        email=request.POST["email"]
        gst=request.POST["gst"]
        phone=request.POST["phone"]
        password =request.POST["pass"]
        r = register_investor11(company_name=cname,email=email,gst_no=gst,contact=phone,password=password,typeof ="2")
        r.save()
        return HttpResponseRedirect("index")        
    else:
        return render(request,"investor_signup.html") 

def r_user(request):
    if(request.method=='POST'):
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        password =request.POST["pass"]
        r = register_user11(name=name,email=email,contact=phone,password=password,typeof ="1")
        r.save()
        return HttpResponseRedirect("index")        
    else:
        return render(request,"individual_signup.html")
     

def  getidea(request):
    result=[]
    ad=add_idea1.objects.all()
    for ideas in ad:
        if(ideas.email==email):
            result.append(ideas)
    return render('myproject.html',{'data':result})        
            
def getprofile(request):
    if(request.method=='POST'):
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        qualification=request.POT["edu"]
        address =request.POST["address"]
        city =request.POST["city"]
        country =request.POST["country"]
        postal_code =request.POST["code"]
        about = request.POST['about_me']
        r = user_profile11(fname=fname,lname=lname,email=email,qualification=qualification,address=address,city=city,country=country,postal_code=postal_code,about_me=about)
        r.save()
        return HttpResponseRedirect("home")
    else:
        return render(request,'profile.html')
                  
     
def home(request):
    

    # def clean_v(s):
    #     s = re.sub('\s+', '', s)
    #     return s

    url = "https://techcrunch.com/startups/"
    response = get(url)
    print(response)
    page_soup = BeautifulSoup(response.content, 'html.parser')
    table = page_soup.findAll('a', {'class' : 'post-block__title__link'})
    final_data = []
    for data in table:
        news_data = {}
        news_data['links'] = data.get('href')
        news_data['title'] = data.text
        final_data.append(news_data)
        print(final_data)
    l=add_idea11.objects.all()
    if types=="1":
        return render(request,"index1.html",{'data':l,'news':final_data})
    else:  
        return render(request,"index2.html",{'data':l,'news':final_data})

def watchlist(request):
    idea = add_idea11.objects.all()
    titles=watchlist1.objects.all()
    t1=[]
    for t in titles:
        print(t.email)
        if(t.email=="harsh.gokhru@somaiya.edu"):
            t1.append(t)
            
    print(t1)        
    a=[]
    
    for ideas in idea:
        for titl in t1:
            if(ideas.title==titl.title):
                 a.append(ideas)
    print(a)             
    return render(request,'watchlist.html',{'data':a})        
            
    
    
def tolist(request):
    if(request.method=='POST'):
        val=request.POST['gettitle']
        w=watchlist1(email="harsh.gokhru@somaiya.edu",title=val)
        
        w.save()
        return HttpResponseRedirect('home')
    else:
        return HttpResponseRedirect('home')
    
def details(request):
    user = user_profile11.objects.all()
    ideas = add_idea11.objects.all()
    print(ideas)
    print(user)
    for i in ideas:
        for u in user:
            if u.email == i.email:
                glink = i.link
                string ="/graphs/contributors"
                url1 = glink
                url2 = url1 + string
                response1 = get(url1)
                print(response1)
                response2 = get(url2)
                print(response2)
                page_soup1 = BeautifulSoup(response1.content, 'html.parser')
                page_soup2 = BeautifulSoup(response2.content, 'html.parser')
                date = page_soup2.findAll('div', {'class' : 'Subhead'})
                data = page_soup1.find('span', {'class' : 'num text-emphasized'}).text
                #print(date)
                star = page_soup2.findAll('a', {'class' : 'social-count js-social-count'})
                print(star)
                print(data)
    return render(request,"details.html");
        
    