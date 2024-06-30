from .models import Login,Logout,Register,Expenses
from django.forms import ModelForm # imported it because the form is using a model
from django import forms #import built in methods for a form
#Login Form
class LoginForm(ModelForm) :
    class Meta :
        model = Login #model to be used
        fields = ['username','password']
        widgets = {
            'password' : forms.PasswordInput()
        }
    #method to check if password is the correct one saved in database
    def clean_password(self) :
        password = self.cleaned_data.get('password')
        return password
    
#class DeleteForm(forms.ModelForm) :
   # class Meta :
        model = DeleteExpense
        fields = '__all__'

#class EditForm(forms.ModelForm) :
    #class Meta :
        model = EditExpense
        fields = ['username','amount','category','description']

#The form for adding expenses
class ExpensesForm(forms.ModelForm) :
    #brings in order to your form
    class Meta :
        model = Expenses #model to be used
        fields = ['amount','date','description','category'] #fields in the model
        widgets = {
            'date' : forms.DateInput(attrs={'type' : 'date'}),
            'description' : forms.Textarea(attrs={'rows':3,'cols':20})
        }
 #widgets were created in order to change its default design to fit programmers own liking