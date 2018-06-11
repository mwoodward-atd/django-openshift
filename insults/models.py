from django.db import models


class Word(models.Model):
    WORD_TYPE_CHOICES = (
        ('shortadj', 'Short Adjective'),
        ('longadj', 'Long Adjective'),
        ('noun', 'Noun'),
    )
    word = models.CharField(max_length=50)
    word_type = models.CharField(max_length=20, choices=WORD_TYPE_CHOICES)

    def __str__(self):
        return '{} ({})'.format(self.word, self.word_type)
    
    class Meta:
        ordering = ['word_type', 'word', ]
