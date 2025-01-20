from django.shortcuts import render, redirect, get_object_or_404
from .models import Bill, BillDetail, Product

def billing(request):
    if request.method == 'POST':
        # Crear la factura
        bill = Bill.objects.create()

        # Leer los detalles enviados desde el formulario
        details = request.POST.getlist('products')
        quantities = request.POST.getlist('quantities')

        for product_id, quantity in zip(details, quantities):
            product = Product.objects.get(id=product_id)
            BillDetail.objects.create(bill=bill, product=product, quantity=int(quantity))

        return redirect('show_bill', bill_id=bill.id)

    # Obtener todos los productos
    products = Product.objects.all()
    return render(request, 'management_views/billing.html', {'products': products})


def show_bill(request, bill_id):
    # Obtener la factura específica
    bill = Bill.objects.get(id=bill_id)
    total = sum(detail.subtotal for detail in bill.details.all())  # Calcula el total
    return render(request, 'management_views/show_Bill.html', {'bill': bill, 'total': total})
