import datetime
from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timeStamp = models.DateField()

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

            _dict = {}
            for attr in fields:
                value = getattr(self, attr)
                if isinstance(value, datetime.datetime):
                    _dict[attr] = value.strftime('%Y-%m-%d %H:%M:%S')
                elif isinstance(value, datetime.date):
                    _dict[attr] = value.strftime('%Y-%m-%d')
                else:
                    _dict[attr] = getattr(self, attr)
        import json
        return json.dumps(_dict)



