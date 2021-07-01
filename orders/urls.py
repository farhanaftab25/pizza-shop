from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("menu", views.menu, name="menu"),
    path("menu/<int:menu_id>", views.menu_dish, name="menu_dish"),
    path("menu/<int:category_id>/menuitem/<int:item_id>", views.menu_item, name="menu_item"),
    path("cart", views.cart, name="cart"),
    path("remove", views.remove_cart, name="remove_cart")
]
