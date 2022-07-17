from django.shortcuts import render

# Create your views here.

def main(request):    
    context={
    }
    return render(request, 'index.html', context)


def implementation(request):    
    context={
    }
    return render(request, 'implementation.html', context)


def contact(request):    
    context={
    }
    return render(request, 'contact.html', context)