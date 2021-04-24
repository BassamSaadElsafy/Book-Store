from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import BookSerializer
from books.models import Book
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def index(request):
    books = Book.objects.all()
    serializers = BookSerializer(instance = books, many = True)
    return Response(data = serializers.data, status = status.HTTP_200_OK)

@api_view(["GET"])
def show(request, id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer(instance = book)
    return Response(data = serializer.data, status = status.HTTP_200_OK)
    

@api_view(["POST"])
def store(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data = serializer.data, status = status.HTTP_201_CREATED)
    
    return Response(data={
        "success" : False,
        "errors"  : serializer.errors
    })
    
    
@api_view(["PUT"])
def update(request, id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["DELETE"])
def destroy(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return Response(data={
        "success" : True,
        "message"  : "Book has been deleted successfully"
    })
    

@api_view(["POST"])
def signup(request):
    seriliazer = UserSerilizer(data=request.data)
    if seriliazer.is_valid():
        seriliazer.save()
        return Response(data={
            "success" : True,
            "message" : "User Created Successfully"
        })

    return Response(data = {
        "success" : False,
        "errors"  : serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)        