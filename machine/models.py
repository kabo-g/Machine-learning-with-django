from django.db import models

# Create your models here.


class BreastCancerChecker(models.Model):
	"""mean_radius 	mean_texture 	mean_perimeter 	mean_area 	mean_smoothness """

	name = models.CharField(max_length=255, null=True)
	surname = models.CharField(max_length=255, null=True)
	mean_radius = models.FloatField(default=17.99, null=True)
	mean_texture = models.FloatField(default=10.38, null=True)
	mean_perimeter = models.FloatField(default=122.80, null=True)
	mean_area = models.FloatField(default=1001.0, null=True)
	mean_smoothness = models.FloatField(default=0.11840, null=True)

	def __str__(self):
		return self.name+ " "+ self.surname