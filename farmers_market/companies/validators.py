from django.core.exceptions import ValidationError


def validate_image(file_obj):
    filesize = file_obj.file.size
    if filesize > 2621440:
        raise ValidationError('File size cannot exceed 2.5MB')
