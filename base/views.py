from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product

"""
{
    "desc": "krembo",
    "price": 23.00,
    "cat_id": 1
  }
"""

@api_view(['GET','POST','DELETE','PUT'])
def products(request, id= -1):
    if request.method == 'GET':
        print(request)
        students = []
        for prod in Product.objects.all():
            students.append({"name":prod.desc,"price":prod.price,"catagory":prod.cat_id})
        return Response(students)
    elif request.method == 'POST':
        data = request.data
        prod = Product.objects.create(desc= data["desc"],price=data["price"],cat_id=data["cat_id"])
        return Response({"done":"success","prod added":prod.desc})
    
    elif request.method == 'DELETE':
        print("del")
        del_prod=Product.objects.filter(id=id)
        del_prod.delete()
        return Response({"done":"success", "removed":"done"})
        
    elif request.method == 'PUT':
        data =request.data
        upd_prod=Product.objects.filter(id=id)[0]
        upd_prod.desc=data["desc"]
        upd_prod.price=data["price"]
        upd_prod.cat_id=data["cat_id"]
        upd_prod.save()
        return Response({"done":"success","product updated":"done"})


# Create your views here.
