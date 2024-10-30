from django.shortcuts import render

# Create your views here.
def humburg(request):
        return render(request, 'Firstsection.html', {})