from django.shortcuts import render, redirect
from .forms import MembershipForm, LoginForm, ProductForm, ProductRent
from .models import Product
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail



def membership_form(request):
    # send_mail(
    #     subject = 'That’s your subject',
    #     message = 'That’s your message body',
    #     from_email = 'flembanheba@gmail.com',
    #     recipient_list = ['flemban2@illinois.edu']
    # )

    form = MembershipForm()
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == 'POST':
                form = MembershipForm(request.POST, request.FILES)

                if form.is_valid():
                    user = form.save(commit=False)
                    user.set_password(user.password)
                    user.save()
                    messages.success(request, 'Membership created successfully, Check your email!')
                    return redirect ('notification_page')
        else:
            messages.warning(request, 'Ask a coordinato for help!')
            return redirect ('notification_page')

    else:
        return redirect ('login_page')


    context = {
        'form' : form
    }
    return render (request, 'membership_form.html', context)


def notification(request):
    return render (request, 'notification.html')


"""
coordinator access only operations + product CRUD poerations
"""
def search_product(request):
    #if request.user.is_staff():


    context = {

    }
    return render (request, '.html', context)


def rent_product(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductRent(instance = product)

    if request.user.is_authenticated:
        if request.user.is_staff:
            form = ProductRent(instance = product)
            if request.method == 'POST':
                form = ProductRent(request.POST, request.FILES, instance = product)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Product Rented!')
                    return redirect ('notification_page')
        else:
            messages.warning(request, 'You don\'t have access to this page')
            return redirect ('notification_page')
    else:
        return redirect ('login_page')

    context = {
        'form' : form,
    }
    return render (request, 'product_form.html', context)


def return_product(request): #update?
    #if request.user.is_staff():

    return render (request, '.html', context)


def add_product(request):
    p_form = ProductForm()
    if not request.user.is_authenticated:
        return redirect ('login_page')
    if not request.user.is_staff:
        messages.warning(request, 'You don\'t have access to this page')
        return redirect ('notification_page')

    if request.method == 'POST':
        p_form = ProductForm(request.POST, request.FILES)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Product Added to shop successfully!')
            return redirect ('notification_page')
        
    context = {
        'p_form' : p_form,
    }
    return render (request, 'product_form.html', context)


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForm(instance = product)

    if request.user.is_authenticated:
        if request.user.is_staff:
            form = ProductForm(instance = product)
            if request.method == 'POST':
                form = ProductForm(request.POST, request.FILES, instance = product)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Product edited successfully!')
                    return redirect ('notification_page')
        else:
            messages.warning(request, 'You don\'t have access to this page')
            return redirect ('notification_page')
    else:
        return redirect ('login_page')

    context = {
        'form' : form,
    }
    return render (request, 'product_form.html', context)


def delete_product(request, product_id):
    if request.user.is_staff:
        product = Product.objects.get(id=product_id)
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('product_list')
    else:
        messages.warning(request, 'You don\'t have access to this page')
        return redirect ('notification_page')

"""
Main pages on nav bar

"""

def home(request):
    context = {
        'name' : '',
        'adress' : '',
        'phone' : '',
        'from' : '',
        'To' : ''
    }
    return render (request, 'home.html', context)


def about(request):
    context = {
        'name' : '',
        'adress' : '',
        'phone' : '',
        'from' : '',
        'To' : ''
    }
    return render (request, 'about.html', context)

def contact(request):
    context = {
        'name' : '',
        'adress' : '',
        'phone' : '',
        'from' : '',
        'To' : ''
    }
    return render (request, 'about.html', context)


def product_list(request):
    context = {
        'products' : Product.objects.all()
    }
    return render (request, 'product_list.html', context)

"""

administration pages

"""

def octopus(request, octopus_id):
    octopus = User.objects.get(id=octopus_id)

    context = {
        "octopus": octopus,
    }
    return render(request, 'octopus.html', context)


def login_(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user.is_staff:
                login(request, user)
                return redirect ('octopus_page', user.id)


    context = {
        'form' : form,
    }
    return render (request, 'login.html', context)


def logout(request):
    logout(request)
    return redirect('home_page')



"""

subpages of the main pages


"""

def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product,
    }
    return render(request, 'product_detail.html', context)
