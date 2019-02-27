from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
import json
# Create your views here.

#def scrapping(request):
#    context = {}
#    context['Products'] = SelectedProducts.objects.all()  
#    
#    return render(request,"index.html",context)


class DataCreate(APIView):

    def post(self,requests,*args, **kwargs):
        serializer = DataInfo(data=requests.data)
        if serializer.is_valid():
            price = Data(
                price = serializer.data['price']
            )
            price.save()
            return JsonResponse({'data':serializer.data})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
