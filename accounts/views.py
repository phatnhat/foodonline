from django.shortcuts import render, redirect
from .forms import UserForm
from vendor.forms import VendorForm
from .models import User, UserProfile
from vendor.models import Vendor
from django.contrib import messages, auth
from .utils import detectUser
from django.contrib.auth .decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

# Create your views here.

#restrict the vendor form accessing the customer page
def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied


#restrict the customer form accessing the vendor page
def check_role_customer(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied


def registerUser(request):
    form = UserForm()

    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('dashboard')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # create the user using the form
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            user.save()

            # create the user using create_user method
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
            #                                 email=email, password=password)
            # user.role = User.CUSTOMER
            # user.save()

            messages.success(request, 'Your acccount has been registered successfully!')

            return redirect('register-user')

    context = {
        'form': form,
    }

    return render(request, 'accounts/register-user.html', context)




def registerVendor(request):
    form = UserForm()
    v_form = VendorForm()

    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('my-account')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.VENDOR
            user.save()

            vendor = v_form.save(commit=False)
            vendor.user = user
            vendor.user_profile = UserProfile.objects.get(user=user)
            vendor.save()

            messages.success(request, 'Your account has been registered successfully! Plase wait for the approval.')

            return redirect('login')

    context = {
        'form': form,
        'v_form': v_form
    }

    return render(request, 'accounts/register-vendor.html', context)




def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('my-account')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('my-account')
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('login')
    return render(request, 'accounts/login.html')



def logout(request):
    auth.logout(request)
    messages.info(request, 'You are logged out.')
    return redirect('login')


@login_required(login_url='login')
def myAccount(request):
    user = request.user
    redirect_url = detectUser(user)
    return redirect(redirect_url)

@login_required(login_url='login')
@user_passes_test(check_role_customer)
def custDashboard(request):
    return render(request, 'accounts/cust-dashboard.html')


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vendorDashboard(request):
    return render(request, 'accounts/vendor-dashboard.html')