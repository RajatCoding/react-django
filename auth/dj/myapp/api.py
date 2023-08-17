from django.http import HttpResponse
from rest_framework import generics
from . serializer import UserSerializer
from . models import CustomUser

def home(request):
    print(request)
    return HttpResponse( "hai")

class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer