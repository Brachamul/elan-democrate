from django.db import models

from django.contrib.auth.models import User
from fichiers_adherents.models import Adhérent

import string
import random
def randomly_generated_code(i):
	return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(i))
	# http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python

class Credentials(models.Model):
	user = models.ForeignKey(User) # credentials are linked to one specific user
	email = models.EmailField() # we'll send them an email !
	code = models.CharField(max_length=6, default=randomly_generated_code(6))
	date = models.DateTimeField(auto_now=True)
	attempts = models.PositiveSmallIntegerField(default=0)
	# each time a user attempts to log in with a code, the "attempts" field is incremented

	class Meta :
		verbose_name_plural = "Credentials"

class EmailConfirmationInstance(models.Model):
	adherent = models.ForeignKey(Adhérent) # credentials are linked to one specific user
	email = models.EmailField() # we'll send them an email !
	code = models.CharField(max_length=32, default=randomly_generated_code(32))
	date = models.DateTimeField(auto_now=True)


### maybe enable phone numbers at some point ?
#   phone_regex = RegexValidator(
#	   regex=r'^\+?1?\d{9,15}$', 
#	   message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
#	   )
#   phone_number = models.CharField(validators=[phone_regex], blank=True)