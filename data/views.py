from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from data.models import GuName as GuNameModel
from data.serializers import GuNameModelSerializer

""""""
# Create your views here.

# url : api/data/v1/rainfall-and-drainpipe-info/<gubn>/<datetime>/
class RainfallAndSewerPipeInfoApiView(APIView):
    """
    Assignee : 희석

    Http method = GET only

    클라이언트의 요청을 받아 하수관로 및 강우량 정보를
    response 하는 API입니다.
    """
    permission_classes = [permissions.AllowAny]
    def get_guname_object(self, obj_pk):
        try:
            object = GuNameModel.objects.get(gubn=obj_pk)
        except GuNameModel.DoesNotExist:
            # seom event : 찾는 object 없으면 빈값을 return
            return
        return object

    def get(self, request, gubn, datetime):
        print(gubn, datetime)
        gu_name = self.get_guname_object(gubn)
        if not gu_name:
            return Response({"error": "구 코드가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        # serializer 사용해서 data response
        return Response(GuNameModelSerializer(gu_name, context={"datetime": datetime}).data, status=status.HTTP_200_OK)
