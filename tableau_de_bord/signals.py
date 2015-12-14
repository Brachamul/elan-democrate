# these signals feed the dashboard, they are imported by the __init__.py file

from django.dispatch import receiver
from django.db.models.signals import post_save

from auth_with_one_time_code.models import EmailConfirmationInstance

from tableau_de_bord.models import Email

@receiver(post_save, sender=EmailConfirmationInstance) 
def email_confirmation_attempt(sender, created, **kwargs):
	if created :
		email_confirmation_instance = kwargs.get('instance')
		author = "adherent n°" + str(email_confirmation_instance.adherent.num_adhérent)
		new_email = Email(
			template="message de confirmation d'adresse email",
			author=author,
			destination=email_confirmation_instance.email
			)
		new_email.save()
		


# Démarrage des signaux pour nourrir le tableau de bord
#		from tableau_de_bord import signals

