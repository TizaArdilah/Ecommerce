from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Order, Product
from .models import CustomUser
from .forms import ProductForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.utils import timezone


def is_admin(user):
    return user.is_staff  # Atau gunakan atribut lain jika sesuai


@login_required
def manage_products(request):
    products = Product.objects.all()
    return render(request, "store/manage_products.html", {"products": products})


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("manage_products")
    else:
        form = ProductForm()
    return render(request, "store/add_product.html", {"form": form})


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("manage_products")
    else:
        form = ProductForm(instance=product)
    return render(
        request, "store/edit_product.html", {"form": form, "product": product}
    )


@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect("manage_products")
    return render(request, "store/delete_product.html", {"product": product})


@login_required
def add_to_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Simpan langsung ke dalam database order (Contoh sederhana)
    request.user.orders.create(product=product, quantity=1)

    # Redirect ke halaman shop setelah menambahkan
    return redirect("shop")


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.user.is_authenticated and getattr(request.user, "is_admin", False):
        return redirect("admin_dashboard")
    return render(request, "store/home.html")


@login_required
def admin_dashboard(request):
    products = Product.objects.all()
    return render(request, "store/admin_dashboard.html", {"products": products})


def shop(request):
    products = Product.objects.all()
    return render(request, "store/shop.html", {"products": products})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect ke halaman utama setelah login
        else:
            return render(request, "store/login.html", {"error": "Invalid credentials"})
    return render(request, "store/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")  # Redirect ke halaman login setelah logout


# Register


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
    return render(request, "store/login.html")


from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import CustomUserCreationForm

CustomUser = get_user_model()

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Transaction


from store.models import Product, Transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime


# def buy_product(request, product_id):
#     # Ensure product is fetched using get_object_or_404 to prevent errors when product is not found
#     product = get_object_or_404(Product, id=product_id)

#     if request.method == "POST":
#         # Ensure 'quantity' is passed in the form
#         quantity = request.POST.get("quantity")

#         if not quantity or int(quantity) <= 0:
#             messages.error(request, "Please provide a valid quantity.")
#             return redirect("shop")  # or a relevant redirect destination

#         # Calculate the total price
#         total_price = product.price * int(quantity)

#         # Create the transaction object
#         transaction = Transaction.objects.create(
#             user=request.user,
#             amount=total_price,
#             transaction_date=datetime.now(),
#         )

#         # Optionally, store the product and quantity in the transaction if needed
#         # transaction.products.add(product)  # if you use a many-to-many relationship for products

#         # Redirect to success or confirmation page
#         messages.success(
#             request,
#             f"Your purchase of {quantity} {product.name}(s) has been successful!",
#         )
#         return redirect("success")  # or redirect to the shop or cart page

#     return render(request, "store/buy_product.html", {"product": product})


# def buy_product(request, product_id):
#     if request.method == "POST":
#         product = Product.objects.get(id=product_id)

#         # Ensure the user is logged in
#         if request.user.is_authenticated:
#             # Create a transaction for the logged-in user
#             transaction = Transaction.objects.create(
#                 user=request.user,  # Set the user to the logged-in user
#                 amount=product.price,
#                 transaction_date=timezone.now(),
#             )
#             # Optionally, add more logic (e.g., payment processing)

#             # Redirect to success page after the transaction
#             return redirect("success")
#         else:
#             return redirect("login")  # Redirect to login if not authenticated
#     else:
#         product = Product.objects.get(id=product_id)
#         return render(request, "store/buy_product.html", {"product": product})


# def buy_product(request, product_id):
#     if request.method == "POST":
#         # Assuming you have a `Product` object fetched by the `product_id`
#         product = Product.objects.get(id=product_id)
#         amount = product.price  # Example for product price
#         user_id = request.user.id  # Get user_id from the logged-in user

#         # Create a new transaction entry
#         transaction = Transaction.objects.create(
#             user_id=user_id, amount=amount, transaction_date=timezone.now()
#         )

#         # Redirect or show success message
#         return redirect("success")  # Redirect to a success page after the transaction


# @login_required
# def buy_product(request, product_id):
#     if request.method == "POST":
#         # Assuming you have a Product object fetched by the product_id
#         product = Product.objects.get(id=product_id)
#         amount = product.price  # Example for product price

#         # Get the user_id directly from request.user
#         user_id = request.user.id  # This gets the ID of the logged-in user

#         # Create a new transaction entry
#         transaction = Transaction.objects.create(
#             user_id=user_id,  # Correctly store the user_id
#             amount=amount,
#             transaction_date=timezone.now(),
#         )

#         # Redirect or show success message
#         return redirect("success")  # Redirect to a success page after the transaction
#     else:
#         # Handle GET request if needed (for example, rendering a buy page)
#         return render(request, "store/buy_product.html")


from django.shortcuts import redirect, render
from django.utils import timezone
from store.models import Transaction, Product
from django.contrib.auth.decorators import login_required


# @login_required
# def buy_product(request, product_id):
#     if request.method == "POST":
#         # Get the product object by its ID
#         product = Product.objects.get(id=product_id)
#         amount = product.price  # Example: product price

#         # Get the user object directly
#         user = request.user  # The full user object

#         # Create a new transaction entry using the user object
#         transaction = Transaction.objects.create(
#             user=user,  # Use the user object, not user_id
#             amount=amount,
#             transaction_date=timezone.now(),
#         )

#         # Redirect to success page or another page after transaction
#         return redirect("success")  # Redirect to a success page after the transaction
#     else:
#         # Handle GET request (if needed, such as showing a confirmation page)
#         return render(request, "store/buy_product.html")


@login_required
def buy_product(request, product_id):
    if request.method == "POST":
        # Get the product object by its ID
        product = Product.objects.get(id=product_id)
        amount = product.price  # Example: product price

        # Get the user object directly
        user = request.user  # The full user object

        # Create a new transaction entry using the user ID (not the full user object)
        transaction = Transaction.objects.create(
            user=user.id,  # Use the user ID explicitly, not the whole user object
            amount=amount,
            transaction_date=timezone.now(),
        )

        # Redirect to success page or another page after transaction
        return redirect("success")  # Redirect to a success page after the transaction
    else:
        # Handle GET request (if needed, such as showing a confirmation page)
        return render(request, "store/buy_product.html")


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Simpan pengguna ke database
            user = form.save()
            messages.success(request, "Registrasi berhasil! Anda dapat login sekarang.")
            return redirect("login")  # Redirect ke halaman login
        else:
            messages.error(request, "Terjadi kesalahan. Mohon periksa form Anda.")
    else:
        form = CustomUserCreationForm()
    return render(request, "store/register.html", {"form": form})


# Logout
def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def checkout_view(request):
    if request.method == "POST":
        # Ambil semua produk dari sesi atau input langsung
        order_items = request.POST.getlist(
            "product_ids"
        )  # Asumsikan ini daftar ID produk
        total_price = 0

        # Loop untuk menghitung total harga berdasarkan produk yang dipilih
        for product_id in order_items:
            try:
                product = Product.objects.get(id=product_id)
                total_price += product.price
            except Product.DoesNotExist:
                messages.error(
                    request, f"Produk dengan ID {product_id} tidak ditemukan."
                )
                return redirect("shop")

        # Buat pesanan baru
        Order.objects.create(
            user=request.user,
            total_price=total_price,
        )

        messages.success(request, "Order placed successfully!")
        return redirect("shop")

    # Jika GET request, tampilkan halaman checkout
    return render(request, "store/checkout.html")


def success_view(request):
    return render(request, "store/success.html")
