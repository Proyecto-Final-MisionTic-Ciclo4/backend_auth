from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings

from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all() # se traen todos los datos
    serializer_class = UserSerializer # Me llama al to_representation para devolverme los datos
    # permission_classes = (IsAuthenticated, )
    
    def update(self, request, *args, **kwargs):
        
        """token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM']) # el algoritmo para encriptar
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']: # En user_id se guarda el user que se esta logeando y lo compara con el usuario que viaja en la URL
            stringResponse = {'detail':'Unauthorized Request'} # valida que el usuario este pidiendo info de el y no de otro user
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""
                
        return super().update(request, *args, **kwargs)