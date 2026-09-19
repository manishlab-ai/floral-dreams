from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, Login, Category, Product, ShoppingCart, Orders

def index(request):
    pro = Product.get_all_products()
    cats = Category.get_all_category()
    categoryID = request.GET.get('category')
    if categoryID:
        pro = Product.get_products_by_categoryid(categoryID)
    else:
        pro = Product.get_all_products()
    data = {}
    data['pro'] = pro
    data['cats'] = cats
    return render(request, 'index.html', data)

def productPage(request):
    pid = request.GET.get('pid')
    product = Product.get_product_by_id(pid)
    data = {'product': product}
    return render(request, 'product.html', data)

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        postData = request.POST
        name = postData.get('name')
        gender = postData.get('gender')
        address = postData.get('address')
        pincode = postData.get('pincode')
        contactno = postData.get('contactno')
        emailaddress = postData.get('emailaddress')
        password = postData.get('password')
        
        customer = Customer(name=name, gender=gender, address=address, pincode=pincode, contactno=contactno, emailaddress=emailaddress, password=password)
        login = Login(userid=emailaddress, password=password, usertype='user')
        
        if customer.is_exists():
            return render(request, 'register.html', {'error': 'Email Address Already Registered...'})
        else:
            customer.save()
            login.save()
            return render(request, 'register.html', {'msg': 'Registration Successful...'})

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Login.objects.get(userid=email, password=password)
            if user is not None:
                request.session['email'] = email
                return redirect('user')
        except Login.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid User ID or Password'})

def user(request):
    if request.session.has_key('email'):
        email = request.session['email']
        customer = Customer.get_customer_by_email(email)
        pro = Product.get_all_products()
        cats = Category.get_all_category()
        categoryID = request.GET.get('category')
        if categoryID:
            pro = Product.get_products_by_categoryid(categoryID)
        else:
            pro = Product.get_all_products()
        data = {'pro': pro, 'cats': cats, 'customer': customer}
        return render(request, 'user.html', data)
    else:
        return redirect('signin')

def orders(request):
    if request.session.has_key('email'):
        email = request.session['email']
        customer = Customer.get_customer_by_email(email)
        order_list = Orders.objects.filter(customer=customer)
        return render(request, 'orders.html', {'customer': customer, 'orders': order_list})
    else:
        return redirect('signin')

def buynow(request):
    if request.session.has_key('email'):
        pid = request.GET.get('pid')
        product = Product.get_product_by_id(pid)
        email = request.session['email']
        customer = Customer.get_customer_by_email(email)
        return render(request, 'confirm.html', {'product': product, 'customer': customer})
    else:
        return redirect('signin')

def checkout(request):
    if request.method == 'POST':
        email = request.session['email']
        customer = Customer.get_customer_by_email(email)
        pid = request.POST.get('pid')
        product = Product.get_product_by_id(pid)
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        quantity = request.POST.get('quantity')
        price = product.price
        
        order = Orders(customer=customer, product=product, price=price, address=address, pincode=pincode, quantity=quantity)
        order.save()
        return redirect('orders')

def mycart(request):
    if request.session.has_key('email'):
        email = request.session['email']
        customer = Customer.get_customer_by_email(email)
        cart_items = ShoppingCart.objects.filter(customer=customer)
        return render(request, 'mycart.html', {'customer': customer, 'cart_items': cart_items})
    else:
        return redirect('signin')

def update_cart(request):
    if request.method == 'POST':
        email = request.session['email']
        customer = Customer.get_customer_by_email(email)
        pid = request.POST.get('pid')
        product = Product.get_product_by_id(pid)
        qty = int(request.POST.get('quantity'))
        
        cart_item, created = ShoppingCart.objects.get_or_create(customer=customer, product=product, defaults={'quantity': qty})
        if not created:
            cart_item.quantity += qty
            cart_item.save()
        return redirect('mycart')
