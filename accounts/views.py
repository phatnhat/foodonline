from django.shortcuts import render, redirect
from .forms import UserForm
from vendor.forms import VendorForm
from .models import User, UserProfile
from vendor.models import Vendor
from django.contrib import messages

# Create your views here.
def registerUser(request):
    form = UserForm()

    if request.method == 'POST':
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

            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'accounts/register-user.html', context)


def registerVendor(request):
    form = UserForm()
    v_form = VendorForm()

    if request.method == 'POST':
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

            return redirect('home')

    context = {
        'form': form,
        'v_form': v_form
    }

    return render(request, 'accounts/register-vendor.html', context)