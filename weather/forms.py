from django.forms import ModelForm, TextInput
class cityform(ModelForm):
    class meta:
        model = City
