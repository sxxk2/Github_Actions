from rest_framework.serializers import ModelSerializer
from data.models import SewerPipe


class OpenAPISewerPipeModelSerializer(ModelSerializer):
    '''
    Assignee : 훈희

    API요청으로 원하는 값을 저장 할 수 있게 구성
    사용할지 고민중

    '''

    class Meta:
        model = SewerPipe
        fields = [
            'idn',
            'gubn',
            'gubn_nam',
            'mea_ymd',
            'mea_wal',
            'sig_sta'
        ]
