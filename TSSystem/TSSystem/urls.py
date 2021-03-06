"""TSSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
import xadmin
from django.conf.urls import url, include
import course_arrangement.views as course_view


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'^stu/', include('student.urls'), name='student'),
    url(r'^tea/', include('teacher.urls'), name='teacher'),
    url(r'^course/', course_view.courseArrangementAdminView.as_view(), name='course'),
    url(r'^courseArrange/', course_view.courseArrangementView.as_view(), name='course'),
    url(r'', include('main_platform.urls', namespace='main_platform')),

]
