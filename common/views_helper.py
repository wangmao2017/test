# coding=utf-8
from django.http import JsonResponse
from django.views.generic.detail import (
    SingleObjectTemplateResponseMixin, BaseDetailView)
from django.utils.translation import ugettext_lazy as _


def ret_format(result=True, messages=None, data=None):
    """
    格式化Json返回数据
    :param result: [bool] 一般为True
    :param messages: [str|list] 要在页面展示的消息，多条消息使用列表
    :param data: [dict] 返回给前端的数据
    :return: [dict]
    """
    assert isinstance(result, bool)
    if messages:
        assert isinstance(messages, (list, str))
        # i18n here
        if isinstance(messages, str):
            messages = [messages]
        messages = [_(m) for m in messages]
    if data:
        assert isinstance(data, dict)

    return {'result': result, 'messages': messages or [], 'data': data or {}}


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class HybridDetailView(JSONResponseMixin, SingleObjectTemplateResponseMixin, BaseDetailView):
    def render_to_response(self, context):
        # Look for a 'format=json' GET argument
        if self.request.GET.get('format') == 'json':
            return self.render_to_json_response(context)
        else:
            return super().render_to_response(context)

