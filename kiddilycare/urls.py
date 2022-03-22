from django.urls import path
from . import views


urlpatterns = [
    # Accueil
    path('', views.store, name = 'store'),
    path('about/', views.about, name = 'about'),
    path('pages/blog/', views.blog, name = 'blog'),
    path('pages/contact/', views.contact, name = 'contact'),
    path('pages/help_center/', views.help_center, name = 'help_center'),
    # path('Admin-Operations/addProduct/', views.addProduct, name = 'addProduct'),

    #Collections
    path('collections/', views.collections, name = 'collections'),
    path('collections/products/', views.products, name = 'products'),
    path('collections/products/visage', views.visage, name = 'visage'),
    path('collections/products/corps', views.corps, name = 'corps'),
    path('collections/products/pierresjade', views.jade, name = 'jade'),
    path('collections/products/ete', views.ete, name = 'ete'),
    path('collections/products/tendances', views.tendances, name = 'tendances'),
    path('collections/products/accessoires', views.accessoires, name = 'accessoires'),
    path('collections/products/beaute', views.beaute, name = 'beaute'),
    path('collections/products/sante', views.sante, name = 'sante'),

    # Process
    path('cart/', views.cart, name = 'cart'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('update_item/', views.updateItem, name = 'update_item'),
    path('process_order/', views.processOrder, name = 'process_order'),
    
    # Policies
    path('policies/terms-of-service/', views.terms_of_service, name = 'terms_of_service'),
    path('policies/privacy-policy/', views.privacy_policy, name = 'privacy_policy'),
    path('policies/shipping-policy/', views.shipping_policy, name = 'shipping_policy'),
    path('policies/refund-policy/', views.refund_policy, name = 'refund_policy'),

]