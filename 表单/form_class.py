from django import forms

class TestForm(forms.Form):
    SEX = (
        ('male', '男性'),
        ('female', '女性')
    )
    name = forms.CharField(max_length=5)
    sex  = forms.ChoiceField(choices=SEX)
    age  = forms.IntegerField()
    login_date = forms.DateField()

POST = {'name':'bobo', 'sex':"male", 'age': '25', 'login_date':'2020-1-1'}

form = TestForm(POST)

