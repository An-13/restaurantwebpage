from django.test import TestCase

# Create your tests here.
def webpage(request):
    return render(request,'webpage.html')
