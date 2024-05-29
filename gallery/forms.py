from django import forms
from .models import Album, Tag
from .widgets import MultipleFileInput

class MultiplePhotoUploadForm(forms.Form):
    images = forms.FileField(widget=MultipleFileInput(), required=True)
    albums = forms.ModelMultipleChoiceField(queryset=Album.objects.all(), required=True)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)


class AlbumAdminForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'cover_image']

    def clean_order(self):
        order = self.cleaned_data.get('order')
        if not isinstance(order, int):
            raise forms.ValidationError("Order must be an integer.")
        return order