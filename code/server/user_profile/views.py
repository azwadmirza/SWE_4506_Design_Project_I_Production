from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework import status
from gateway.models import user

@authentication_classes([JWTAuthentication])
class Profile(APIView):
    permission_classes = []
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id is None:
            return Response({'message': 'id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            searcheduser = user.objects.filter(id=id).values().exclude(password=None).first()
            if searcheduser:
                response_data = {
                    'username': searcheduser['username'],
                    'email': searcheduser['email'],
                    'image': searcheduser['image']
                }
                return Response(response_data)
            else:
                return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except user.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id is None:
            return Response({'message': 'id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_instance = user.objects.get(id=id)
            user_data = request.data  

            if 'username' in user_data:
                user_instance.username = user_data['username']
            if 'email' in user_data:
                user_instance.email = user_data['email']
            if 'image' in user_data:
                user_instance.image = user_data['image']

            user_instance.save()
            return Response({
                'id': user_instance.id,
                'username': user_instance.username,
                'email': user_instance.email,
                'image': user_instance.image
            })
        except user.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print("Error occurs in this block")
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        