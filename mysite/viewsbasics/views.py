from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from random import choice
from django.views import View
from django.shortcuts import render

def funktionally(request):
    response = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Funktionally Page</title>
    <link rel="icon" href="https://ict.gctaa.net/resources/GCTAAfavicon.png">
    <style>
    body {
        margin: 4vw;
    }
    main {
        padding: 4vw;
        border: 1px dotted #777;
    }
    h1, footer {
        text-align: center;
    }
    footer {
        margin-top: 1vw;
    }
    a, a:visited {
        text-decoration: none;
        font-weight: bold;
        color: #C92; 
    }
    </style>
    </head>
    <body>
    <h1>Funktionally Page</h1>
    <p>
    This is the <i>Funktionally Page</i>.  It was returned as a literal string
    from a simple Django functional view that did nothing else but return it.
    </p>

    <footer>
    <a href="../viewsbasics/">Return to Viewbasics index page</a>
    </footer>
    </body>
    """
    return HttpResponse(response)


def danger(request):
    response = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Danger Page!</title>
    <link rel="icon" href="https://ict.gctaa.net/resources/GCTAAfavicon.png">
    <style>
    body {
        margin: 4vw;
    }
    main {
        padding: 4vw;
        border: 1px dotted #777;
    }
    h1, footer {
        text-align: center;
    }
    span {
        font-size: x-large;
        font-weight: bold;
        color: red;
    }
    footer {
        margin-top: 1vw;
    }
    a, a:visited {
        text-decoration: none;
        font-weight: bold;
        color: #C92; 
    }
    </style>
    </head>
    <body>
    <h1>Danger Page!</h1>
    <p>Your thing was: <span>"""+request.GET['thing']+"""</span></p>
    <p>You can learn more about <b>URL encoding</b> by clicking
    <a href="https://en.wikipedia.org/wiki/Percent-encoding">here</a>.</p>
    <footer>
    <a href="../viewsbasics/">Return to Viewbasics index page</a>
    </footer>
    </body>
    """
    return HttpResponse(response)


def safer(request):
    response = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Safer Page</title>
    <link rel="icon" href="https://ict.gctaa.net/resources/GCTAAfavicon.png">
    <style>
    body {
        margin: 4vw;
    }
    main {
        padding: 4vw;
        border: 1px dotted #777;
    }
    h1, footer {
        text-align: center;
    }
    span {
        font-size: x-large;
        font-weight: bold;
        color: red;
    }
    footer {
        margin-top: 1vw;
    }
    a, a:visited {
        text-decoration: none;
        font-weight: bold;
        color: #C92; 
    }
    </style>
    </head>
    <body>
    <h1>Safer Page</h1>
    <p>Your thing was: <span>"""+escape(request.GET['thing'])+"""</span></p>
    <footer>
    <a href="../viewsbasics/">Return to Viewbasics index page</a>
    </footer>
    </body>
    """
    return HttpResponse(response)


def prettyurldata(request, thing):
    response = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Pretty URL Data Page</title>
    <link rel="icon" href="https://ict.gctaa.net/resources/GCTAAfavicon.png">
    <style>
    body {
        margin: 4vw;
    }
    main {
        padding: 4vw;
        border: 1px dotted #777;
    }
    h1, footer {
        text-align: center;
    }
    span {
        font-size: x-large;
        font-weight: bold;
        color: red;
    }
    footer {
        margin-top: 1vw;
    }
    a, a:visited {
        text-decoration: none;
        font-weight: bold;
        color: #C92; 
    }
    </style>
    </head>
    <body>
    <h1>Pretty URL Data Page</h1>
    <p>Your thing was: <span>"""+escape(thing)+"""</span></p>
    <footer>
    <a href="../">Return to Viewbasics index page</a>
    </footer>
    </body>
    """
    return HttpResponse(response)


def bounce(request):
    places = [
        'https://www.python.org/',
        'https://ict.gctaa.net/',
        'https://www.dj4e.com/',
        'https://www.djangoproject.com/',
    ]
    return HttpResponseRedirect(choice(places))

class Name(View):
    def get(self,request,name=""):
        #name = request.GET.get('name')
        x = {'name':name}
        return render(request, 'viewsbasics/name.html',x)

class Num(View):
    def get(self,request,num=""):
        #num = request.GEt.get('num')
        x = {'num':num}
        return render(request, 'viewsbasics/num.html',x)

class Word(View):
    def get(self,request,word=""):
        #word = request.GET.get('word')
        x = {'word':word}
        return render(request, 'viewsbasics/word.html',x)

class BMI(View):
    def get(self, request, weight, height):
        #height = request.GET.get('height')
        #weight = request.GET.get('weight')
        weight = int(weight)
        height = int(height)
        bmi = round(703*(weight / (height**2)))  # Calculate BMI

        x = {'height':height, 'weight':weight, 'bmi':bmi}
        return render(request, 'viewsbasics/bmi.html',x)

class Calc(View):
    def get(self, request, length, height):
        #length = request.GET.get('length')
        #height = request.GET.get('height')
        length = int(length)
        height = int(height)
        area = length * height
        perimeter = 2 * (length + height)

        x = {'length':length, 'height':height, 'area':area, 'perimeter':perimeter}
        return render(request, 'viewsbasics/calc.html',x)

