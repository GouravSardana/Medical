from django.contrib.auth.models import User
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from django.views.generic import TemplateView
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required



class Home(TemplateView):
    template_name = 'home.html'

class SignUp(TemplateView):
    template_name = 'signup.html'
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            first_name = self.request.POST.get('first_name')
            last_name = self.request.POST.get('last_name')
            email=self.request.POST.get('email')
            username = self.request.POST.get('username')
            password= self.request.POST.get('password')
            form = User.objects.create_user(first_name=first_name, last_name=last_name,email=email, username=username,password=password)  # = wala model ka naam
            form.save()
            print(form)
            return HttpResponseRedirect(reverse('user_login'))


class LogIn(TemplateView):
    template_name = 'login.html'


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')


        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request, user)

                if user.groups.filter(name='Doctor'):
                    return HttpResponse('Hey student')
                elif user.groups.filter(name='LabUser'):
                    return HttpResponseRedirect(reverse('patient_details'))
                else:
                    return HttpResponse('Hey Customer')
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('home'))


class Patient_details(TemplateView):
    template_name = 'patient-details.html'

