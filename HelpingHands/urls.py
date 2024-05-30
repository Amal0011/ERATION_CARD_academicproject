"""HelpingHands URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginPage),
    path('AdminHome/', AdminHome, name='AdminHome'),
    path('Regshop/',Regshop, name='Regshop'),
    path('Add_to_stock/',Add_to_stock, name='Add_to_stock'),
    path('SaveStore/',SaveStore, name='SaveStore'),
    path('Addstock/',Addstock, name='Addstock'),
    path('View_stock/',View_stock, name='View_stock'),
    path('Get_stock/',Get_stock, name='Get_stock'),
    path('Update_stock/',Update_stock, name='Update_stock'),
    path('Shop_stock/',Shop_stock, name='Shop_stock'),
    path('View_stores/',View_stores, name='View_stores'),
    path('Get_my_shops/',Get_my_shops, name='Get_my_shops'),
    path('Get_shop_id/',Get_shop_id, name='Get_shop_id'),
    path('Selected_shop/',Selected_shop, name='Selected_shop'),
    path('Buy_ration/',Buy_ration, name='Buy_ration'),
    path('Save_my_ration/',Save_my_ration, name='Save_my_ration'),
    path('Bill_page/',Bill_page, name='Bill_page'),
    path('Pcode/',Pcode, name='Pcode'),
    path('Customer_history/',Customer_history, name='Customer_history'),
    path('Shop_receive_orders/',Shop_receive_orders, name='Shop_receive_orders'),
    path('Accept_order/',Accept_order, name='Accept_order'),
    path('Shop_all_orders/',Shop_all_orders, name='Shop_all_orders'),
    path('Add_rating/',Add_rating, name='Add_rating'),
    path('Admin_view_history/',Admin_view_history, name='Admin_view_history'),
    path('Andro_SaveStore/',Andro_SaveStore, name='Andro_SaveStore'),
    path('Andro_Savecustomer/',Andro_Savecustomer, name='Andro_Savecustomer'),
    path('Andro_CheckLogin/',Andro_CheckLogin, name='Andro_CheckLogin'),
    path('Andro_admin_view_store/',Andro_admin_view_store, name='Andro_admin_view_store'),
    path('Andro_UpdateShopuser/',Andro_UpdateShopuser, name='Andro_UpdateShopuser'),
    path('Andro_DeleteShopuser/',Andro_DeleteShopuser, name='Andro_DeleteShopuser'),
    path('Andro_Addstock/',Andro_Addstock, name='Andro_Addstock'),
    path('Andro_Get_stock/',Andro_Get_stock, name='Andro_Get_stock'),
    path('Android_Update_stock/',Android_Update_stock, name='Android_Update_stock'),
    path('Andro_admin_view_history/',Andro_admin_view_history, name='Andro_admin_view_history'),
    path('Andro_shop_view_quota/',Andro_shop_view_quota, name='Andro_shop_view_quota'),
    path('Andro_shop_sell_ration/',Andro_shop_sell_ration, name='Andro_shop_sell_ration'),
    path('Andro_approve_ration/',Andro_approve_ration, name='Andro_approve_ration'),
    path('Andro_shop_view_history/',Andro_shop_view_history, name='Andro_shop_view_history'),
    path('Andro_user_list_shop/',Andro_user_list_shop, name='Andro_user_list_shop'),
    path('Andro_get_user_ration/',Andro_get_user_ration, name='Andro_get_user_ration'),
    path('Andro_buy_product/',Andro_buy_product, name='Andro_buy_product'),
    path('Android_add_rating/',Android_add_rating, name='Android_add_rating'),
    path('Andro_user_view_history/',Andro_user_view_history, name='Andro_user_view_history'),
    path('Newindex/',Newindex, name='Newindex'),
















    path('Regauto/',Regauto, name='Regauto'),
    path('Saveauto/',Saveauto, name='Saveauto'),
    path('LoginPage/',LoginPage, name='LoginPage'),
    path('Regcustomer/',Regcustomer, name='Regcustomer'),
    path('Savecustomer/',Savecustomer, name='Savecustomer'),
    path('Adminviewstore/',Adminviewstore, name='Adminviewstore'),
    path('Approvestore/',Approvestore, name='Approvestore'),
    path('UpdateShopuser/',UpdateShopuser, name='UpdateShopuser'),
    path('DeleteShopuser/',DeleteShopuser, name='DeleteShopuser'),
    path('Approveauto/',Approveauto, name='Approveauto'),
    path('Adminviewauto/',Adminviewauto, name='Adminviewauto'),
    path('Updateauto/',Updateauto, name='Updateauto'),
    path('Deleteauto/',Deleteauto, name='Deleteauto'),
    path('Admin_add_cat/',Admin_add_cat, name='Admin_add_cat'),
    path('add_cat/',add_cat, name='add_cat'),
    path('Admin_add_Subcat/',Admin_add_Subcat, name='Admin_add_Subcat'),
    path('add_Subcat/',add_Subcat, name='add_Subcat'),
    path('Shophome/',Shophome, name='Shophome'),
    path('Add_items/',Add_items, name='Add_items'),
    path('get_sub_cat/',get_sub_cat, name='get_sub_cat'),
    path('upload_item/',upload_item, name='upload_item'),
    path('View_items/',View_items, name='View_items'),
    path('Get_products/',Get_products, name='Get_products'),
    path('Autohome/',Autohome, name='Autohome'),
    path('update_item/',update_item, name='update_item'),
    path('updatelocation/',updatelocation, name='updatelocation'),
    path('Customerhome/',Customerhome, name='Customerhome'),
    path('Customershop/',Customershop, name='Customershop'),
    path('Electronics_hone/',Electronics_hone, name='Electronics_hone'),
    path('addtocart/',addtocart, name='addtocart'),
    path('Dress_home/',Dress_home, name='Dress_home'),
    path('Food_home/',Food_home, name='Food_home'),
    path('Footwear_home/',Footwear_home, name='Footwear_home'),
    path('Cart_page/',Cart_page, name='Cart_page'),
    path('Grocery_home/',Grocery_home, name='Grocery_home'),
    path('payment_page/',payment_page, name='payment_page'),
    path('delete_cart/',delete_cart, name='delete_cart'),
    path('buy_product/',buy_product, name='buy_product'),
    path('My_orders/',My_orders, name='My_orders'),
    path('add_auto/',add_auto, name='add_auto'),
    path('View_near_auto/',View_near_auto, name='View_near_auto'),
    path('add_auto_notify/',add_auto_notify, name='add_auto_notify'),
    path('my_notification/',my_notification, name='my_notification'),
    path('accept_request/',accept_request, name='accept_request'),
    path('auto_delivery/',auto_delivery, name='auto_delivery'),
    path('complete_order/',complete_order, name='complete_order'),
    path('Bot_response/',Bot_response, name='Bot_response'),
    
    path('CheckLogin/',CheckLogin, name='CheckLogin'),

    







]
