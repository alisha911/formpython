
from django import forms

class StudentForm(forms.Form):
    student_id = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'student id'}))
    name= forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'phone'}))
    email = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'email'}))