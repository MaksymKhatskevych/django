from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.urls import reverse
from .models import Description
from django.views.generic import ListView


def contactform(reguest): 
    
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']         
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recepients = ['khatskevychmaksym@ukr.net']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, 'khatskevychmaksym@ukr.net', recepients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return HttpResponseRedirect(reverse('thanks'))

    else:
        form = ContactForm()
        template_name = Description.objects.all()
        context = {
                   'form': form, 
                   'template_name': template_name 
                    }
    # Выводим форму в шаблон
    return render(reguest, 'ord/order.html', context)
        

def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'ord/thanks.html', {'thanks': thanks})    


    """'username': auth.get_user(reguest).username"""

"""class DeskListView(ListView):
    
    def get(self,request):
        template_name = Description.objects.all()
        return render(request, 'ord/order.html', {'template_name': template_name} )"""



  
