from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import generics
from .models import IPO
from .serializers import IPOSerializer


class IPOListView(generics.ListAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer

class IPOByStatusView(generics.ListAPIView):
    serializer_class = IPOSerializer

    def get_queryset(self):
        status = self.kwargs['status']
        return IPO.objects.filter(status=status)

class IPODetailView(generics.RetrieveAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
    lookup_field = 'id'


def admin_signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        print("Signup Data:", name, email, password, confirm_password)

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("admin-signup")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect("admin-signup")

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        login(request, user)
        return redirect("admin-dashboard")

    return render(request, "admin_ui/signup.html")



def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")  # <-- changed from email to username
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("admin-dashboard")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("admin-login")

    return render(request, "admin_ui/signin.html")


def forgot_password(request):
    return render(request, "admin_ui/forgot_password.html")

@login_required
def admin_dashboard(request):
    return render(request, "admin_ui/dashboard.html")  # this is just a placeholder

@login_required
def upcoming_ipos_view(request):
    ipos = IPO.objects.all()
    return render(request, 'admin_ui/upcoming_ipos.html', {'ipos': ipos})

@login_required
def register_ipo(request):
    return render(request, "admin_ui/register_ipo.html") # Update if you use another template name

def landing_page(request):
    return render(request, 'admin_ui/landing.html')




