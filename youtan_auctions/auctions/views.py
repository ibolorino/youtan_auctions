from django.views.generic import TemplateView, DetailView
from .forms import AuctionForm
from .mixins import AdminMixin
from .models import Auction


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



home_page = HomePageView.as_view()
auctions_list_view = AuctionsListView.as_view()
auctions_create_view = CreateAuctionView.as_view()
auctions_update_view = UpdateAuctionView.as_view()

auctions_items_list_view = AuctionItemsListView.as_view()