from __future__ import unicode_literals

from django.db import models

# Create your models here.
from proje.settings import AUTH_USER_MODEL


class Blog(models.Model):
    """
    Blog Fields
    """
    slug = models.SlugField(max_length=80, null=True, blank=True, help_text=u"Link otomatik alinir, Lutfen Degistirmeyiniz!")
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(AUTH_USER_MODEL)
    content = models.TextField(help_text='Bu Alan Bos Birakilamaz!')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='BlogResimleri/%Y/%m/%d', default='BlogResimleri/blog.png')
    video = models.FileField(upload_to='Videos/%Y/%m/%d', blank=True)
    link = models.URLField(blank=True)

    def __unicode__(self):
        return '{}'.format(self.title)
