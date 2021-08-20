from django.contrib import admin
from .models import Run, Order, FeedbackOrder, FeedbackRun, Deal

admin.site.register(Run)
admin.site.register(Order)
admin.site.register(FeedbackOrder)
admin.site.register(FeedbackRun)
admin.site.register(Deal)

