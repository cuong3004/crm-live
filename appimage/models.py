
from django.db import models

# from pprint import pprint

# Create your models here.

# def case_upload_location(object, filename):
# 	case_name = object.full_name.lower().replace(' ', '-')
# 	file_name = filename.lower().replace(' ','-')
# 	return "casos/{}/{}".format(case_name, file_name)

class Class_User(models.Model):
	full_name = models.CharField(max_length=255, null=True, blank=False)
	title = models.CharField(max_length=255, blank=True)
	image_rep = models.ImageField(max_length=255, upload_to='class', null=True, blank=True)

	def __str__(self):
		# if full_name:
		# 	return full_name
		# else:
		return self.full_name

	# def __str__(self):
	# 	return self.last_name + self.first_name

class Image_User(models.Model):
	#create file_name 'class_user_id'
	class_user = models.ForeignKey(Class_User, on_delete=models.CASCADE)
	image = models.ImageField(max_length=255, upload_to='image', null=True, blank=False)
	def __str__(self):
		return self.class_user.username + str(self.pk)

#  iamgaein classroom
class Image_Classroom(models.Model):
	image_Class = models.ImageField(max_length=255, upload_to='classroom', null=True, blank=True)

class Image_class_picture(models.Model):
	image_picture = models.ImageField(max_length=255, upload_to='classroom', null=True, blank=True)



# user = Class_User.objects.get(pk='1')

# o = user.image_user_set.all
# print(o)

# user = Class_User.objects.all()

# b = user.image_rep

# print(b)

