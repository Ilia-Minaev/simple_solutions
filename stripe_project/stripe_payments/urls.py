
from django.urls import path, include
from .views import IndexView, SingleItemView, CreateCheckoutSession, CancelView, SuccessView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('item/<int:pk>/', SingleItemView.as_view(), name='single_item'),
    path('buy/<int:pk>/', CreateCheckoutSession.as_view(), name='create-checkout-session'),

    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    
]
