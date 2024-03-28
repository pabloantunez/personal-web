from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name= 'Title')
    content = models.TextField(verbose_name= 'Content')
    image = models.ImageField(null=True, verbose_name='Image', upload_to='projects')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date of update')
    url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['updated']

    def __str__(self) -> str:
        return self.title 