from django import forms
from .models import Album, Tag
from .models import Photo

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image', 'albums', 'tags']

class MultiPhotoUploadForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    albums = forms.ModelMultipleChoiceField(queryset=Album.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    new_album_title = forms.CharField(max_length=100, required=False, label="Create New Album")

class AlbumAdminForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'cover_image']

    def clean_order(self):
        order = self.cleaned_data.get('order')
        if not isinstance(order, int):
            raise forms.ValidationError("Order must be an integer.")
        return order