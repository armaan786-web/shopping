

from django.urls import path
from django.contrib.auth import views as auth_views
from shopping_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path("",views.signin,name="signin"),
    path('logout/',auth_views.LogoutView.as_view(next_page='signin'),name="logout"),
    path("signup/",views.signup,name="signup"),
    path("otp/",views.otp,name="otp"),
    path("dashboard",views.home,name="home"),
    path("prducts/",views.product,name="product"),
    path("prducts/detail/<int:id>",views.product_detail,name="product_detail"),
    path("wallet/",views.wallet,name="wallet"),
    path("profile/",views.profile,name="profile"),



    # -------------------Recharge Url -----------------------
    path("recharge/",views.recharge,name="recharge"),
    path("recharge/history",views.recharge_history,name="recharge_history"),


    # -----------------------Withdraw Url----------------------------
    path("withdraw/transaction",views.withdraw_transaction,name="withdraw_transaction"),


    # --------------------------- Orders Url ---------------------

    path("orders",views.myorder,name="myorder"),




    # ------------------------ Booking Url -------------------
    path("booking/",views.booking,name="booking"),
    

    # ------------------------ Kyc Url -------------------
    path("Kyc/",views.kyc,name="kyc"),
    

    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
