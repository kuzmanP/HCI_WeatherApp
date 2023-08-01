# from django import forms

# # from weather.models import Todo

# # class TodoForm(forms.ModelForm):
# #      class Meta:
         
# #        model = Todo

from django import forms

class Contactform(forms.Form):
  name = forms.CharField()
  email = forms.EmailField(label='Email')
  category = forms.ChoiceField(choices=[('question','Question'),('other','Other')])
  subject = forms.CharField(required='false')
  body = forms.CharField(widget=forms.Textarea)