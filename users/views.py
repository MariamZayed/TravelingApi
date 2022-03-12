from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView #this is new!first time to use
from .serializers import RegisterUserSerializer #we created this to specify what to serialize to save in DB
from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.views import TokenObtainPairView


class CustomUserRegister(APIView): #when to register
    permission_classes = [AllowAny] #AllowAny because of when to register, it should be allowed to anyone
    
    def post(self, request):#post request
        reg_serializer = RegisterUserSerializer(data=request.data)#this's a fun we created in serializer.py#fetch all data from request
        if reg_serializer.is_valid(): #if it staisfes the serializer form
            newuser = reg_serializer.save() #then save this user in the db
            if newuser: #if true
                # json = reg_serializer.data 
                return Response(status=status.HTTP_201_CREATED)#then return response with the json data and congratualtions, we're done!
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)#if the first if is false, continue and come here, send 400 :'(
        
        ##here was an old code, you can find it in the other repo https://github.com/MariamZayed/travel-app-workshop

class BlacklistTokenUpdateView(APIView):#when logs out
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()#add refresh_token to black list, cause it's no longer availabe to user to login with
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)