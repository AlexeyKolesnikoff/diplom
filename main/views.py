from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm 
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages 
from .forms import UserRegisterForm, UserLoginForm , ContactForm
from .models import Profile, Trainers, Athletes, Sports, News
from django.utils.translation import gettext as _

def index(request):
    return render(request,'main/index.html')


def news(request):
    return render(request,'main/news.html')


def objects(request):
    return render(request,'main/objects.html')

def contacts(request):
    return render(request,'main/contacts.html')

def managers(request):
    return render(request,'main/managers.html')

def news_detail(request):
    return render(request,'main/news_detail.html')

def trainers_list(request, category_slug=None):
   
    trainers = Trainers.objects.all()
    

    return render(request,
                  'main/trainers.html',
                   {'trainers': trainers})

def athlete_list(request, category_slug=None):
   
    athletes = Athletes.objects.all()
    

    return render(request,
                  'main/athlete.html',
                   {'athletes': athletes})


def sports_list(request, category_slug=None):
   
    sports = Sports.objects.all()
    

    return render(request,
                  'main/sports.html',
                   {'sports': sports})


def news_list(request, category_slug=None):
   
    news = News.objects.all()
    

    return render(request,
                  'main/news.html',
                   {'news': news})




def reg(request): 
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST) 
        if form.is_valid(): 
            try:
                user = form.save() 
                Profile.objects.create(user=user, first_name=user.first_name, last_name=user.last_name) 
                messages.success(request, _(f'Аккаунт создан для {user.email}!')) 
                login(request, user) 
                return redirect('main:objects') 
            except Exception as e:
                messages.error(request, _('Ошибка при создании аккаунта: ') + str(e))
        else:
            messages.error(request, _('Пожалуйста, исправьте ошибки в форме.'))
    else: 
        form = UserRegisterForm() 
    return render(request, 'main/reg.html', {'register_form': form})
 
def auth(request): 
    if request.method == 'POST': 
        form = UserLoginForm(data=request.POST) 
        if form.is_valid(): 
            user = form.get_user() 
            login(request, user) 
            return redirect('main:profile') 
    else: 
        form = UserLoginForm() 
    return render(request, 'main/auth.html', {'form': form}) 
 

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('main:profile')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'main/profile.html', {'form': form})



def contact_form(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Форма обратной связи успешно отправлена!')
            return redirect('main:index')
        else:
            messages.error(request, 'Произошла ошибка при отправке формы обратной связи. Пожалуйста, попробуйте снова.')
    else:
        contact_form = ContactForm()
    
    return render(request, 'main/contact_form.html', {'contact_form': contact_form})
