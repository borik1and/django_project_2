from django import forms

from product_app.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'version_flag':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


    def get_active_version(self):
        return self.instance.version_set.filter(version_flag=True).first()

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if any(keyword in name.lower() for keyword in
               ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']):
            raise forms.ValidationError('Это слово или слова запрещены в названии продукта.')

        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')

        if any(keyword in description.lower() for keyword in
               ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']):
            raise forms.ValidationError('Это слово или слова запрещены в названии продукта.')

        return description


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
