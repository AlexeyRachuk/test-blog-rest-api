from django.shortcuts import render

from .models import Contact
from .forms import FormOnContacts


def contact_page(request):
    error = ''
    if request.method == 'POST':
        form = FormOnContacts(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                error = 'Форма не отправлена'
    else:
        form = FormOnContacts()
    return render(request, 'contact.html',
                  {'form': form, 'error': error, 'contacts': Contact.objects.all()})
