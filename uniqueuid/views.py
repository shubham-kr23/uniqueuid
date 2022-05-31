from multiprocessing import context
from sqlite3 import connect
from django.shortcuts import render
import  requests
from subprocess import run,PIPE
from django.http import HttpResponse

from ctypes import sizeof
from json import JSONDecoder
from nturl2path import url2pathname
from turtle import clear
from typing import Any
from urllib import request
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def availableInstagram(id):
    url="https://www.instagram.com/"+id+"/?__a=1"  # Soup.getText()

    # request.urlopen(url)
    req=requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    recived_data=soup.getText()

    # print(url)
    # print(len(recived_data))
    # print(recived_data)

    if(len(recived_data)==2):
        return 1 #available
    else:
        return 0 #Not available

def availableFacebook(id):
    url = "https://www.facebook.com/"+id  #using soup.title

    req=requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    recived_data=soup.title.get_text()


    # print(len(recived_data))

    # print(recived_data)

    if(recived_data.find("Facebook")!=-1):
        return 1 #Not available
    else:
        return 0 #available

def availableSnapchat(id):
    # id="shubham_kr2309"
    url = "https://www.snapchat.com/add/"+id #using soup.title  

    print(url)

    req=requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    recived_data=soup.title.get_text()


    print(len(recived_data))
    print(recived_data)
    # print(soup.getText())
    # if(len(recived_data)==0):
    if(recived_data.find("Sorry,This content was not found")!=-1):
        return 0    #Not available
    else:
        return 1    #available

def availableCodeforces(id):
    url = "https://codeforces.com/profile/"+id #using soup.title

    req=requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    recived_data=soup.title.get_text()

    # print(len(recived_data))

    # print(recived_data)

    if(recived_data.find("-")!=-1):
        return 0 #Not available
    else:
        return 1 #available

def availableCodeChef(id):
    url = "https://www.codechef.com/users/"+id

    req=requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    recived_data=soup.title.get_text()

    # print(len(recived_data))

    # print(recived_data)

    if(recived_data.find("| CodeChef User Profile for")!=-1):
        return 0 #Not available
    else:
        return 1 #available

    # Error page  -> Not Allowed
    # | CodeChef User Profile for (x y z) | -> alredy exist
    # Competitive Programming | Participate & Learn | CodeChef-> ID not found :)

def availableAtCoder(id):
    url = "https://atcoder.jp/users/"+id

    req=requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    recived_data=soup.title.get_text()

    # print(len(recived_data))

    # print(recived_data)

    if(recived_data.find(id+" - AtCoder")!=-1):
        return 0 #Not available
    else:
        return 1 #available # 404 Not Found - AtCoder


def defaultHomePage(request):
    context={
        "UID" : '',
        "flagInstaGram" : 0,
        "flagFacebook" : 0,
        "flagTwitter" : 0,
        "flagSnapchat" : 0,
        "flagCodeforces" : 0,
        "flagCodechef" : 0,
        "flagAtCoder" :0,
    }
    return render(request,'home.html',context)

def output(request):
    # get from user input
    # id  = request.POST.get('userID')  # Second Value is default Value

    id="shubham.kr23"
    if request.method == 'POST':
        id = request.POST.get('userID')
    # id = request.POST.get('userID')

    

    context={
        "UID" : '',
        "flagInstaGram" : 0,
        "flagFacebook" : 0,
        "flagTwitter" : 0,
        "flagSnapchat" : 0,
        "flagCodeforces" : 0,
        "flagCodechef" : 0,
        "flagAtCoder" : 0,
    }


    # id=str(id)
    if id is None :
        # print("No input")
        return render(request,'home.html',context)

    # print(id)

    
    context["UID"]=id

    # if checked then change  
    if availableInstagram(id) :
        context["flagInstaGram"]=1
        # print("Instagram : Available")
    else:
        context["flagInstaGram"]=-1
        # print("Instagram : Not Available")

    if availableFacebook(id) :
        context["flagFacebook"]=1
        # print("Facebook : Available")
    else:
        context["flagFacebook"]=-1
        # print("Facebook : Not Available")

    if availableSnapchat(id) :
        context["flagSnapchat"]=1
        # print("Snapchat : Available")
    else:
        context["flagSnapchat"]=-1
        # print("Snapchat : Not Available")

    if availableCodeforces(id) :
        context["flagCodeforces"]=1
        # print("Codeforces : Available")
    else:
        context["flagCodeforces"]=-1
        # print("Codeforces : Not Available")

    if availableCodeChef(id):
        context["flagCodechef"]=1
        # print("CodeChef : Available")
    else:
        context["flagCodechef"]=-1
        # print("CodeChef : Not Available")

    if availableAtCoder(id):
        context["flagAtCoder"]=1
        # print("AtCoder : Available")
    else:
        context["flagAtCoder"]=-1
        # print("AtCoder : Not Available")

    return  render(request,"home.html",context)