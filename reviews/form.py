from django import forms
from .models import Reviews

# class ReviewForm(forms.Form):
#     """Create a form for user"""
#     username = forms.CharField(max_length=100, label="Your Name",error_messages={
#         "required": "It's mendatory to fill your name.",
#         "max_length": "Please write your name in short form."
#     })
#     review_text = forms.CharField(widget=forms.Textarea,max_length=200,label="Your feedback")
#     rating = forms.IntegerField(min_value=1,max_value=5,label="Rating")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = "__all__"
        labels = {
            "username": "Your Name",
            "review_text": "Your Review",
            "rating": "Your Rating"
        }
        errors = {
            "username": {
                "required": "It's mendatory to fill your name.",
                "max_length": "Please write your name in short form."
            }
        }
