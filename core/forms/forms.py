# -*- coding: utf-8 -*-
from django import forms
from datetime import datetime

class CalendarForm(forms.ModelForm):

    user = forms.CharField(max_length=100)
    title = forms.CharField(max_length=200)
    description = forms.TextField()
    starts_at = forms.DateTimeField(default=datetime.now)
    ends_at = forms.DateTimeField(default=datetime.now)
    created_at = forms.DateTimeField(default=datetime.now)