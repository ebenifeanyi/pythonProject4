from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
                  path('', home, name='home'),
                  path('create', createacct, name='create'),
                  path('profile', profile_create, name='profile'),
                  path('<int:pk>/', profile_detail, name='profile_detail'),
                  path('add-friend/<int:pk>', add_friend, name='add_friend'),
                  path('friends-list<int:pk>', view_friends, name='friends_list'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
