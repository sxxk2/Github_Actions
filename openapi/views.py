from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from data.models import GuName as GuNameModel
from .serializers import OpenAPISewerPipeModelSerializer

from .tests import save_sewerpipe_data_all_gubn, save_sewerpipe_data, save_rainfall_data


class OpenAPISewerPipeInfoApiView(APIView):
    """
    Assignee : 훈희

    Http method = GET only

    날짜를 입력 받아 OpenAPI의 값을 가져와서 저장하는 API입니다.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, start_date, end_date):
        # openapi_serializers = OpenAPISewerPipeModelSerializer()
        start_date = int(start_date)
        end_date = int(end_date)
        save_sewerpipe_data_all_gubn(start_date, end_date)

        return Response({f'{start_date} 부터 {end_date}까지 저장하였습니다.'}, status=status.HTTP_200_OK)

    def post(self, request, start_date, end_date):
        save_sewerpipe_data_all_gubn(start_date, end_date)

        return Response({'message': 'post method!!'})
