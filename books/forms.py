from django import forms


class ReviewForm(forms.Form):
    rating = forms.IntegerField(min_value=1, max_value=5)
    review = forms.CharField(widget=forms.Textarea)
