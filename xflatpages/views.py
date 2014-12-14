# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader, RequestContext, TemplateDoesNotExist
from django.utils.safestring import mark_safe

from .models import FlatPage


def flatpage(request, url):
    """ Rewrited version of django flatpage view
    """
    if not url.startswith('/'):
        url = '/' + url
    flatpage = get_object_or_404(FlatPage, url=url)
    try:
        template = loader.get_template(flatpage.get_template())
    except TemplateDoesNotExist:
        logger.error(
            u'Template %s doesnt exists, loaded default' % flatpage.get_template()
        )
        template = loader.get_template(flatpage.get_template(True))
    # To avoid having to always use the "|safe" filter in flatpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    flatpage.title = mark_safe(flatpage.title)
    flatpage.cont = mark_safe(flatpage.cont)
    c = RequestContext(request, {'flatpage': flatpage,})
    response = HttpResponse(template.render(c))
    return response
