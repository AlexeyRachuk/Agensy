from django.shortcuts import render
from estate_contact.models import Contact, FormContactPage
from django.core.mail import send_mail

from .forms import ContactForm


def contact_page(request):
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                send_mail(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['subject'],
                          form.cleaned_data['message'], 'alexeyrachuk94@gmail.com', ['alexeyrachuk94@gmail.com'],
                          fail_silently=False)
            except:
                error = 'Форма не была отправлена'
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html',
                  {'form': form, 'error': error, 'contacts': Contact.objects.all(), 'title': 'Контакты'})
