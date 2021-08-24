from django.db import models

# Create your models here.
class MovieQuerySet(models.QuerySet):
    def filter_by_query(self,query_dict):
        return self.filter(**query_dict)

class MovieManager(models.Manager):
    def get_queryset(self):
        return MovieQuerySet(self.model,using=self._db)

    def filter_by_query(self,query_dict):
        return self.get_queryset().filter_by_type(**query_dict)
    
    


class Movie(models.Model):
    title = models.CharField(max_length=255,unique=True)
    start_year = models.IntegerField(null=True,blank=True)
    end_year = models.IntegerField(null=True,blank=True)
    rated = models.CharField(max_length=150,null=True,blank=True)
    released = models.DateField(null=True,blank=True)
    runtime = models.CharField(max_length=50,null=True,blank=True)
    genere = models.CharField(max_length=50,null=True,blank=True)
    director = models.CharField(max_length=150,null=True,blank=True)
    writer = models.CharField(max_length=150,null=True,blank=True)
    actors = models.TextField(null=True,blank=True)
    plot = models.TextField(null=True,blank=True)
    language = models.CharField(max_length=255,null=True,blank=True)
    country = models.CharField(max_length=150,null=True,blank=True)
    awards = models.CharField(max_length=255,null=True,blank=True)
    poster =  models.URLField(max_length=255,null=True,blank=True)
    metascore = models.FloatField(null=True,blank=True)
    imdb_rating = models.FloatField(null=True,blank=True)
    imdb_votes = models.CharField(max_length=150,null=True,blank=True)
    imdb_id = models.CharField(max_length=255,null=True,blank=True)
    type = models.CharField(max_length=150,null=True,blank=True)
    dvd = models.DateField(null=True,blank=True)
    box_office = models.CharField(max_length=150,null=True,blank=True)
    production = models.CharField(max_length=255,null=True,blank=True)
    website =   models.URLField(max_length=255,null=True,blank=True)

    objects = MovieManager()

    class Meta:
        verbose_name_plural = 'Movies'
    

    def __str__(self):
        return self.title




class CommentQuerySet(models.QuerySet):
    def filter_by_query(self,query_dict):
        return self.filter(**query_dict)

class CommentManager(models.Manager):
    def get_queryset(self):
        return CommentQuerySet(self.model,using=self._db)

    def filter_by_query(self,query_dict):
        return self.get_queryset().filter_by_type(**query_dict)

class Comment(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField()

    objects = CommentManager()

    class Meta:
        verbose_name_plural = 'Comments'
    

    def __str__(self):
        return self.movie.title