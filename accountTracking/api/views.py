from rest_framework.response import Response
from rest_framework.decorators import api_view

from accountTracking.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        #Define data obj
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response'] = "successfully registered a new user."
            data['username'] = account.username
            data['email'] = account.email
            # To simplify the authentication process, provide each user a Toke in
            # advance whenever a new user is created
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
