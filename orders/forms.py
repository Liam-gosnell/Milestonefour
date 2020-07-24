from django import forms
from .widgets import CustomClearableFileInput
from .models import Item, ItemTag


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'


    image = forms.ImageField(label='Image', required=True, widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        itemtags = ItemTag.objects.all()

        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-3'