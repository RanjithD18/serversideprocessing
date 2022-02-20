# Design a Website for Server Side Processing

## AIM:
To design a website to perform mathematical calculations in server side.

## DESIGN STEPS:

### Step 1:
Desing your website for calculation using wireframe work.

### Step 2:
Then to execute the wireframe work desing use html,css

### Step 3:
Use views.py to execute the coding in serverside.

### Step 4:
Mention the path of the website in urls.py.

### Step 5:
Publish the website in the given URL.

## PROGRAM :
### Home.html
~~~
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Page Title</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
<style>
    h1{
        text-align: center;
        color: blueviolet;
    }
    form{
        text-align: center;
    }
    body{
        background-color: blanchedalmond;
    }
    h4{
        text-align: center;
    }
</style>
</head>
<body>
    <h1>Calculator</h1>
    <form method="POST">
        {% csrf_token %}
        A= <input type="text" name="a" value="{{ a }}"><br>
        B= <input type="text" name="b" value="{{ b }}"><br>
        <input type="submit" value="ADD"><br><br>
        C= <input type="text" name="c" value="{{ c }}">
    </form>
    <h4>Developed by:Ranjith D</h4>
</body>
</html>
~~~
### views.py
~~~
from django.shortcuts import render

def myserverfunction(request):
    context = {}
    if request.method == "GET":
        context["a"] = "0"
        context["b"] = "0"
        context["c"] = "0"
    if request.method == "POST":        
        a = int(request.POST.get("a"))
        b = int(request.POST.get("b"))
        c = a+b
        context["a"] = a
        context["b"] = b
        context["c"] = c

    return render(request, 'myapp/home.html', context)
~~~
### urls.py
~~~
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage/',views.myserverfunction,name="mypage")
]
~~~

## OUTPUT:

![output](https://github.com/RanjithD18/serversideprocessing/blob/main/Screenshot%20(95).png)


## Result:
A website to perform mathematical calculations in server side is created.
