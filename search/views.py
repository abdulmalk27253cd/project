from django.shortcuts import render
# Create your views here.
def search_product(request):
        return render(request, 'search.html', {})