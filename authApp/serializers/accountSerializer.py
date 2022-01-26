from rest_framework                         import serializers
from models                                 import Account
from models                                 import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Account
        fields = ['balance', 'last_change_date', 'is_active']
        
    """ If we want to be able to return complete object instances based on the 
        validated data we need to implement one or both of the .create() and 
        .update() methods.  """
        
    def to_representation(self, obj):
        """ Se hace los inner joins"""
        accountData = Account.objects.get(id=obj.id)
        userData = User.objects.get(id=obj.user_id)
        return {
            'id': accountData.id,
            'balance': accountData.balance,
            'last_change_date': accountData.last_change_date,
            'user': {
                'name': userData.name,
                'email': userData.email
                }
        }
