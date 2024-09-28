from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

class Meta:
    model = Review
    fields = ('review_title', 'rating',)
    widgets = {
        'review_title': forms.TextInput(
             attrs={'class': 'form-control',
                'placeholder': 'Enter your reviews'
                }
            ),
        }