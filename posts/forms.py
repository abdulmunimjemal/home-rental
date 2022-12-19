from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(NewPostForm, self).__init__(*args, **kwargs)

    REGIONS = [
        ('Addis Ababa', 'Addis Ababa'),
        ('Diredawa', 'DireDawa'),
        ('Oromia', 'Oromia'),
        ('Amhara', 'Amhara'),
        ('Tigrai', 'Tigrai'),
        ('Afar', 'Afar'),
        ('Harari', 'Harari'),
        ('Sidama', 'Sidama'),
        ('South Nations', 'South Nations'),
        ('Gambella', 'Gambella'),
        ('Benishangul Gumuz', 'Benishangul Gumuz'),
    ]
    CAT = [
        ('studio', 'ስቱድዮ'),
        ('apartment', 'አፓርታማ'),
        ('condominium', 'ኮንዶሚኒየም'),
        ('office', 'ቢሮ'),
        ('other', 'ሌላ')
    ]
    title = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Post Title'}), label='')
    address = forms.CharField(max_length=300, required=True, widget=forms.TextInput(attrs={'placeholder': 'Address'}),  label='' )
    town = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Town'}),  label='')
    region = forms.ChoiceField(choices=REGIONS, required=True,  label='')
    body = forms.CharField(widget=forms.Textarea(attrs={"rows":"5", "cols": "30", "id": "editor"}))
    category = forms.ChoiceField(choices=CAT, required=True, label='')
    rental_rate = forms.IntegerField(max_value=1000000, min_value=500, required=True, label='', initial=1000)
    
    photo_1 = forms.ImageField(allow_empty_file=False, label='')
    photo_2 = forms.ImageField(allow_empty_file=False, label='')
    photo_3 = forms.ImageField(allow_empty_file=False, label='')
    photo_4 = forms.ImageField(allow_empty_file=False, label='')

    class Meta:
        model = Post
        fields = ('title', 'body', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'category', 'region', 'address', 'town', 'rental_rate')
    
    def save(self):
        obj = super(NewPostForm, self).save(commit=False)
        obj.author = self.user
        obj.save()
        return obj