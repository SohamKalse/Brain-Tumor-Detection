from django.shortcuts import render,HttpResponse

# Create your views here.
def base(request):
    return render(request,'base.html')
    # return HttpResponse("This is home page")

def login(request):
    return render(request,'login.html')


def SignUp(request):
    return render(request,'SignUp.html')

def contact(request):
    return render(request,'contact.html')

    


# def about(request):
#     return HttpResponse("This is about page")