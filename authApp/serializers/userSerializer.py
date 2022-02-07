from rest_framework                         import serializers
from authApp.models.user                    import User

class UserSerializer(serializers.ModelSerializer):
    """El usuario tiene la funcion de crear la cuenta"""
    class Meta:
        model  = User
        fields = ['id', 'username', 'password', 'name']
    
    """def create(self, validated_data):
        Creacion de usuario
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        En el campo user asocia la cuenta creada
        Account.objects.create(user=userInstance, **accountData) 
        return userInstance"""
        
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id' : user.id,
            'username' : user.username,
            'name' : user.name,
            'email' : user.email,
        }

    """def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
            'id' : user.id,
            'username' : user.username,
            'name' : user.name,
            'email' : user.email,
            'account' : {
                'id' : account.id,
                'balance' : account.balance,
                'last_change_date' : account.last_change_date,
                'is_active' : account.is_active
            }
        }"""
        
        