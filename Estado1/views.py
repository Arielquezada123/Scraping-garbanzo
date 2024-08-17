import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .forms import BusquedaForm

def busqueda_view(request):
    form = BusquedaForm()
    results = []

    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            
            # Realizar el web scraping
            url = f'https://ww3.lectulandia.com/search/{busqueda}'# Reemplaza con la URL real de búsqueda
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            books = soup.find_all('a', class_='title')  
            results = [book.get_text() for book in books]
        
    return render(request, 'busqueda.html', {'form': form, 'results': results})
