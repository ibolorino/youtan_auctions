from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AuctionForm, PropertyForm, VehicleForm, BankForm
from .mixins import AdminMixin
from .models import Auction, Property, Vehicle, Bank


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AuctionsListView(LoginRequiredMixin, TemplateView):
    template_name = "auctions/list_auctions.html"


class AuctionCreateView(AdminMixin, TemplateView):
    template_name = "auctions/create_auction.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuctionForm()
        return context


class AuctionUpdateView(AdminMixin, DetailView):
    template_name = "auctions/update_auction.html"
    model = Auction

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['form'] = AuctionForm(instance=instance)
        context['object_id'] = instance.id
        return context


class AuctionItemsListView(LoginRequiredMixin, DetailView):
    template_name = "auctions/list_auction_items.html"
    model = Auction
    context_object_name = "auction"


class AllItemsListView(LoginRequiredMixin, TemplateView):
    template_name = "auctions/list_all_items.html"


class PropertyCreateView(AdminMixin, TemplateView):
    template_name = "auctions/create_property.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PropertyForm()
        return context


class PropertyDetailViel(LoginRequiredMixin, DetailView):
    template_name = "auctions/property_detail.html"
    model = Property
    context_object_name = "property"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context["images"] = instance.propertyimages_set.all()
        return context


class PropertyUpdateView(AdminMixin, DetailView):
    template_name = "auctions/update_item.html"
    model = Property

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['form'] = PropertyForm(instance=instance)
        context['item_type'] = 'properties'
        context['object_id'] = instance.id
        context["images"] = instance.propertyimages_set.all()
        return context


class VehicleCreateView(AdminMixin, TemplateView):
    template_name = "auctions/create_vehicle.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VehicleForm()
        return context


class VehicleDetailViel(LoginRequiredMixin, DetailView):
    template_name = "auctions/vehicle_detail.html"
    model = Vehicle
    context_object_name = "vehicle"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context["images"] = instance.vehicleimages_set.all()
        return context


class VehicleUpdateView(AdminMixin, DetailView):
    template_name = "auctions/update_item.html"
    model = Vehicle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['form'] = VehicleForm(instance=instance)
        context['item_type'] = 'vehicles'
        context['object_id'] = instance.id
        context["images"] = instance.vehicleimages_set.all()
        return context


class BankCreateView(AdminMixin, TemplateView):
    template_name = "auctions/create_bank.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BankForm()
        return context

class BankUpdateView(AdminMixin, DetailView):
    template_name = "auctions/update_bank.html"
    model = Bank

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['form'] = BankForm(instance=instance)
        context['object_id'] = instance.id
        return context


class BankListView(AdminMixin, TemplateView):
    template_name = "auctions/list_banks.html"


home_page = HomePageView.as_view()
auctions_list_view = AuctionsListView.as_view()
auctions_create_view = AuctionCreateView.as_view()
auctions_update_view = AuctionUpdateView.as_view()

auctions_items_list_view = AuctionItemsListView.as_view()
all_items_list_view = AllItemsListView.as_view()
property_detail_view = PropertyDetailViel.as_view()
property_create_view = PropertyCreateView.as_view()
property_update_view = PropertyUpdateView.as_view()
vehicle_detail_view = VehicleDetailViel.as_view()
vehicle_create_view = VehicleCreateView.as_view()
vehicle_update_view = VehicleUpdateView.as_view()

bank_create_view = BankCreateView.as_view()
bank_list_view = BankListView.as_view()
bank_update_view = BankUpdateView.as_view()