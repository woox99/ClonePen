from rest_framework.serializers import ModelSerializer
from core.models import Pen

class PenSerializer(ModelSerializer):
    class Meta:
        model = Pen
        fields = ('__all__') ### Do we want all fields to be returned?
