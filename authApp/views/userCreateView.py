from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from authApp.serializers.userSerializer import UserSerializer



"""from django.conf import settings
from django.conf import settings
from rest_framework_simplejwt.backends import TokenBackend
"""

""" Generics APIView"""

class UserCreateView(views.APIView): 
    
    """queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer # la data la vamos a hacer con la data del body para crear el objeto de la categoria
    # permission_class = [IsAuthenticated,]"""

    def post(self, request, *args, **kwargs): # metodo HTTP (POST, GET, PUSH, DELETE) 
                                    # recibe una data en el request del body 
                                    # *args argumentos basicos del servicio web 
                                    # **kwargs argumentos que se necesiten y que puedan llegar 
    
        serializer = UserSerializer(data=request.data) # Almacena los datos que vienen en el body de la peticion HTTP
        serializer.is_valid(raise_exception=True) #Revisa los campos del serializador
        serializer.save() # Llama la funcion create en el serializador
        
        token_data = {
            'username': request.data['username'],
            'password': request.data['password']
        }
        
        token_serializer = TokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)
        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)
 