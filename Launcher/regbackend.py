from registration.backends.default.views import RegistrationView
from .forms import ProfileForm
from .models import Profile


class MyRegistrationView(RegistrationView):
    form = ProfileForm

    def register(self, form):
        new_user = super(MyRegistrationView,self).register(form)
        n = form.cleaned_data['roll_number']
        if form.is_valid():
            new_profile = Profile.objects.create(user=new_user,roll_number = n)
            new_profile.save()
        return new_user

