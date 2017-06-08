from django import template
from promanage.models import Notification

register = template.Library()

@register.simple_tag(takes_context=True)
def unread_notifications(context):
    user = context['user']
    return Notification.objects.filter(to_user=user,is_read=False).count()