from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .forms import RegisterUserForm, UserLoginForm


def view_signup(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            print('user form valid')
            user = form.save()
            login(request, user)
            user_id = request.user.id
            print('user_id =', user_id)

            if user_id == None:
                #redirect_path = '/view_add_counter/view_home/'
                redirect_path = '/view_merits_detail/view_merits/'
            else:
                #redirect_path = '/view_add_counter/view_add_counter/' + str(user_id)
                redirect_path = '/view_merits_detail/view_merits_detail/' + \
                    str(user_id)

            return HttpResponseRedirect(redirect_path)
    else:
        #form = UserCreationForm()
        form = RegisterUserForm()
        print('user get request')

    print('view signup')
    return render(request, 'signup.html', {'form': form})


def view_login(request):
    if request.user.is_authenticated:
        print(request.user)
        user_id = request.user.id
        print('user_id =', user_id)
        redirect_path = '/view_merits_detail/view_merits_detail/' + \
            str(user_id)

        return HttpResponseRedirect(redirect_path)

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print('user form valid', user)

            user_id = request.user.id
            print('user_id =', user_id)
            redirect_path = '/view_merits_detail/view_merits_detail/' + \
                str(user_id)

            return HttpResponseRedirect(redirect_path)
            # return redirect('view_merits')
    else:
        form = UserLoginForm()
        print('login get request')

    print('view login')
    return render(request, 'login.html', {'form': form})


def view_logout(request):
    print('view logout')
    if request.method == 'POST':
        logout(request)
        # return redirect('view_home')
        return redirect('view_merits')

    # return redirect('view_home')
    return redirect('view_merits')


def view_login_counter(request):
    if request.user.is_authenticated:
        print(request.user)
        user_id = request.user.id
        print('user_id =', user_id)
        redirect_path = '/view_add_counter/view_add_counter/' + \
            str(user_id)

        return HttpResponseRedirect(redirect_path)

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print('user form valid', user)

            user_id = request.user.id
            print('user_id =', user_id)
            redirect_path = '/view_add_counter/view_add_counter/' + \
                str(user_id)

            return HttpResponseRedirect(redirect_path)
            # return redirect('view_merits')
    else:
        form = UserLoginForm()
        print('login get request')

    print('view login')
    return render(request, 'login.html', {'form': form})
