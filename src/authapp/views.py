from django.shortcuts import render, redirect
from django.views import View



class Home(View):
    
    """Home View"""

    def get(self, request):
        
        context = [
            
        ]
        
        return render(request, 'authapp/home.html', context)
    
    
class Login(View):
    
    """Account Login View 
    """
    
    def get(self, request):
        
        context = [
            
        ]
        
        return render(request, 'authapp/login.html', context)
    
    
    def post(self, request):
        
        """Handle the Login post request
        """
        
        return redirect('home')
