# Ex.05 Design a Website for Server Side Processing
## Date:3.10.25

## AIM:
 To design a website to calculate the Body Mass Index (BMI) in the server side. 


## FORMULA:
BMI = W/H<sup>2</sup>
<br> BMI --> Body Mass Index
<br> W --> Weight
<br> H --> Height
## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<html>
<head>
<title>Body Mass Index</title>
<h1 style="color:black"> GEETHA SHRI.G (25018001)</h1>
<style>
body
{
    background-color:mediumvioletred;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    font-size: x-large;
    font-weight: 100;
    display:flexbox;
    
}
.edge {
    width:1000px;
margin-left:auto;
margin-right:auto;
padding-top:140px;
padding-left:440px;
}
.box {
display:block;
border: solid 10px cyan;
width:600px;
height:400px;
font-size: 30px; 
background-color:lawngreen;
}
.formelt{ 
    color:black; 
    text-align: center; 
    margin-top: 10px; 
    margin-bottom: 5px;
    font-size: larger;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
h1
{
color:deeppink;
text-align:center;
padding-top: 10px;
}    
</style>
</head>
<body>
    <div class="edge">
    <div class="box">
    <h1>Body Mass Index</h1>
    <form method="POST">
    {%csrf_token%}
    <div class="formelt">
        Weight : <input type="text" name="Weight" value="{{w}}"></input>(in kg)<br/>
    </div>
    <div class="formelt">
        Height : <input type="text" name="Height" value="{{h}}"></input>(in m)<br/>
    </div>
    <div class="formelt">
        <input type="submit" value="calculate"></input><br/>
    </div>
    <div class="formelt">
       Bmi :<input type="text" name="bmi" value="{{bmi}}"></input>kg/m<sup>2</sup><br/>
    </div>
    </form>
    </div>
    </div>
</body>
</html>

views.py

from django.shortcuts import render
def bmi(request):
    context={}
    context['bmi'] = "0"
    context['w'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        w= request.POST.get('Weight', '0')
        h= request.POST.get('Height', '0')
        print('request=', request)
        print('Weight=',w)
        print('Height=',h)
        w=int(w)
        h=int(h)
        bmi=w/(h*h)
        context['bmi']=bmi
        context['w'] = w
        context['h'] = h
        print('BMI=', bmi)
    return render(request, 'myapp/math.html',context)

urls.py

from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns=[
    path('admin/',admin.site.urls),
    path('bodymassindex/',views.bmi,name="bodymassindex"),
    path('',views.bmi,name="bodymassindexroot")
]
```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2025-10-03 214632.png>)

## HOMEPAGE:
![alt text](<Screenshot 2025-10-03 214606.png>)

## RESULT:
The program for performing server side processing is completed successfully.
