
# Create your models here.

#encoding: utf-8
from django.db import models

class Message(models.Model):
    username=models.CharField(max_length=256)
    title=models.CharField(max_length=512)
    content=models.TextField(max_length=256)
    publish=models.DateTimeField()
	#为了显示
    def __str__(self):
        tpl = '<Message:[username={username}, title={title}, content={content}, publish={publish}]>'
        return tpl.format(username=self.username, title=self.title, content=self.content, publish=self.publish)

class Player(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    # 为了显示
    def __str__(self):
        tpl = '<Player:[username={username}, score={score}]>'
        return tpl.format(username=self.username, score=self.score)