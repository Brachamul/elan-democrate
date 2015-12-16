import random

from django.core import mail
from django.test import TestCase, RequestFactory

from autofixture import AutoFixture

from django.contrib.auth.models import User
from fichiers_adherents.models import Adherent

from django.contrib.messages.storage.fallback import FallbackStorage

#	from models import *
from .views import signup

class RegistrationTestCases(TestCase):

	def setUp(self):

		self.factory = RequestFactory()
		self.adherents = AutoFixture(Adherent).create(100) # On crée 100 faux adhérents

	def test_registering_new_user_from_existing_adherent(self):
		for adherent in self.adherents :
			# On teste au pif le mail ou le numéro
			if random.choice([True, False]) :
				key = adherent.email
			else :
				key = adherent.num_adhérent

			request = self.factory.post(reverse('signup'), data={'numero_ou_email': 'key'})
			setattr(request, 'session', 'session')
			messages = FallbackStorage(request)
			setattr(request, '_messages', messages)

			signup(request)

		print(mail.outbox)
