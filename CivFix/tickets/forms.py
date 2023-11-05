from django import forms


class TicketForm(forms.Form):
    CATEGORY_CHOICES = [
        ('INFRASTRUCTURE', 'Infrastructure'),
        ('SAFETY_SECURITY', 'Safety & Security'),
        ('SANITATION_HEALTH', 'Sanitation & Health'),
        ('TRAFFIC_TRANSPORTATION', 'Traffic & Transportation'),
    ]

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]

    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, initial='INFRASTRUCTURE')
    # status = forms.ChoiceField(choices=STATUS_CHOICES, initial='OPEN')
    # creator = forms.CharField(initial='admin')

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if not title:
    #         raise forms.ValidationError('This field is required.')
    #     return title
    #
    # def clean_description(self):
    #     description = self.cleaned_data.get('description')
    #     if not description:
    #         raise forms.ValidationError('This field is required.')
    #     return description
    #
    # def clean_location(self):
    #     title = self.cleaned_data.get('location')
    #     if not title:
    #         raise forms.ValidationError('This field is required.')
    #     return title
    #
    # def clean_category(self):
    #     category = self.cleaned_data.get('category')
    #     if not category:
    #         raise forms.ValidationError('This field is required.')
    #     return category

