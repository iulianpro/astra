from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'country', 'town_or_city', 'app', 'mac', 'mac_pass', 'notes',)
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Nume si Prenume',
            'email': 'Adresa email',
            'phone_number': 'WhatsApp (daca doriti sa fiti contactat)',
            'country': 'Tara',
            'town_or_city': 'Orasul',
            'app': 'Selectati aplicatia',
            'mac': 'Adresa MAC / TV ID',
            'mac_pass': 'PIN MAC / Parola MAC',
            'notes': 'Nota comanda (opțional)',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
