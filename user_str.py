from django.contrib.auth.models import User

# Parce que le "username" est ici utilisé comme numéro adhérent
# Ce code change l'affichage standard d'un "User" du "username" vers le "profil.nom_courant"
def user_str(self): return self.profil.nom_courant
User.__str__ = user_str