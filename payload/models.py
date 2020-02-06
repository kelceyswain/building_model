from django.db import models
from django.core.exceptions import ValidationError


class Building(models.Model):
    name = models.CharField(max_length=200)
    building_id = models.IntegerField()
    desctription = models.TextField()
    
    def __str__(self):
        return self.name



class Content(models.Model):

    title = models.CharField(max_length=100)
    #creator = pass # I think this needs to make use of a foreign key that takes something from the Users app with email etc available. 
    public = models.BooleanField(default=False, null=False, editable=True)
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        abstract = True



class Text(Content):

    body = models.TextField()
    def __str__(self):
        return self.title



class Image(Content):
    # TODO: in settings need to update the path of MEDIA_ROOT.
    # TODO: investigate how to limit size of image upload.
    #body = models.ImageField(upload_to='uploads/')
    
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    body = models.ImageField(upload_to="uploads/", validators=[validate_image])
    
    def __str__(self):
        return self.title


class Video(Content):
    body = models.URLField(max_length=255)
    
    def __str__(self):
        return self.title



class Sound(Content):
    # TODO: limit size of sound file uploads
    body = models.FileField(upload_to='uploads/%Y/%m/%d/')
    
    def __str__(self):
        return self.title
