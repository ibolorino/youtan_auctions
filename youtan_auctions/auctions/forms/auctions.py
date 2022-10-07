from django import forms

from youtan_auctions.auctions.models import Auction


class AuctionForm(forms.ModelForm):

    class Meta:
        model = Auction
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({"placeholder": field.label})
        self.fields['date'].widget.attrs.update({'placeholder': 'YYYY-MM-DD'})