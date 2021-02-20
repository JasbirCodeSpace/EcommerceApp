from django import forms
from store.models import Item
from store.models import Category

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

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'