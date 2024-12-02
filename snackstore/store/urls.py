from django.urls import path
from . import views
from .views import register_view, login_view

urlpatterns = [
    path("", views.home, name="home"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("manage-products/", views.manage_products, name="manage_products"),
    path("add-product/", views.add_product, name="add_product"),
    path("edit-product/<int:product_id>/", views.edit_product, name="edit_product"),
    path(
        "delete-product/<int:product_id>/", views.delete_product, name="delete_product"
    ),
    path("shop/", views.shop, name="shop"),
    path("add-to-order/<int:product_id>/", views.add_to_order, name="add_to_order"),
    path("logout/", views.logout_view, name="logout"),
    path("checkout/", views.checkout_view, name="checkout"),
    path("buy/<int:product_id>/", views.buy_product, name="buy_product"),
    path("success/", views.success_view, name="success"),  # Define 'success' URL
]
