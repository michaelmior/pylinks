import six
from django.conf import settings
from django.core.exceptions import ValidationError
from pyuploadcare.dj.models import FileField
from pyuploadcare.api_resources import File, UUID_WITH_EFFECTS_REGEX
from pyuploadcare.exceptions import InvalidRequestError

# Patch File to pass through S3 URLs
class LinkFile(File):
    def __init__(self, cdn_url_or_file_id):
        matches = cdn_url_or_file_id.startswith('links/')
        if matches:
            self.s3_path = cdn_url_or_file_id
            self.uuid = None
        else:
            self.s3_path = None
            File.__init__(self, cdn_url_or_file_id)

    @property
    def cdn_url(self):
        if self.s3_path is not None:
            return u'http://s3.amazonaws.com/{bucket}/media/{path}'.format(bucket=settings.AWS_STORAGE_BUCKET_NAME, path=self.s3_path)
        else:
            return File.cdn_url.fget(self)

    def __repr__(self):
        if self.uuid is None:
            return u'<LinkFile {s3_path}>'.format(s3_path=self.s3_path)
        else:
            return '<LinkFile {uuid}>'.format(uuid=self.uuid)

# Patch FileField to return LinkFile instances
class LinkFileField(FileField):
    def __init__(self, *args, **kwargs):
        kwargs.pop('upload_to', None)
        super(LinkFileField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if value is None or value == '':
            return value

        if isinstance(value, File):
            return value

        if not isinstance(value, six.string_types):
            raise ValidationError(
                'Invalid value for a field: string was expected'
            )

        if not UUID_WITH_EFFECTS_REGEX.search(value):
            return None

        try:
            return LinkFile(value)
        except InvalidRequestError as exc:
            raise ValidationError(
                'Invalid value for a field: {exc}'.format(exc=exc)
            )
