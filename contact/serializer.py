from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth.models import User
from contact.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(min_length=3, max_length=10)
    lastname = serializers.CharField(min_length=3, max_length=10)
    phone_number = PhoneNumberField()

    def create(self, validated_data):
        validated_data["user"] = User.objects.get(id=self.context["request"].user.id)

        contact = Contact.objects.create(**validated_data)
        contact.save()
        return contact

    class Meta:
        model = Contact
        fields = "__all__"
        extra_kwargs = {"user": {"read_only": True}}
