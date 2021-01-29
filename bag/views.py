from django.shortcuts import render, reverse, redirect, HttpResponse
from django.contrib import messages


# Create your views here.

def view_bag(request):
    """ This view returns the shopping bag and its contents """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add one or more products to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    messages.success(
                    request, "Your bag has been successfully updated."
                )

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """Update item quantity in bag"""

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                    request, "Your bag has been successfully updated."
                )
        else:
            del bag[item_id]['items_by_size'][size]
            messages.success(
                    request, "The item has been removed from the bag"
                )

            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(
                    request, "The item has been removed from the bag"
                )

    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                    request, "Your bag has been successfully updated."
                )

        else:
            bag.pop(item_id)
            messages.success(
                    request, "The item has been removed from the bag"
                )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def delete_bag_item(request, item_id):
    """Remove item from the shopping bag"""

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(
                    request, "The item has been removed from your bag"
                )
        else:
            bag.pop(item_id)
            messages.success(
                    request, "The item has been removed from your bag"
                )

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))

    except Exception as e:
        messages.error(
                    request, "There was an error updating your bag."
                )
        return HttpResponse(status=500)
