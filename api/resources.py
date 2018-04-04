from tastypie import fields
from tastypie.resources import ModelResource
from api.models import Note, Label

class NoteResource(ModelResource):
    labels = fields.ToManyField('blog.api.LabelResource', 'labels', null=True, blank=True)
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        always_return_data = True

class LabelResource(ModelResource):
	notes = fields.ToManyField(NoteResource, 'notes')
	class Meta:
		queryset = Label.objects.all()
        resource_name = 'labels'
