from django.shortcuts import render
from django.views import View
# Create your views here.


class IndexView(View):
    """
    首页
    """
    def get(self, request):
        return render(request, 'index.html',)


class LoginView(View):
    """
    登陆
    """
    def get(self, request):
        return render(request, 'index.html',)


    def post(self,request):
        return render(request, 'index.html',)
        # return HttpResponse('{"status": "fail", "msg": "用户未激活, 请先激活用户"}', content_type='application/json')

