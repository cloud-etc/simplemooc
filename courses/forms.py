from django import forms
from django.core.mail import send_mail
from django.conf import settings
from core.mail import send_mail_template
from .models import Comment

class ContactCourse(forms.Form):
    """formulario do contato"""
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem', widget=forms.Textarea
    )

    """funcao para o envio de email"""
    def send_mail(self, course):
        subject = '%s Contato' % course
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],

        }
        template_name = 'courses/contact_email.html'
        send_mail_template(subject, template_name, context,
                           [settings.DEFAULT_FROM_EMAIL])

    # def send_mail(self, course):
    #     subject = '[%s] Contato' % course
    #     context = {
    #         'name': self.cleaned_data['name'],
    #         'email': self.cleaned_data['email'],
    #         'message': self.cleaned_data['message'],
    #
    #     }
    #     template_name = 'courses/email.html'
    #     send_mail(
    #         subject, template_name, context,
    #         [settings.DEFAULT_FROM_EMAIL]
    #     )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']