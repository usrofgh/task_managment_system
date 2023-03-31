from django import forms
from django.contrib.auth import get_user_model

from todo.models import Task, TaskType


class TaskForm(forms.ModelForm):
    workers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = "__all__"


class PriorityRadioForm(forms.ModelForm):
    fweffff = forms.ModelChoiceField(
        queryset=TaskType.objects.all(),
        widget=forms.RadioSelect(),
    )

    class Meta:
        model = Task
        fields = "__all__"
