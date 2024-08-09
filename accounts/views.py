from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserSerializer, PasswordUpdateSerializer, CreateUserSerializer

User = get_user_model()

class UserList(APIView):
    permission_classes = [IsAuthenticated]

    # todo: add permission for admin only

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            if request.user == user:
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UserCreate(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            if request.user == user:
                serializer = UserSerializer(user, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)




class PasswordUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = PasswordUpdateSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            confirm_password = serializer.validated_data['confirm_password']

            if not user.check_password(old_password):
                return Response({'error': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

            if new_password != confirm_password:
                return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)