# Example serializer helper: convert MongoDB ObjectId to string

from rest_framework import serializers

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        try:
            return str(value)
        except Exception:
            return value

    def to_internal_value(self, data):
        return data
