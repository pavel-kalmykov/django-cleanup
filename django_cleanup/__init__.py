import django

'''
    django-cleanup automatically deletes files for FileField, ImageField, and
    subclasses. It will delete old files when a new file is being save and it
    will delete files on model instance deletion.
'''
__version__ = '6.0.0-dev'
if django.VERSION < (3, 2):
    default_app_config = 'django_cleanup.apps.CleanupConfig'
