from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
#def homeview(request)
#    return HttpResponse('hellow world')
from django.views.generic import ListView
from example.models import Publisher, Book, Author
from example.forms import ContactForm
import datetime
from django.core.mail import send_mail, get_connection

class PublisherList(ListView):
    model = Publisher

def ua_display_good1(request):
        try:
            ua = request.META['HTTP_USER_AGENT']
        except KeyError:
            ua = 'unknown'
        return HttpResponse("Your browser is %s" % ua)

def search_form(request):
    return render(request , 'example/search_form.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'example/search_results.html', {'books': books, 'query': q})
    return render(request, 'example/search_form.html', {'error': error})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})

def thanks(request):
    return render(request, 'thanks.html')
