import requests
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import mm_User
from .serializers import (UserSerializer, ProfileSerializer, MiniprogramLoginSerializer)

from utils.wechat.WXBizDataCrypt import WXBizDataCrypt


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = mm_User.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'], serializer_class=MiniprogramLoginSerializer, permission_classes=[], authentication_classes=[])
    def login_miniprogram(self, request):
        """小程序登录
        1. csrf校验去除
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']
        avatar_url = serializer.validated_data['avatar_url']
        name = serializer.validated_data['name']
        encryptedData = serializer.validated_data['encryptedData']
        iv = serializer.validated_data['iv']
        logger.info('code: {}'.format(code))
        logger.info('encryptedData: {}'.format(encryptedData))
        logger.info('iv: {}'.format(iv))
        
        wx_res = requests.get(settings.MINI_PRAGRAM_LOGIN_URL + code)
        ret_json = wx_res.json()
        logger.info('code: {}, name: {}'.format(code, name))
        logger.info('wechat resp: {}'.format(ret_json))
        if 'openid' not in ret_json:
            return Response(data=ret_json, status=status.HTTP_400_BAD_REQUEST)
        
        # 处理unionid
        session_key = ret_json['session_key']
        pc = WXBizDataCrypt(settings.MINI_PROGRAM_APP_ID, session_key)
        try:
            decrypt_dict = pc.decrypt(encryptedData, iv)
        except Exception as e:
            return Response(status=status.HTTP_401_UNAUTHORIZED) 
        logger.info('decrypt_dict : {}'.format(decrypt_dict))
        # unionid不一定存在
        unionid = decrypt_dict.get('unionId')
        mini_openid = ret_json['openid']
        user = mm_User.get_user_by_miniprogram(avatar_url, name,  mini_openid=mini_openid, unionid=unionid)
        process_login(request, user)
        serializer_user = ProfileSerializer(user)
        data = serializer_user.data
        return Response(data=data)
