from django import forms
from .models import AdmissionApplication, Department, Subject

class AdmissionForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="Select Department")
    subject = forms.ModelChoiceField(queryset=Subject.objects.none(), empty_label="Select Subject")

    class Meta:
        model = AdmissionApplication
        fields = ['full_name', 'email', 'phone', 'department', 'subject', 'preferred_date', 'photo']
        widgets = {'preferred_date': forms.DateInput(attrs={'type': 'date'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['subject'].queryset = Subject.objects.filter(department_id=department_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.department:
            self.fields['subject'].queryset = self.instance.department.subjects.all()
