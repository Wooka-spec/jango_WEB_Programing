from django.db import models #django 에서는 테이블을 하나의 클래스로 정의하고 테이블의 컬럼은 클래스의 변수(속성)으로 매핑

# Create your models here.
class Question(models.Model): #테이블 클래스는 django.db.models.Model 에서 상속받아 정의
    question_text = models.CharField(max_length = 200) #테이블의 변수타입(컬럼타입) 또한 장고에서 미리 정해둔 필드 클래스를 사용합니다
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.choice_text


