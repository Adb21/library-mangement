from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,generics
from .serializers import AdminSerializer, LoginSerailizer,StudentSerailizer, getTokens, LogoutSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterAdminAPIView(generics.GenericAPIView):
    serializer_class = AdminSerializer
    
    def post(self,request):
        serializer  = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Message":"Admin Registerd Successfully",
                    "Username":serializer.data['username']
                },status=status.HTTP_201_CREATED
            )
        return Response({"Error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class RegisterStudentAPIView(generics.GenericAPIView):
    serializer_class = StudentSerailizer
    
    def post(self,request):
        serializer  = StudentSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Message":"Student Registerd Successfully",
                    "Username":serializer.data['username']
                },status=status.HTTP_201_CREATED
            )
        return Response({"Error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(generics.GenericAPIView):
    # serializer_class = LoginSerailizer

    # def post(self,request):
    #     serializer  = LoginSerailizer(data=request.data,context={ 'request': self.request })
    #     if serializer.is_valid():
    #         return Response(
    #             {
    #                 "Message":"Login Successfully"
                   
    #             },status=status.HTTP_202_ACCEPTED
    #         )
    #     return Response({"Error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    serializer_class = LoginSerailizer
    
    def post(self,request):
        serializer  = LoginSerailizer(data=request.data,context={ 'request': self.request })
        if serializer.is_valid():
            tokens = getTokens(request.data['email'])
            return Response(
                {
                    "Message":"User Login Successfully",
                    "tokens":tokens

                },status=status.HTTP_202_ACCEPTED
            )
        return Response({"Error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)



class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
                    "Message":"User Logout Successfully"
                },status=status.HTTP_204_NO_CONTENT)

    
