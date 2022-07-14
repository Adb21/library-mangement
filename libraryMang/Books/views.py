from .models import Books
from rest_framework.response import Response
from .serializers import BookSerailizer
from rest_framework import status,generics
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated ,IsAdminUser


# Create your views here.
class BooksListAPIView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Books.objects.all()
    serializer_class = BookSerailizer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['category','language']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'author']

# class BooksRetrieveAPIView(generics.RetrieveAPIView):
    
#     queryset = Books.objects.all()
#     serializer_class = BookSerailizer

#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

# class BookCreateAPIView(generics.GenericAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerailizer
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def post(self,request):
#         serializer  = BookSerailizer(data=request.data,context={ 'request': self.request })
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                     "Message":"Added Book Successfully",

#                 },status=status.HTTP_202_ACCEPTED
#             )
#         return Response({"Error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class BookCreateAPIView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerailizer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]

class BookRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerailizer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]



