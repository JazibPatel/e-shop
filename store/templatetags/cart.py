from django import template

register = template.Library()


@register.filter(name='cart_product')

# this function is use to check if product is in card or not
def cart_product(product, cart):
    # print("cart", cart)
    keys = cart.keys()
    for id in keys:
        # print("id",id)
        # if id == "null":
        #     continue
        if int(id) == product.id:
            # print("type check id",type(id))
            # print("type check p.id ",type(product.id))
            return True
    #     print("type check id",type(id))
    # print("type check p.id ",type(product.id))
    return False

@register.filter(name='cart_quantity')
# this function return number of product avalibal in cart
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name='total_product')
# this function return number of total product avalibal in cart
def total_product(product, cart):
    return product.price * cart_quantity(product, cart)

@register.filter(name='total_price')
# this function return number of total product avalibal in cart
def total_price(product, cart):
    sum = 0
    for prod in product:
        sum += total_product(prod, cart)
    return sum

@register.filter(name='order_price')
def order_price(product, cart):
    sum = 0
    for prod in product:
        sum += total_product(prod, cart)
        
    return sum*100

@register.filter(name='rs_symbol')
# this function use to display rs symbole 
def rs_symbol(symbol):
    return "₹ "+str(symbol)

@register.filter(name='myorder_total')
# this function use to display rs symbole 
def myorder_total(order_price, order_quantity):
    return order_price * order_quantity
