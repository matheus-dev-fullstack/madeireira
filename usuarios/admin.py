from django.contrib import admin
from .models import Users 
from django.contrib.auth import admin as admin_auth_django
from .models import Users

# from .forms import UserChangeForm, UserCreationForm

admin.site.register(Users)