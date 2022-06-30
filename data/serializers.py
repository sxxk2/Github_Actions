import datetime

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import SewerPipe, Rainfall, GuName


class SewerPipeModelSerializer(ModelSerializer):
    '''
    Assignee : 민지

    데이터 출력 예시와 동일하게 고유번호, 측정 수위 필드만 출력
    '''
    class Meta:
        model = SewerPipe
        fields = ['idn', 'mea_wal']


class RainfallModelSerializer(ModelSerializer):
    '''
    Assignee : 민지
    
    데이터 출력 예시와 동일하게 강우량계명, 10분우량 필드만 출력
    '''
    class Meta:
        model = Rainfall
        fields = ['raingauge_name', 'rainfall10']


class GuNameModelSerializer(ModelSerializer):
    """
    Assignee : 희석

    View단에서 GuName 테이블의 오브젝트가 주어졌을 때
    역참조를 통해 Rainfall, SewerPipe 모델의 쿼리셋을 가져오고
    datetime_info로 필터하여 serializer data 전달
    """
    rainfall_data = serializers.SerializerMethodField()
    sewer_pipe_data = serializers.SerializerMethodField()

    def get_rainfall_data(self, obj):
        rainfalls = obj.rainfall
        datetime_info = self.context["datetime"]
        rainfall_serializer = RainfallModelSerializer(rainfalls.filter(
            receive_time__gte=datetime_info,
            receive_time__lt=datetime_info + datetime.timedelta(minutes=10)
        ), many=True)
        return rainfall_serializer.data

    def get_sewer_pipe_data(self, obj):
        sewer_pipe = obj.sewer_pipe
        datetime_info = self.context["datetime"]
        sewer_pipe_serializer = SewerPipeModelSerializer(sewer_pipe.filter(
            mea_ymd__gte=datetime_info,
            mea_ymd__lt=datetime_info + datetime.timedelta(minutes=1)
        ), many=True)
        return sewer_pipe_serializer.data

    class Meta:
        model = GuName
        fields = ["gubn", "name", "rainfall_data", "sewer_pipe_data"]

