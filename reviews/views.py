from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .form import ReviewForm
from django.views import View
# from .models import Reviews

# Create your views here.

class HomepageView(View):
    """Return the home page of website using class based view"""
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/homepage.html", {
            "form":form
        })
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            redirect_path = reverse("thankyou")
            return HttpResponseRedirect(redirect_path)
        return render(request, "reviews/homepage.html",{
            "form": form
        })

def thankyou(request):
    """Returns the thank you page of website"""
    return render(request, "reviews/thankyou.html")