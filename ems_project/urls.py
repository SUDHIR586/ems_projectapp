"""
URL configuration for ems_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from ems_app.views import NoPermsPage
from accounts.views import UserAutocomplete, UserAdminsAutocomplete
# from django_private_chat import urls as django_private_chat_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ems_app.urls')),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    # url('msg/', include('django_private_chat.urls')),
    path('projects/', include('project_app.urls')),
    path('resources/', include('resources_app.urls')),
    path('holiday/', include('holiday_app.urls')),
    path('no-permission/', NoPermsPage.as_view(), name="no_permission"),
    path('user-autocomplete/', UserAutocomplete.as_view(),name='user_autocomplete'),
    path('user-admin-autocomplete/', UserAdminsAutocomplete.as_view(),name='user_admin_autocomplete'),

]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
