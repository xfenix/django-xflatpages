# -*- coding: utf-8 -*-
import os
import glob

from django.conf import settings
from django.db import models
from django.utils.encoding import iri_to_uri
from django.core.urlresolvers import get_script_prefix
from cache_utils.decorators import cached


FLATPAGE_TPL_DIR = getattr(settings, 'FLATPAGE_TPL_DIR', 'flatpages')
FLATPAGE_DEFAULT_TPL = getattr(settings, 'FLATPAGE_DEFAULT_TPL', 'default')


#@cached(86400)
def get_avail_tpls():
    """ Scan flatpages directory in template folder
    then return list of all available templates
    """
    try:
        tpl_dir = settings.TEMPLATE_DIRS[0]
    except IndexError:
        return ()
    try:
        templates = glob.glob(
            os.path.join(
                tpl_dir, FLATPAGE_TPL_DIR, '*.html'
            )
        )
    except TypeError:
        return []
    choices = []
    for tpl in templates:
        choices.append(
            (os.path.split(tpl)[-1], os.path.split(tpl)[-1])
        )
    return choices


class FlatPage(models.Model):
    """ Custom flatpage
    rewrite of https://github.com/django/django/blob/master/django/contrib/flatpages/
    """
    url = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name=u'URL',
        help_text=u"Например: '/about/contact/'. Убедитесь, что вы добавили слеш в начало и конец",
    )
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название',
    )
    cont = models.TextField(
        verbose_name=u'Содержимое',
        blank=True,
    )
    template_name = models.CharField(
        u'Шаблон', max_length=255,
        help_text=u'Выберите из списка доступных шаблонов (директория /templates/%s/)' % FLATPAGE_TPL_DIR,
        choices=get_avail_tpls(),
        default=getattr(
            dict(get_avail_tpls()), FLATPAGE_DEFAULT_TPL, None
        ),
    )

    def get_template(self, default=False):
        # return relative path to flatpage template
        return os.path.join(
            FLATPAGE_TPL_DIR,
            FLATPAGE_DEFAULT_TPL if default else self.template_name
        )

    def clean(self):
        url = self.url
        same_url = FlatPage.objects.filter(url=url)
        if self.pk:
            same_url = same_url.exclude(pk=self.pk)
        if same_url.exists():
            raise ValidationError(
                u'Простая страница с адресом %(url)s уже существует',
                code='duplicate_url',
                params={'url': url,},
            )
        return super(FlatPage, self).clean()

    def get_absolute_url(self):
        # handle script prefix manually because we bypass reverse()
        return iri_to_uri(get_script_prefix().rstrip('/') + self.url)

    def __unicode__(self):
        return u"%s -- %s" % (self.url, unicode(self.title))

    class Meta:
        verbose_name = u'Простая страница'
        verbose_name_plural = u'Простые страницы'
        ordering = ('url',)
