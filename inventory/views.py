from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Item, Customer, Supplier, Purchase, Sale, SaleItem, PurchaseItem

# CATEGORIES
@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = [{'id': c.id, 'name': c.name, 'description': c.description} for c in categories]
        return Response(data)
    
    elif request.method == 'POST':
        name = request.data.get('name')
        description = request.data.get('description', '')
        
        if not name:
            return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        category = Category.objects.create(name=name, description=description)
        return Response({'id': category.id, 'name': category.name, 'message': 'Category created'}, 
                       status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return Response({'id': category.id, 'name': category.name, 'description': category.description})
    
    elif request.method == 'PUT':
        category.name = request.data.get('name', category.name)
        category.description = request.data.get('description', category.description)
        category.save()
        return Response({'message': 'Category updated'})
    
    elif request.method == 'DELETE':
        category.delete()
        return Response({'message': 'Category deleted'}, status=status.HTTP_204_NO_CONTENT)

# ITEMS
@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        items = Item.objects.all()
        data = []
        for item in items:
            data.append({
                'id': item.id,
                'name': item.name,
                'category': item.category.name if item.category else None,
                'stock_quantity': item.stock_quantity
            })
        return Response(data)
    
    elif request.method == 'POST':
        name = request.data.get('name')
        category_id = request.data.get('category_id')
        stock_quantity = request.data.get('stock_quantity', 0)
        
        if not name:
            return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        category = None
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                return Response({'error': 'Category not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        item = Item.objects.create(
            name=name,
            category=category,
            stock_quantity=stock_quantity
        )
        return Response({
            'id': item.id,
            'name': item.name,
            'stock_quantity': item.stock_quantity,
            'message': 'Item created'
        }, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    try:
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return Response({
            'id': item.id,
            'name': item.name,
            'category': item.category.name if item.category else None,
            'stock_quantity': item.stock_quantity
        })
    
    elif request.method == 'PUT':
        item.name = request.data.get('name', item.name)
        item.stock_quantity = request.data.get('stock_quantity', item.stock_quantity)
        
        category_id = request.data.get('category_id')
        if category_id:
            try:
                item.category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                return Response({'error': 'Category not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        item.save()
        return Response({'message': 'Item updated'})
    
    elif request.method == 'DELETE':
        item.delete()
        return Response({'message': 'Item deleted'}, status=status.HTTP_204_NO_CONTENT)

# CUSTOMERS
@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        data = []
        for customer in customers:
            data.append({
                'id': customer.id,
                'name': customer.name,
                'email': customer.email,
                'phone': customer.phone,
                'city': customer.city
            })
        return Response(data)
    
    elif request.method == 'POST':
        name = request.data.get('name')
        email = request.data.get('email', '')
        phone = request.data.get('phone', '')
        city = request.data.get('city', '')
        gender = request.data.get('gender', '')
        
        if not name:
            return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        customer = Customer.objects.create(
            name=name,
            email=email,
            phone=phone,
            city=city,
            gender=gender
        )
        return Response({
            'id': customer.id,
            'name': customer.name,
            'email': customer.email,
            'message': 'Customer created'
        }, status=status.HTTP_201_CREATED)

# SIMPLE SALE CREATION
@api_view(['POST'])
def create_sale(request):
    customer_id = request.data.get('customer_id')
    items = request.data.get('items', [])  # List of {item_id, quantity, selling_price}
    
    if not customer_id or not items:
        return Response({'error': 'customer_id and items are required'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create sale
    sale = Sale.objects.create(customer=customer)
    
    # Add sale items
    for item_data in items:
        try:
            item = Item.objects.get(id=item_data['item_id'])
            SaleItem.objects.create(
                sale=sale,
                item=item,
                quantity=item_data['quantity'],
                selling_price=item_data['selling_price']
            )
        except Item.DoesNotExist:
            return Response({'error': f"Item {item_data['item_id']} not found"}, 
                           status=status.HTTP_400_BAD_REQUEST)
    
    return Response({
        'sale_id': sale.id,
        'customer': customer.name,
        'sale_date': sale.sale_date,
        'message': 'Sale created successfully'
    }, status=status.HTTP_201_CREATED)
# SUPPLIERS
@api_view(['GET', 'POST'])
def supplier_list(request):
    if request.method == 'GET':
        suppliers = Supplier.objects.all()
        data = []
        for supplier in suppliers:
            data.append({
                'id': supplier.id,
                'name': supplier.name,
                'email': supplier.email,
                'phone': supplier.phone
            })
        return Response(data)
    
    elif request.method == 'POST':
        name = request.data.get('name')
        email = request.data.get('email', '')
        phone = request.data.get('phone', '')
        
        if not name:
            return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        supplier = Supplier.objects.create(
            name=name,
            email=email,
            phone=phone
        )
        return Response({
            'id': supplier.id,
            'name': supplier.name,
            'email': supplier.email,
            'message': 'Supplier created'
        }, status=status.HTTP_201_CREATED)

# PURCHASES
@api_view(['GET', 'POST'])
def purchase_list(request):
    if request.method == 'GET':
        purchases = Purchase.objects.all()
        data = []
        for purchase in purchases:
            data.append({
                'id': purchase.id,
                'supplier': purchase.supplier.name,
                'purchase_date': purchase.purchase_date,
                'items_count': purchase.items.count()
            })
        return Response(data)
    
    elif request.method == 'POST':
        supplier_id = request.data.get('supplier_id')
        items = request.data.get('items', [])  # List of {item_id, quantity, buying_price}
        
        if not supplier_id or not items:
            return Response({'error': 'supplier_id and items are required'}, 
                           status=status.HTTP_400_BAD_REQUEST)
        
        try:
            supplier = Supplier.objects.get(id=supplier_id)
        except Supplier.DoesNotExist:
            return Response({'error': 'Supplier not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create purchase
        purchase = Purchase.objects.create(supplier=supplier)
        
        # Add purchase items and update stock
        for item_data in items:
            try:
                item = Item.objects.get(id=item_data['item_id'])
                PurchaseItem.objects.create(
                    purchase=purchase,
                    item=item,
                    quantity=item_data['quantity'],
                    buying_price=item_data['buying_price']
                )
                # Update stock quantity
                item.stock_quantity += item_data['quantity']
                item.save()
            except Item.DoesNotExist:
                return Response({'error': f"Item {item_data['item_id']} not found"}, 
                               status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'purchase_id': purchase.id,
            'supplier': supplier.name,
            'purchase_date': purchase.purchase_date,
            'message': 'Purchase created successfully'
        }, status=status.HTTP_201_CREATED)