from django.db import models

class Certification(models.Model):

    STATE_CHOICES = [
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=100, verbose_name= 'Title')
    platform = models.CharField(max_length=50, verbose_name='Platform')
    professor = models.CharField(max_length=100, verbose_name='Professor')
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='in_course', verbose_name='State')
    image = models.ImageField(null=True, verbose_name='Image', upload_to='certifications')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date of update')

    class Meta:
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'
        ordering = ['updated']

    def __str__(self) -> str:
        return self.title 
