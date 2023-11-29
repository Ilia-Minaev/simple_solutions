import stripe

from typing import Any, Optional

from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView, View
#from django.views import View
from django.conf import settings
from django.http import HttpRequest, HttpResponse, JsonResponse

from .models import Items
 
stripe.api_key = settings.STRIPE_SECRET_KEY
 

class IndexView(ListView):
    model = Items
    template_name = "stripe_payments/index.html"
    context_object_name = 'items_list'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        #context[""] = 
        return context
    

class SingleItemView(DetailView):
    model = Items
    template_name = "stripe_payments/single_item.html"
    context_object_name = 'single_item'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["STRIPE_PUBLIC_KEY"] = settings.STRIPE_PUBLIC_KEY
        return context


class CreateCheckoutSession(View):
    def post(self, request, *args, **kwargs):

        item = Items.objects.get(pk=self.kwargs["pk"])
        domain = 'http://127.0.0.1:8000'
        if settings.DEBUG:
            domain = 'http://127.0.0.1:8000'

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": self.kwargs["pk"]
            },
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return JsonResponse({'id': checkout_session.id})


    
class SuccessView(TemplateView):
    template_name = "stripe_payments/success.html"


class CancelView(TemplateView):
    template_name = "stripe_payments/cancel.html"
    
