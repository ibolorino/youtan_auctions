from django import forms

from youtan_auctions.auctions.models import Property, Auction, Vehicle

from datetime import datetime


class PropertyForm(forms.ModelForm):
    auction = forms.ModelChoiceField(
        queryset=Auction.objects.filter(date__gt=datetime.now().date()),
        label="Leilão"
    )
    images = forms.ImageField(label="Fotos")

    class Meta:
        model = Property
        fields = "__all__"
        exclude = ["bids"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({"placeholder": field.label})
        self.fields["images"].widget.attrs.update({"multiple": True})


class VehicleForm(forms.ModelForm):
    auction = forms.ModelChoiceField(
        queryset=Auction.objects.filter(date__gt=datetime.now().date()),
        label="Leilão"
    )
    images = forms.ImageField(label="Fotos")

    class Meta:
        model = Vehicle
        fields = "__all__"
        exclude = ["bids"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({"placeholder": field.label})
        self.fields["images"].widget.attrs.update({"multiple": True})
