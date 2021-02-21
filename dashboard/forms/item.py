from django import forms
from store.models import Item

class ItemForm(forms.ModelForm):
    # name = forms.CharField()
    # price = forms.FloatField()
    # quantity = forms.IntegerField()
    # description = forms.CharField()
    # category = forms.ModelChoiceField(queryset=Category.get_all_categories())
    # image = forms.ImageField()
    class Meta:
        model = Item
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs = {'rows': 3}