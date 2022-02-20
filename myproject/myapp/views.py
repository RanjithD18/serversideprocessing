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

