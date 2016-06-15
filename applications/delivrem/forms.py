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
    showoff = forms.CharField(
        label="showoff",
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'whadiyabi',
            'class': 'form-control',
        }))
    photo = forms.ImageField(
        label="Photo",
        required=True,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
        }))
    class Meta:
        model = Product
        fields = ['showoff', 'photo']
