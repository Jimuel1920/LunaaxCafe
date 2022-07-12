from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


app_name = 'backend'

urlpatterns =[


        path('', views.home2, name='home2'),
        path('accounts', views.accounts, name='accounts'),
        path('show', views.show, name='show'),
        path('ship', views.ship, name='ship' ),

    #login
        path('login', views.loginview, name='login'),
        path('login/Loginprocess', views.Loginprocess, name='Loginprocess'),
        path('logout', views.processlogout, name='logout'),

        path('add' , views.add, name='add'),
        path('Processadd', views.Processadd, name='Processadd'),
        path('isearch' , views.isearch, name='isearch'),

        path('products', views.productshow, name='products'),
        path('Productprocess', views.Productprocess, name='Productprocess'),
        path('Meatprocess', views.Meatprocess, name='Meatprocess'),


          # user updates show delete
        path('<int:user_id>/detail/', views.detail, name='detail'),
        path('<int:user_id>/deletes/', views.deletes, name='deletes'),
        path('<int:user_id>/edits/', views.edits, name='edits'),
        path('<int:user_id>/processedit/', views.proccessedit, name='processedit'),

        # meat update delete
         path('<int:meat_id>/mdetail/', views.mdetail, name='mdetail'),
         path('<int:meat_id>/mdelete/', views.mdelete, name='mdelete'),
         path('<int:meat_id>/medit/', views.medit, name='medit'),
         path('<int:meat_id>/mproccessedit/', views.mproccessedit, name='mproccessedit'),
         path('search', views.search, name='search'),

        # pancit update delete
         path('<int:pancit_id>/pdetails/', views.pdetails, name='pdetails'),
         path('<int:pancit_id>/pdelete/', views.pdelete, name='pdelete'),
         path('<int:pancit_id>/pedit/', views.pedit, name='pedit'),
         path('<int:pancit_id>/pproccessedit/', views.pproccessedit, name='pproccessedit'),
         path('psearch', views.psearch, name='psearch'),



        path('proccessing',views.procesingorders,name='proccessing'),
        path('food_orders',views.food_orders,name='food_orders'),
        path('meatpage', views.meatpage, name='meatpage') ,
        path('pancitpage', views.pancitpage, name='pancitpage') ,
        path('home', views.home, name='home'),


    #------------------------------ front end --------

         path('home2', views.home3, name='home2')



   ]  +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)



