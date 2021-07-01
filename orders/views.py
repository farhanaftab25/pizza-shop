from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Item, Size, ItemPrice, Topping, Order, Cart
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "orders/index.html")


def menu(request):
    category_list = Category.objects.all()
    first_category = category_list[0]
    items = first_category.items.all()
    context = {
        "categories": category_list,
        "category": category_list[0],
        "items": items
    }
    return render(request, "orders/menu.html", context)

def menu_dish(request, menu_id):
    try:
        category = Category.objects.get(pk=menu_id)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")
    context = {
        "categories": Category.objects.all(),
        "category": category,
        "items": category.items.all() 
    }
    return render(request, "orders/menu.html", context)
    
def menu_item(request, category_id, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    itemPrice = item.prices.all()
    first_item = itemPrice[0]
    context = {
        "item_id": item_id,
        "item": itemPrice,
        "first_item": first_item,
        "toppings": item.toppings.all(),
        "len_of_toppings": len(item.toppings.all())
    }
    return render(request, "orders/menu-item.html", context)

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        messages.success(request, 'Registration Successful!')
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "orders/register.html")

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("menu"))
        else:
            messages.error(request, 'Username or Password is incorrect!')
            return HttpResponseRedirect(reverse("login"))
    return render(request, "orders/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out.')
    return HttpResponseRedirect(reverse("login"))

def cart(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    user = request.user
    if request.method == "POST":
        try:
            item_id = int(request.POST["item_id"])
            item = Item.objects.get(pk=item_id)
        except KeyError:
            raise Http404("No item selected")
        except Item.DoesNotExist:
            raise Http404("No item")
        # toppings
        toppings = request.POST.getlist('toppings')
        toppings_price = len(toppings) * 0.5
        size = request.POST.get("size", 'none')
        quantity = request.POST["quantity"]
        price = None
        name = item.name
        item_price = item.prices.all()
        # size and price detemination
        for e in item_price:
            if e.size.name == size:
                price = e.price
            elif e.size.name == 'none':
                price = e.price
        # quantity
        quantity_with_price = round((int(quantity) * price) + toppings_price, 4)
        cart_item = Cart(name=name, quantity=quantity, size=size, price=quantity_with_price, user=user)
        cart_item.save()
        return HttpResponseRedirect(reverse('cart'))
    carts = user.carts.all()
    length_of_carts = len(carts)
    TOTAL = 0
    for item in carts:
        TOTAL = TOTAL + item.price
    context = {
        "carts": carts,
        "total": TOTAL,
        "length_of_cart": length_of_carts
    }
    return render(request, "orders/cart.html", context)

def remove_cart(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    user = request.user
    if request.method == "POST":
        total = request.POST["total"]
        items = request.POST["length"]
        order = Order(items=items, total=total, status=False, user=user)
        order.save()
        user.carts.all().delete()
        messages.success(request, 'Your order is on the way!')
        return HttpResponseRedirect(reverse("index"))
    return render(request, "orders/index.html")

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    user = request.user
    orders = user.orders.order_by('-id')
    context = {
        "user": request.user,
        "orders": orders
    }
    return render(request, "orders/home.html", context)