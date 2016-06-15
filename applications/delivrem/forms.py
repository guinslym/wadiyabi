from django import forms
from . models import  Product, Zin
from django.forms import ModelForm

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class ProductForm(ModelForm):
    # I might get an error saying that Django can't
    # find the template widget.html for captcha
    #captcha = ReCaptchaField(attrs={'theme' : 'clean'})
    class Meta:
        model = Product
        fields = ['photo','showoff']
