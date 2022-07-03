from django.db import models

# Create your models here.


class SewerPipe(models.Model):
    """
    Assignee : 상백

    서울시 하수관로 수위 API 출력값의 출력명과 데이터 형태를 고려해서 설정
    mea_ynd는 날짜 형태로 DateTimeField 설정
    mea_wal는 소수점으로 FloatField 설정

    idn : 고유번호 | gubn : 구분코드 | gubn_nam : 구분명 | mea_ynd : 측정일자 | mea_wal : 측정수위 | sig_sta : 통신상태
    """

    idn = models.CharField(max_length=10)

    gubn = models.ForeignKey("GuName", on_delete=models.SET_NULL, null=True, related_name="sewer_pipe")

    gubn_nam = models.CharField(max_length=5)
    mea_ymd = models.DateTimeField()
    mea_wal = models.FloatField()
    sig_sta = models.CharField(max_length=10)


class Rainfall(models.Model):
    """
    Assignee : 상백

    서울시 강우량 정보 API 출력값의 출력명과 데이터 형태를 고려해서 설정
    gu_code는 숫자로 IntegerField 설정
    rainfall10는 소수점으로 FloatField 설정

    raingauge_code : 강우량계 코드 | raingauge_name : 강우량계명 | gu_code : 구청 코드 | gu_name : 구청명 | rainfall10 : 10분우량 |
    receive_time : 자료수집시각
    """

    raingauge_code = models.CharField(max_length=5)
    raingauge_name = models.CharField(max_length=10)
    gu_code = models.IntegerField()
    gu_name = models.CharField(max_length=5)
    rainfall10 = models.FloatField()
    receive_time = models.DateTimeField()

    gubn = models.ForeignKey("GuName", on_delete=models.SET_NULL, null=True, related_name="rainfall")


class GuName(models.Model):
    """
    Assignee : 상백

    GuName : SewerPipe = 1 : N
    GuName : Rainfall = 1 : N
    다음과 같은 관계로 설정해서 SewerPipe와 Rainfall 모델에서 참조할 수 있게 설정
    gubn 필드는 primary_key로 설정
    name 필드 ex) 강서구, 강남구,,,
    """

    gubn = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=5)
