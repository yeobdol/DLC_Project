from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from user.models import User
from user.serializers import UserSerializer, CustomObtainPairSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "가입완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message" : f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        
class FollowView(APIView):
    def post(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        me = request.user
        if me in you.followers.all():
            you.followers.remove(me)
            return Response("Unfollow 했습니다.", status=status.HTTP_200_OK)
        else:
            you.followers.add(me)
            return Response("follow 했습니다.", status=status.HTTP_200_OK)
        
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer