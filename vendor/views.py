from django.shortcuts import render, get_object_or_404, redirect
from .forms import VendorForm
from accounts.forms import UserProfileForm
from accounts.models import UserProfile
from .models import Vendor
from django.contrib import messages
from django.contrib.auth .decorators import login_required, user_passes_test
from accounts.views import check_role_vendor
from menu.models import Category, FoodItem
from menu.forms import CategoryForm, FoodItemForm

# Create your views here.

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vprofile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    vendor = get_object_or_404(Vendor, user=request.user)

    profile_form = UserProfileForm(instance=profile)
    vendor_form = VendorForm(instance=vendor)

    if request.method == "POST":
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        vendor_form = VendorForm(request.POST, request.FILES, instance=vendor)
        if profile_form.is_valid() and vendor_form.is_valid():
            profile_form.save()
            vendor_form.save()

            messages.success(request, 'Settings updated.')
            return redirect('vprofile')
        else:
            messages.error(request, 'Something went wrong. Please try again!')

    context = {
        'profile_form': profile_form,
        'vendor_form': vendor_form,
        'profile': profile,
        'vendor': vendor,
    }

    return render(request, 'vendor/vprofile.html', context)

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def menuBuilder(request):
    vendor = Vendor.objects.get(user=request.user)
    categories = Category.objects.filter(vendor=vendor).order_by('-created_at')

    context = {
        'categories': categories,
    }

    return render(request, 'vendor/menu-builder.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def fooditemsByCategory(request, pk=None):
    vendor = Vendor.objects.get(user=request.user)
    category = get_object_or_404(Category, pk=pk)
    fooditems = FoodItem.objects.filter(vendor=vendor, category=category)

    context = {
        'vendor': vendor,
        'category': category,
        'fooditems': fooditems,
    }

    return render(request, 'vendor/fooditems-by-category.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def addCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.vendor = vendor = Vendor.objects.get(user=request.user)
            category.save()

            messages.success(request, 'Category added successfully!')
            return redirect('menu-builder')
        else:
            messages.error(request, 'Something went wrong. Please try again!')
    else:
        form = CategoryForm()

    context = {
        'form': form
    }

    return render(request, 'vendor/add-category.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def editCategory(request, pk):
    category = Category.objects.get(pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            category = form.save(commit=False)
            category.vendor = Vendor.objects.get(user=request.user)
            category.save()

            messages.success(request, 'Category updated successfully!')
            return redirect('menu-builder')
        else:
            messages.error(request, 'Something went wrong. Please try again!')
    else:
        form = CategoryForm(instance=category)

    context = {
        'form': form,
        'category': category,
    }

    return render(request, 'vendor/edit-category.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def deleteCategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, 'Category has been deleted successfully!')
    return redirect('menu-builder')


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def addFood(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES)
        print(form)

        if form.is_valid():
            food = form.save(commit=False)
            food.vendor  = Vendor.objects.get(user=request.user)
            food.save()

            messages.success(request, 'Food Item updated successfully!')
            return redirect('fooditems-by-category', food.category.id)
        else:
            messages.error(request, 'Something went wrong. Please try again!')
    else:
        form = FoodItemForm()
        form.fields['category'].queryset = Category.objects.filter(vendor=Vendor.objects.get(user=request.user))

    context = {
        'form': form,
    }

    return render(request, 'vendor/add-food.html', context)
    

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def editFood(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)

    if request.method == 'POST':
        form = FoodItemForm(request.POST, instance=food)

        if form.is_valid():
            food = form.save(commit=False)
            food.vendor = Vendor.objects.get(user=request.user)
            food.save()

            messages.success(request, 'Food Item updated successfully!')
            return redirect('menu-builder')
        else:
            messages.error(request, 'Something went wrong. Please try again!')
    else:
        form = FoodItemForm(instance=food)

    context = {
        'form': form,
        'food': food,
    }

    return render(request, 'vendor/edit-food.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def deleteFood(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    food.delete()
    messages.success(request, 'food has been deleted successfully!')
    return redirect('fooditems-by-category', food.category.id)