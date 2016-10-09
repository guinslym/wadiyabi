from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

def is_staff(user):
    return user and not user.is_anonymous() and user.is_staff


class SuccessMessageMixin(object):
    """
    Adds a success message on successful form submission.
    """
    success_message = ''

    def form_valid(self, form):
        response = super(SuccessMessageMixin, self).form_valid(form)
        success_message = self.get_success_message()
        if success_message:
            messages.success(self.request, success_message)
        return response

    def delete(self, request, *args, **kwargs):
        response = super(SuccessMessageMixin, self).delete(request, *args, **kwargs)
        success_message = self.get_success_message()
        if success_message:
            messages.success(self.request, success_message)
        return  response

    def get_success_message(self):
        return self.success_message % dict(object=self.object)

class StaffMixin(object):
    @method_decorator(login_required)
    @method_decorator(user_passes_test(is_staff))
    def dispatch(self, *args, **kwargs):
        return super(StaffMixin, self).dispatch(*args, **kwargs)
