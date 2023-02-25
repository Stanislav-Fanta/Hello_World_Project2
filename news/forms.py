from django import forms
from .models import Article,News,Review

class Article_Form(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('name','description', 'image', 'publication_date', 'author', 'category')


class New_Form(forms.ModelForm):

    class Meta:
        model = News
        fields = ('name', 'description', 'image', 'publication_date', 'author', 'category')


class Review_Form(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('name', 'description', 'image', 'publication_date', 'author', 'category')