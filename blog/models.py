from django.db import models

class Blog(models.Model):
	Reviews = 1 
	Profiles = 2
	Rant = 3
	Inspirational =4

	Genre = (
		(Reviews, "Reviews"),
		(Profiles, "Profiles"), 
		(Rant, "Rant"), 
		(Inspirational, "Inspirational")
	)

	Title = models.CharField(verbose_name="Blog Title", max_length= 200)
	Author = models.CharField(verbose_name="Author", max_length= 200)
	Genre = models.IntegerField(verbose_name = "Genre", choices= Genre)
	Content = models.CharField(verbose_name="Content", max_length= 2000)

	def __str__(self):
		return "%s" % self.Title
		

	def get_Title(self):
		return	self.Title

	def get_Author(self):
		return	self.Author

	def get_Genre(self):
		return	self.Genre

	def get_Content(self):
		return	self.Content
