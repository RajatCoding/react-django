from django.http import HttpResponse
from rest_framework import generics
from . serializer import UserSerializer
from . models import CustomUser

def home(request):
    print(request)
    return HttpResponse( "hai")

class UserListView(generics.ListCreateAPIView):
    print("hii")

    queryset = CustomUser.objects.all()
    print(queryset)
 
    serializer_class = UserSerializer

    def create(self, serializer):
        print(self.request.data)  # Print the incoming data for debugging
        serializer.save()