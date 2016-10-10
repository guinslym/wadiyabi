from django import forms
from . models import  Product, Zin
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _, ugettext
from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
#from crispy_forms.layout import Layout, Fieldset, Submit, Button

from django.core.urlresolvers import reverse

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['showoff', 'photo']
    """
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
    """
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"

        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Main data"),
                layout.Field("showoff", css_class="input-block-level", rows="3"),
            ),
            layout.Fieldset(
                _("Image"),
                layout.Field("photo", css_class="input-block-level"),
                layout.HTML(u"""{% load i18n %}
                    <p class="help-block">{% trans "Available formats are JPG, GIF, and PNG. Minimal size is 800 × 800 px." %}</p>
                """),
                title=_("Image upload"),
                css_id="image_fieldset",
            ),
            bootstrap.FormActions(
                layout.Submit("submit", _("Save")),
                layout.Button('cancel', 'Cancel', onclick="location.href='%s'" % reverse('delivrem:product-home')),
            )
        )


class ProductEditForm(ModelForm):
    class Meta:
        model = Product
        fields = ['showoff', 'photo', 'price']
    """
    """
    def __init__(self, *args, **kwargs):
        super(ProductEditForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"

        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Add Price"),
                layout.Field("price", css_class="input-block-level", rows="3"),
                    ),
            layout.Fieldset(
                _("Main data"),
                layout.Field("showoff", css_class="input-block-level", rows="3"),
            ),
            layout.Fieldset(
                _("Image"),
                layout.Field("photo", css_class="input-block-level"),
                layout.HTML(u"""{% load i18n %}
                    <p class="help-block">{% trans "Available formats are JPG, GIF, and PNG. Minimal size is 800 × 800 px." %}</p>
                """),
                title=_("Image upload"),
                css_id="image_fieldset",
            ),
            bootstrap.FormActions(
                layout.Submit("submit", _("Save")),
                layout.Button('cancel', 'Cancel', onclick="location.href='%s'" % reverse('delivrem:product-home')),
            )
        )
