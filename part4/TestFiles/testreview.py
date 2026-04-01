#!/usr/bin/python3
from models.review import Review  # Adapte l'import selon ton dossier

# Simulation de classes Place et User minimalistes pour le test
class MockPlace: pass
class MockUser: pass

def test_review_creation():
    print("--- Test 1: Création valide ---")
    p = MockPlace()
    u = MockUser()
    try:
        r = Review("Superbe endroit, j'ai adoré !", 5, p, u)
        print(f"✅ Succès : ID {r.id}")
        print(f"   Texte: {r.text}")
        print(f"   Note: {r.rating}/5")
    except Exception as e:
        print(f"❌ Échec inattendu : {e}")

def test_invalid_rating():
    print("\n--- Test 2: Note invalide (6/5) ---")
    p = MockPlace()
    u = MockUser()
    try:
        r = Review("Cool", 6, p, u)
        print("❌ Échec : La note invalide a été acceptée.")
    except ValueError as e:
        print(f"✅ Succès : L'erreur a bien été levée ({e})")

def test_missing_text():
    print("\n--- Test 3: Texte manquant ---")
    p = MockPlace()
    u = MockUser()
    try:
        r = Review("", 3, p, u)
        print("❌ Échec : Le texte vide a été accepté.")
    except ValueError as e:
        print(f"✅ Succès : L'erreur a bien été levée ({e})")

def test_missing_relations():
    print("\n--- Test 4: Place ou User manquant ---")
    try:
        r = Review("Texte", 3, None, None)
        print("❌ Échec : L'absence de Place/User a été acceptée.")
    except ValueError as e:
        print(f"✅ Succès : L'erreur a bien été levée ({e})")

if __name__ == "__main__":
    test_review_creation()
    test_invalid_rating()
    test_missing_text()
    test_missing_relations()