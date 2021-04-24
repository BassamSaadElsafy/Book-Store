from django import forms 
from .models import Book, Category
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model= Book
        fields= '__all__'         
        exclude = ('isbn',)

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) > 10 and len(title) < 60:
            return title
        raise ValidationError("title should be between 10 and 60 characters!")

# class CategoryForm(forms.ModelForm):  validators
#     class Meta:
#         model=Category
#         fields= '__all__'         

#     def clean_title(self):
#         title = self.cleaned_data.get("title")
#         if len(title) > 2:
#             return title
#         raise ValidationError("title should be at least 2 characters!")
