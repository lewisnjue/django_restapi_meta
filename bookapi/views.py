from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['post','GET']) # inside the bracket specify the  
# methods that are allowed 
def books(request):
    return Response('list of books ',status=status.HTTP_200_OK)
# by default the method allowed is get 
# the api_view decorator also allow you to imprement throttling 
# and or rate limiting 
# lets see the same with class based view 
from rest_framework.views import APIView # -> in order 
#to use class based views

class BookList(APIView):
    def get(self,request):
        author = request.GET.get('author')
        if (author):
            return Response({'messange':'ist of books by '+ author},status.HTTP_200_OK)
        #-> the above is if there is a parameter called author 
        return Response({'message':'lis of the books'},status.HTTP_200_OK)
    def post(self,request):
        return Response({'message':'new book created'},status.HTTP_200_OK)
    
class Book(APIView):
    def get(self,request,pk):
        return Response({'messange':'single book with id '+ str(pk)},status.HTTP_200_OK)
    def put(self,request,pk):
        return Response({'title':request.data.get('title')},status.HTTP_200_OK)
