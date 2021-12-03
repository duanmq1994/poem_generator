from django.db import models

# Create your models here.
class WordType(models.Model):
    type_name = models.CharField(max_length=200)
    after = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.type_name
    
class Words(models.Model):
    word_type = models.ForeignKey(WordType, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)

    def __str__(self):
        return '%s (%s)' % (self.word, self.word_type)

class Rules(models.Model):
    rule_type = models.CharField(max_length=50)
    members = models.CharField(max_length=200)

    def __str__(self):
        return self.rule_type

class Visitor(models.Model):
    ip = models.CharField(max_length=50, default=None)
    end_point = models.CharField(max_length=50, default=None)
    count = models.IntegerField(default=0)
    
    def __str__(self):
        return '%s at %s' % (self.ip, self.visit_time)
    
