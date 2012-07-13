# coding: utf-8
from django.db import models
from django.contrib.sites.models import Site
from django.core.cache import cache


def get_option(name):
    field_names = [field.name for field in Options._meta.fields]
    if name not in field_names:
        raise ValueError("Options don't have field: '%s'" % name)
    options = current_options()
    return getattr(options, name) if options else None

def current_options():
    current_site = Site.objects.get_current()
    try:
        return Options.objects.get(site=current_site)
    except Options.DoesNotExist:
        return


class Options(models.Model):
    class Meta:
        verbose_name = u'опции'
        verbose_name_plural = u'опции'

    site = models.OneToOneField(Site, default=Site.objects.get_current())
    site_name = models.CharField(u'имя сайта', max_length=255, default='My Company Name')
    site_slogan = models.CharField(u'слоган', max_length=255, default='Our Company produces goods and services.')
    from_email = models.EmailField(blank=True, null=True)
    to_email = models.EmailField(blank=True, null=True)
    extra_head = models.TextField(u'extra head', blank=True, null=True, help_text=u'Дополнения в head страницы, например здесь можно разместить код Яндекс.Метрики или Google.Analytics')
    informers = models.TextField(u'информеры', blank=True, null=True)
