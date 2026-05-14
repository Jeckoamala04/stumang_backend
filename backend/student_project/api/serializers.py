from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

    # Name Validation
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Name must contain at least 3 characters"
            )
        return value

    # Phone Validation
    def validate_phone(self, value):

        # number mattum allow
        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only numbers"
            )

        # exact 10 digits
        if len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must be 10 digits"
            )

        return value

    # Email Validation
def validate_email(self, value):

    student_id = self.instance.id if self.instance else None

    if Student.objects.filter(email=value).exclude(id=student_id).exists():
        raise serializers.ValidationError(
            "Email already exists"
        )

    return value

    # Address Validation
    def validate_address(self, value):

        if len(value.strip()) < 5:
            raise serializers.ValidationError(
                "Address is too short"
            )

        return value

        # Image Validation
def validate_image(self, value):

    # file size check (2MB)
    if value.size > 2 * 1024 * 1024:
        raise serializers.ValidationError(
            "Image size must be less than 2MB"
        )

    # extension check
    valid_extensions = ['jpg', 'jpeg', 'png']

    ext = value.name.split('.')[-1].lower()

    if ext not in valid_extensions:
        raise serializers.ValidationError(
            "Only JPG, JPEG, PNG images are allowed"
        )

    return value