import datetime
from django import forms
from vdeed_app.models import deeds1, deeds2, deeds3, globalLamrim2, plastic, paper, misc
from datetime import datetime, time


def add_date1_needed():
    filename = 'date1.txt'
    file = open(
        'D:/djangoProject/virtuous_deed_project/vdeeds/static/' + filename, 'r')
    date = file.read()
    file.close()
    print(date)
    today = datetime.now().strftime("%Y%m%d")
    print('today', today)
    if today != date:
        print('different date')
        return True
    else:
        print('same date')
        return False


def write_today_date1():
    filename = 'date1.txt'
    today = datetime.now().strftime("%Y%m%d")
    file = open(
        'D:/djangoProject/virtuous_deed_project/vdeeds/static/' + filename, 'w')
    file.write(today)
    file.close()
    print('date written')

# Removes character at index i


def remove(string, i):
    # Characters before the i-th indexed
    # is stored in a variable a
    a = string[: i]

    # Characters after the nth indexed
    # is stored in a variable b
    b = string[i + 1:]

    # Returning string after removing
    # nth indexed character.
    return a + b


class deeds1Form(forms.ModelForm):
    class Meta:
        model = deeds1
        fields = ['deed', 'name']
        labels = {
            'name': 'Enter your name here (姓名)',
            'deed': 'OMAK (观功念恩)'  # OMAK (观功念恩)
        }
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name1', 'class': 'form-control', 'required': 'True', 'placeholder': 'Name (姓名)', 'blank': 'False'}),
            'deed': forms.Textarea(attrs={'id': 'deed1', 'rows': "4", 'maxlength': '250', 'class': 'form-control', 'required': 'True', 'placeholder': 'Message here (在此留言)', 'blank': 'False'})
        }

    def clean(self):
        date = datetime.now().strftime("%d/%m/%Y")
        date1 = remove(date, 6)
        date1 = remove(date1, 6)
        cleaned_data = self.cleaned_data
        begin = '<p>'
        end = '</p> <br>'
        cleaned_data['deed'] = begin + cleaned_data['deed'] + \
            ' (' + cleaned_data['name'] + ') ' + date1 + end
        print(cleaned_data)
        return cleaned_data

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        hide_condition = kwargs.pop('hide_condition', None)
        super(deeds1Form, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields['deed'].widget = HiddenInput()
            self.fields['name'].widget = HiddenInput()
            # or alternately:  del self.fields['fieldname']  to remove it from the form altogether.


class deeds2Form(forms.ModelForm):
    class Meta:
        model = deeds2
        fields = ['deed', 'name']
        labels = {
            'name': 'Enter your name here (姓名)',
            'deed': 'Remembering Kindness (修信念恩)'
        }
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name2', 'class': 'form-control', 'required': 'True', 'blank': 'False'}),
            'deed': forms.Textarea(attrs={'id': 'deed2', 'rows': "4", 'maxlength': '250', 'class': 'form-control', 'required': 'True', 'blank': 'False'})
        }

    def clean(self):
        date = datetime.now().strftime("%d/%m/%Y")
        date2 = remove(date, 6)
        date2 = remove(date2, 6)
        cleaned_data = self.cleaned_data
        begin = '<p>'
        end = '</p> <br>'
        cleaned_data['deed'] = begin + cleaned_data['deed'] + \
            ' (' + cleaned_data['name'] + ') ' + date2 + end
        print(cleaned_data)
        return cleaned_data

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        hide_condition = kwargs.pop('hide_condition', None)
        super(deeds2Form, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields['deed'].widget = HiddenInput()
            self.fields['name'].widget = HiddenInput()
            # or alternately:  del self.fields['fieldname']  to remove it from the form altogether.


class deeds3Form(forms.ModelForm):
    class Meta:
        model = deeds3
        fields = ['deed', 'name']
        labels = {
            'name': 'Enter your name here (姓名)',
            'deed': 'Virtuous deeds (善行点滴)'
        }
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name3', 'class': 'form-control', 'required': 'True', 'blank': 'False'}),
            'deed': forms.Textarea(attrs={'id': 'deed3', 'rows': "4", 'maxlength': '250', 'class': 'form-control', 'required': 'True', 'blank': 'False'})
        }

    def clean(self):
        date = datetime.now().strftime("%d/%m/%Y")
        date3 = remove(date, 6)
        date3 = remove(date3, 6)
        cleaned_data = self.cleaned_data
        begin = '<p>'
        end = '</p> <br>'
        cleaned_data['deed'] = begin + cleaned_data['deed'] + \
            ' (' + cleaned_data['name'] + ') ' + date3 + end
        print(cleaned_data)
        return cleaned_data

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        hide_condition = kwargs.pop('hide_condition', None)
        super(deeds3Form, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields['deed'].widget = HiddenInput()
            self.fields['name'].widget = HiddenInput()
            # or alternately:  del self.fields['fieldname']  to remove it from the form altogether.


class globalLamrim2Form(forms.ModelForm):
    class Meta:
        model = globalLamrim2
        fields = ['deed', 'name']
        labels = {
            'name': 'Name and Class (姓名与班级)',
            'deed': 'Global Lamrim II Sharing (广海明月分享)'
        }
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name4', 'class': 'form-control', 'required': 'True', 'blank': 'False'}),
            'deed': forms.Textarea(attrs={'id': 'deed4', 'rows': "4", 'maxlength': '250', 'class': 'form-control', 'required': 'True', 'blank': 'False'})
        }

    def clean(self):
        date = datetime.now().strftime("%d/%m/%Y")
        date4 = remove(date, 6)
        date4 = remove(date4, 6)
        cleaned_data = self.cleaned_data
        begin = '<p>'
        end = '</p> <br>'
        br = '<br>'
        strongStart = '<strong>'
        strongEnd = '</strong>'
        cleaned_data['deed'] = begin + cleaned_data['deed'] + br + strongStart + \
            cleaned_data['name'] + strongEnd + ' (' + date4 + ')' + end
        print(cleaned_data)
        return cleaned_data

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        hide_condition = kwargs.pop('hide_condition', None)
        super(globalLamrim2Form, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields['deed'].widget = HiddenInput()
            self.fields['name'].widget = HiddenInput()
            # or alternately:  del self.fields['fieldname']  to remove it from the form altogether.


class DateInput(forms.DateInput):
    input_type = 'date'


class DateForm(forms.Form):
    date1_from = forms.DateField(widget=DateInput)
    date1_to = forms.DateField(widget=DateInput)


class Date2Form(forms.Form):
    date2_from = forms.DateField(widget=DateInput)
    date2_to = forms.DateField(widget=DateInput)


class Date3Form(forms.Form):
    date3_from = forms.DateField(widget=DateInput)
    date3_to = forms.DateField(widget=DateInput)


class Date4Form(forms.Form):
    date4_from = forms.DateField(widget=DateInput)
    date4_to = forms.DateField(widget=DateInput)


class plasticForm(forms.ModelForm):
    class Meta:
        model = plastic
        fields = ['plastic_bag_counter', 'plastic_bottle_counter',
                  'plastic_wrapper_counter', 'plastic_cup_straw_counter']


class sutraRecitationForm(forms.ModelForm):
    class Meta:
        model = paper
        fields = ['paper_tissue_counter', 'paper_counter',
                  'paper_cup_counter', 'paper_cigarette_butt_counter']


class mantraRecitationForm(forms.ModelForm):
    class Meta:
        model = misc
        fields = ['misc_glass_bottle_counter', 'misc_mask_counter',
                  'misc_others_counter', 'misc_can_counter']
