from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_portfolio, name='portfolio'),
    path('<portfolio_id>', views.portfolio_details, name='portfolio_details'),
]
