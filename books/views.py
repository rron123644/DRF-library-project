from django.shortcuts import render
from rest_framework import generics,status
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView,Response

# Create your views here.

# Book modelidagi barcha kitoblarni o'qish qismi
# class BooksListAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BooksListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer_class = BookSerializer(books, many=True).data
        data = {
            "status": f"{len(books)} ta kitob mavjud",
            "books": serializer_class
        }
        
        return Response(data)
    
        
# Book modelidagi qaysidir kitobni o'qib olish qismi
# class BookDetailAPIView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailAPIView(APIView):
        def get(self, request, pk):
            book = Book.objects.get(pk=pk)
            serializer_class = BookSerializer(book).data
            data = {
                "status": f"{book} kitobi",
                "book": serializer_class
            }
            
            return Response(data)
    
# Book modelidagi qaysidir kitobni o'chirib olish qismi
# class BookDeleteAPIView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDeleteAPIView(APIView):
    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        data = {
            "status": True,
            "message": f"{book} kitobi o'chirildi"
        }
        
        return Response(data)
    
# Book modelidagi qaysidir kitobni o'qib yangilash qismi
# class BookUpdateAPIView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    
  
class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        data = request.data
        serializer =  BookSerializer(book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        
        data = {
            "status": True,
            "message": {f"{book_saved} kitobi ma'lumotlari yangilandi"}
        }
        
        return Response(data)
    
    
    
# Book modelidagi qaysidir kitobni yaratish
# class BookCreateAPIView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": "Kitob yaratildi",
                "books": data
            }
            
            return Response(data)
        else:
            return Response(
                {"status": False,
                "message": "Serializer is not valid"}, status = status.HTTP_400_BAD_REQUEST
            )
    
    
    
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_class = BookSerializer(books, many=True).data
        data = {
            "status": f"{len(books)} ta kitob mavjud",
            "books": serializer_class
        }
        
        return Response(data)
        
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": "Kitob yaratildi",
                "books": data
            }
            
            return Response(data)
        else:
            return Response(
                {"status": False,
                "message": "Serializer is not valid"}, status = status.HTTP_400_BAD_REQUEST
            )