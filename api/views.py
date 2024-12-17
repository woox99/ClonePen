from django.shortcuts import render, get_object_or_404
from django.views import View
from core.models import Pen
from django.http import JsonResponse, HttpResponse


class TogglePin(View):
    def post(self, request, pk):
        pen = get_object_or_404(Pen, pk=pk)
        if pen in request.user.profile.pinned_items.all():
            request.user.profile.pinned_items.remove(pen)
            return JsonResponse({'pinned': False})
        request.user.profile.pinned_items.add(pen)
        return JsonResponse({'pinned': True})

