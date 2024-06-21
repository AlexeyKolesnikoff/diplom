from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView, logout_then_login

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('trainers', views.trainers_list, name='trainers' ),
    path('athlete', views.athlete_list, name='athlete' ),
    path('news', views.news_list, name='news' ),
    path('sports', views.sports_list, name='sports' ),
    path('objects', views.objects, name='objects' ),
    path('contacts', views.contacts, name='contacts' ),
    path('managers', views.managers, name='managers' ),
    path('reg', views.reg, name='reg' ),
    path('auth', views.auth, name='auth' ),
    path('profile', views.profile, name='profile' ),
    path('logout/', LogoutView.as_view(template_name='account/registration/index.html'), name='logout'),
    path('contact_form', views.contact_form, name='contact_form' ),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)