import secrets
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import RegisterForm, LoginForm, OTPForm
from .models import PhoneOTP

User = get_user_model()


def send_otp(user):
    PhoneOTP.objects.filter(user=user).delete()
    code = f"{secrets.randbelow(1000000):06d}"
    PhoneOTP.objects.create(user=user, code=code)
    print(f"\n[DEV] OTP for {user.phone}: {code}\n")  # replaced by a real SMS on Day 24


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        ident = data['identifier']
        if '@' in ident:
            user = User.objects.create_user(
                email=ident, password=data['password'], full_name=data['full_name'])
            login(request, user)
            return redirect('dashboard')
        user = User.objects.create_user(
            phone=ident, password=data['password'], full_name=data['full_name'])
        send_otp(user)
        request.session['pending_user_id'] = user.id
        return redirect('verify-otp')
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data['identifier'],
            password=form.cleaned_data['password'],
        )
        if user is None:
            form.add_error(None, "Wrong email, phone number or password.")
        elif user.needs_verification:
            send_otp(user)
            request.session['pending_user_id'] = user.id
            return redirect('verify-otp')
        else:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'accounts/login.html', {'form': form})


def verify_otp_view(request):
    user_id = request.session.get('pending_user_id')
    if not user_id:
        return redirect('login')
    user = User.objects.get(pk=user_id)
    form = OTPForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        otp = PhoneOTP.objects.filter(user=user).first()
        if otp and not otp.is_expired() and otp.code == form.cleaned_data['code']:
            user.is_phone_verified = True
            user.save(update_fields=['is_phone_verified'])
            otp.delete()
            del request.session['pending_user_id']
            login(request, user)
            return redirect('dashboard')
        form.add_error('code', "Invalid or expired code.")
    return render(request, 'accounts/verify_otp.html', {'form': form, 'phone': user.phone})


@require_POST
def logout_view(request):
    logout(request)
    return redirect('home')
