from django.shortcuts import get_object_or_404

from rest_framework import parsers, renderers
#from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
#from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
#from rest_framework.schemas import ManualSchema
from rest_framework.views import APIView

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import AuthTokenSerializer, UserModelSerializer
from ..models import User


class ObtainAuthToken(APIView):
    '''A Custom ObtainAuthToken APIView that uses email instead of username.'''
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({'success': True, 'message': '성공', 'token': token.key})


class UserDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserModelSerializer

    def get_object(self):
        queryset = User.objects.all()
        obj = get_object_or_404(queryset, username=self.request.user.username)
        return obj
