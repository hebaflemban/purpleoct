"""purpleoctpus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rentals import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('purpleoctopus/membership/', views.membership_form, name = 'membership_page'),
    path('purpleoctopus/<int:octopus_id>/', views.octopus, name = 'octopus_page'),
    path('purpleoctopus/login/', views.login_, name = 'login_page'),
    path('purpleoctopus/logout/', views.logout, name = 'logout_page'),
    path('purpleoctopus/notif/', views.notification, name = 'notification_page'),

    path('purpleoctopus/product_list/', views.product_list, name = 'product_list_page'),
    path('purpleoctopus/product_details/<int:product_id>/', views.product_details, name = 'product_details_page'),
    path('purpleoctopus/add_product/', views.add_product, name = 'add_product_page'),
    path('purpleoctopus/edit_product/<int:product_id>/', views.edit_product, name = 'edit_product_page'),
    path('purpleoctopus/delete_product/<int:product_id>/', views.delete_product, name = 'delete_product_page'),

    path('purpleoctopus/rent_product/<int:product_id>/', views.rent_product, name = 'rent_product_page'),

    ]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
