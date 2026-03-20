## Tests HBNB – Part 3

Ce document contient toutes les étapes pour tester la configuration de la base de données et les données initiales de HBNB.


# 1️ Pré-requis

Python 3.12

Virtual environment activé :

source .venv/bin/activate

Base MySQL hbnb_db créée et utilisateur hbnb_user configuré avec le bon mot de passe.

Tables initialisées (users, amenities, places, etc.).


# 2️ Test de connexion MySQL

Ouvre un terminal et connecte-toi avec l’utilisateur HBNB :

mysql -u hbnb_user -p

Mot de passe : hbnb_password

Vérifie que la connexion fonctionne et que la base existe :

SHOW DATABASES;

Vérifie la présence de la base :

USE hbnb_db;
SHOW TABLES;

Tu devrais voir les tables : users, amenities, places, reviews, etc.


# 3️ Test des données initiales
3.1 Admin

Vérifie la présence de l’utilisateur admin :

SELECT id, email, first_name, last_name, is_admin FROM users WHERE email='admin@hbnb.io';

Résultat attendu :

id	email	first_name	last_name	is_admin
36c9050e-ddd3-4c3b-9731-9f487208bbc1	admin@hbnb.io
	Admin	HBnB	1

3.2 Amenities

Vérifie les amenities :

SELECT id, name FROM amenities;

Résultat attendu :

id	name
a1f0d6e5-9e12-4b3a-bfd7-1a2e5c3f8d12	WiFi
b2e1c7f3-3d45-4f2b-91ae-8b7d9c1e0f34	Swimming Pool
c3f2d8a4-6a78-4d1c-ae9b-3d2f4b5e7a89	Air Conditioning
3.3 Vérification des places et relations
SELECT id, name, city_id, user_id FROM places LIMIT 5;
SELECT place_id, amenity_id FROM place_amenity LIMIT 5;

Vérifie que chaque place a au moins un utilisateur associé (user_id) et que les relations place_amenity sont cohérentes.


# 4️ Test avec Python (optionnel depuis le terminal)

Pour vérifier que SQLAlchemy fonctionne dans ton projet :

python

Puis dans l’interpréteur Python :

from app import app, db
from app.models import User, Amenity

# Connexion
db.session.execute("SELECT 1")
print("Connexion MySQL OK")

# Test admin
admin = User.query.filter_by(email='admin@hbnb.io').first()
print("Admin trouvé :", admin.email if admin else "Non trouvé")

# Test amenities
amenities = Amenity.query.all()
print("Amenities :", [a.name for a in amenities])


# 5️ Vérification des logs

Lance le serveur HBNB :

python run.py

Vérifie qu’il n’y a aucune erreur de connexion à MySQL.

Les warnings sur Review.place peuvent apparaître mais ne bloquent pas l’exécution.
