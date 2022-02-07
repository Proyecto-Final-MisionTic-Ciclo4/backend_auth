from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenVerifySerializer


class VerifyTokenView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        serializer = TokenVerifySerializer(data=request.data)  # Almacena los datos que vienen en el body de la peticion HTTP
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM']) #Indica el algoritmo usado para decodificar
        
        try:
            serializer.is_valid(raise_exception=True) #Revisa los campos del serializador
            token_data = token_backend.decode(request.data['token'], verify=False) # Aqui viajan las credenciales
            serializer.validated_data['User_id'] = token_data['user_id'] #Toma el user_id que viaja en el token
        except TokenError as e:
            print(e)
            raise InvalidToken(e.args[0])
        except Exception as e:
            print(e)
        
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
