from django import forms
from .models import Movie, Comment

class CreateForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['poster', 'title', 'description', 'genre', 'score']
        widgets = {
            'score': forms.NumberInput(attrs={
                'min': 0,
                'max': 5,
                'step': 0.5,
            }),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )
        
# # form2 (ModelForm 예시)
# class ProductForm(forms.ModelForm):
#     CATEGORY_CHOICES = [
#         ('ELEC', 'Electronics'),
#         ('BOOK', 'Books'),
#         ('FASH', 'Fashion'),
#     ]
#     category = forms.MultipleChoiceField(
#         choices=CATEGORY_CHOICES,
#         required=False,
#         help_text='하나 이상의 카테고리를 선택하세요',
#         widget=forms.CheckboxSelectMultiple,  # 체크박스 형태로 랜더링
#     )

#     class Meta:
#         model = Movie
#         fields = '__all__'

# # form2 (ModelForm 예시)
# class ProductForm(forms.ModelForm):
#     CATEGORY_CHOICES = [
#         ('ELEC', 'Electronics'),
#         ('BOOK', 'Books'),
#         ('FASH', 'Fashion'),
#     ]
#     category = forms.MultipleChoiceField(
#         choices=CATEGORY_CHOICES,
#         required=False,
#         help_text='하나 이상의 카테고리를 선택하세요',
#         widget=forms.CheckboxSelectMultiple,  # 체크박스 형태로 랜더링
#     )

#     class Meta:
#         model = Product
#         fields = ['name', 'price', 'category']


# # form3
# class BaseForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     email = forms.EmailField()


# # form4
# class ExtendedForm(BaseForm):
#     address = forms.CharField(max_length=100)


# # form5
# class WidgetForm(forms.Form):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#             },
#         )
#     )
#     bio = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 'rows': 5,
#                 'cols': 50,
#                 'style': 'resize: none;',
#             }
#         ),
#         required=False,
#     )
