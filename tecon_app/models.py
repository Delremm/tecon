# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.contrib import auth
from django.core.urlresolvers import reverse
from model_utils import Choices
from model_utils.fields import StatusField

User = auth.get_user_model()


class Trial(models.Model):
    """
    Model whis represents test
    """
    STATUS = Choices(
        ('users', _(u'Добавлено пользователем')), ('good', _(u'Годно')))
    status = StatusField(verbose_name=_(u"Статус"))
    title = models.CharField(_(u'Название теста'), max_length=255)
    description = models.TextField(_(u'Описание теста'), blank=True, null=True)
    data = models.TextField(
        _(u'Тест в json представлении'), blank=True, null=True)
    created = models.DateTimeField(_(u"Время создания"), auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=_(u"Создатель теста"))
    category = models.ForeignKey(
        'categories.Category',
        verbose_name=_(u"Категория"), null=True, blank=True)

    def __unicode__(self):
        return '%s %s' % (self.title, self.user.__unicode__())

    class Meta:
        verbose_name = _(u'Тест')
        verbose_name_plural = _(u'Тесты')

    def get_absolute_url(self):
        return reverse('tecon:test_details', args=[str(self.id)])


admin.site.register(Trial)
