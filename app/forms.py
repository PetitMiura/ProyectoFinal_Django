from django import forms
from django.core.exceptions import ValidationError

# Definición de opciones para los campos Select
CURRENCY_CHOICES = [
    ('EUR', 'EUR'), ('BTC', 'BTC'), ('ETH', 'ETH'), 
    ('BNB', 'BNB'), ('ADA', 'ADA'), ('DOT', 'DOT'), 
    ('XRP', 'XRP'), ('SOL', 'SOL'), ('USDT', 'USDT'), 
    ('MATIC', 'MATIC')
]

# Validador para asegurarse de que el valor sea mayor que cero
def validate_greater_than_zero(value):
    if value <= 0:
        raise ValidationError('La cantidad debe ser mayor que cero.')

# Validador para asegurarse de que la elección de la moneda sea válida
def validate_currency_choice(value):
    valid_options = [choice[0] for choice in CURRENCY_CHOICES]
    if value not in valid_options:
        raise ValidationError('Opción de moneda inválida.')

class CompraForm(forms.Form):
    def init(self, *args, **kwargs):
        super(CompraForm, self).init(args, **kwargs)
        # Añadiendo clases CSS a los widgets
        self.fields['from_currency'].widget.attrs.update({'class': 'custom-select-class1'})
        self.fields['cantidad_from'].widget.attrs.update({'class': 'custom-input-class1'})
        self.fields['to_currency'].widget.attrs.update({'class': 'custom-select-class'})
        self.fields['cantidad_to'].widget.attrs.update({'type': 'hidden'})

    from_currency = forms.ChoiceField(
        choices=CURRENCY_CHOICES,
        label='From:',
        validators=[validate_currency_choice]
    )
    cantidad_from = forms.FloatField(
        label='Cantidad From:',
        validators=[validate_greater_than_zero]
    )
    to_currency = forms.ChoiceField(
        choices=CURRENCY_CHOICES,
        label='To:',
        validators=[validate_currency_choice]
        # La validación para asegurar que from_currency y to_currency sean diferentes se maneja en el método clean
    )
    cantidad_to = forms.FloatField(
        widget=forms.HiddenInput(), 
        required=False
    )
    calculate = forms.CharField(
        widget=forms.Button(attrs={'class': 'btn btn-primary'}), 
        required=False
    )
    submit = forms.CharField(
        widget=forms.HiddenInput(), 
        required=False
    )
    submit = forms.CharField(
        widget=forms.HiddenInput(), 
        required=False
    )

    # Método para la validación personalizada que involucra múltiples campos
    def clean(self):
        cleaned_data = super().clean()
        from_currency = cleaned_data.get("from_currency")
        to_currency = cleaned_data.get("to_currency")

        # Validación personalizada para asegurar que 'from_currency' y 'to_currency' sean diferentes
        if from_currency and to_currency and from_currency == to_currency:
            raise ValidationError("Los campos 'From' y 'To' deben ser diferentes.")

        return cleaned_data