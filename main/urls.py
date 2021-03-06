from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
                  path('store', views.store, name="store"),
                  path('cart/', views.cart, name="cart"),
                  path('checkout/', views.checkout, name="checkout"),

                  path('update_item/', views.updateItem, name="update_item"),
                  path('process_order/', views.processOrder, name="process_order"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
