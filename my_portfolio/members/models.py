from django.db import models
#데이터베이스를 통틀어 모델이라고 함
#최근 개발의 트렌드는 MVC패턴 : Model(백엔드), View(프론트엔드), Controller => javq spring
#모델이란? 데이터가 모델이라는 Object
#Django에서는 데이터가 모델이라는 객체로 생성되고 실제로는 데이터베이스의 테이블

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

