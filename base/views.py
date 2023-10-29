from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
# Create your views here.


class Home(View):
    template_name = "base/home.html"
    
    def get(self, request):
        return render(request, self.template_name, context={})
    
@login_required 
def home(request): 
    return Home.as_view()(request)