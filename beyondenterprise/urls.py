"""beyondenterprise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    # ...
    path('admin/', admin.site.urls),
    # ...
 
    # If no prefix is given, use the default language
    prefix_default_language=False
)

admin.site.site_header = 'Beyond Enterprise'                    # default: "Django Administration"
admin.site.index_title = 'Beyond Enterprise'                 # default: "Site administration"
admin.site.site_title = _('My Site Management') # default: "Django site admin"

