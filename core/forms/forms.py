# -*- coding: utf-8 -*-
from django import forms
from datetime import datetime
from ..models import Event



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"