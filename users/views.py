from django.shortcuts import render, redirect
# from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST': ##if there is a data sent from the form then
        form = UserRegisterForm(request.POST) ###store it in the form variable
        if form.is_valid(): ####if it staisfes the validation form
            form.save()     #####then save this user in the db
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!') ##this is a flash message to be shown in frontend
            return redirect('home-home') #####congrats, go to the home page
    else:
        form = UserRegisterForm() ##create a blank form if the user didnt send any posted data, return this blank form to register.html
    return render(request, 'users/register.html', {'form': form})## return the form you have if the user didnt successed to sign up, 
                                                                 ## either he didnt post a dtat in the form,or posted invalied data
 