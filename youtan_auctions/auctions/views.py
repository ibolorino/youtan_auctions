from django.views.generic import TemplateView, DetailView
from .forms import AuctionForm, PropertyForm, VehicleForm
from .mixins import AdminMixin
from .models import Auction, Property, Vehicle


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AuctionsListView(TemplateView):
    template_name = "auctions/list_auctions.html"


class CreateAuctionView(AdminMixin, TemplateView):
    template_name = "auctions/create_auction.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuctionForm()
        return context


class UpdateAuctionView(AdminMixin, DetailView):
    template_name = "auctions/update_auction.html"
    model = Auction

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['form'] = AuctionForm(instance=instance)
        context['object_id'] = instance.id
        return context


class AuctionItemsListView(DetailView):
    template_name = "auctions/list_auction_items.html"
    model = Auction
    context_object_name = "auction"


class AllItemsListView(TemplateView):
    template_name = "auctions/list_all_items.html"


class CreatePropertyView(AdminMixin, TemplateView):
    template_name = "auctions/create_property.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PropertyForm()
        return context


class PropertyDetailViel(DetailView):
    template_name = "auctions/property_detail.html"
    model = Property
    context_object_name = "property"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context["images"] = instance.propertyimages_set.all()
        return context


class UpdatePropertyView(AdminMixin, DetailView):
    template_name = "auctions/update_item.html"
    model = Property

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['form'] = PropertyForm(instance=instance)
        context['item_type'] = 'properties'
        context['object_id'] = instance.id
        return context


class CreateVehicleView(AdminMixin, TemplateView):
    template_name = "auctions/create_vehicle.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VehicleForm()
        return context


class UpdateVehicleView(AdminMixin, DetailView):
    template_name = "auctions/update_item.html"
    model = Vehicle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['form'] = VehicleForm(instance=instance)
        context['item_type'] = 'vehicles'
        context['object_id'] = instance.id
        return context



home_page = HomePageView.as_view()
auctions_list_view = AuctionsListView.as_view()
auctions_create_view = CreateAuctionView.as_view()
auctions_update_view = UpdateAuctionView.as_view()

auctions_items_list_view = AuctionItemsListView.as_view()
all_items_list_view = AllItemsListView.as_view()
property_detail_view = PropertyDetailViel.as_view()
property_create_view = CreatePropertyView.as_view()
property_update_view = UpdatePropertyView.as_view()
vehicle_create_view = CreateVehicleView.as_view()
vehicle_update_view = UpdateVehicleView.as_view()