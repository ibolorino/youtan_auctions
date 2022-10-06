from django import forms

from youtan_auctions.auctions.models import Bank


class BankForm(forms.ModelForm):

    class Meta:
        model = Bank
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({"placeholder": field.label})