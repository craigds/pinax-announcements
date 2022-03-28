import django.dispatch

# provides args: announcement, request
announcement_created = django.dispatch.Signal()
# provides args: announcement, request
announcement_updated = django.dispatch.Signal()
# provides args: announcement, request
announcement_deleted = django.dispatch.Signal()
