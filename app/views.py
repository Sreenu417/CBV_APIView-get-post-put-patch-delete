from django.shortcuts import render

# Create your views here.
from app.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from app.serializers import *



class ProductCrud(APIView):
    def get(self,request,id):
        PQS=Product.objects.all()
        PJD=ProductSerializer(PQS,many=True)
        return Response(PJD.data)
    

    def post(self,request,id):
        PMSD=ProductSerializer(data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'message': ' product is created.format'})
        else:
            return Response({'Faile': 'product creation is failed'})

    def put(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        PMSD=ProductSerializer(PO,data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'message': 'Product is Updated' })
        else:
            return Response({'message': 'Product is Not Updated' })


    def patch(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        PO.pname=request.data['pname']
        PO.save()
        return Response({'Prtially Update':'Product is updated partially'})
    

    def delete(self,request,id):
        
        PO=Product.objects.get(id=id)
        PO.delete()
        return Response({'confirmation':'Deleted sucessfully'})
        
