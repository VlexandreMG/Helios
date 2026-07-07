import psycopg2
from psycopg2 import OperationalError

class DBConnection:
    def __init__(self):
        # Configuration de tes identifiants PostgreSQL locaux
        self.host = "localhost"
        self.database = "helios_db"
        self.user = "postgres"
        self.password = "postgres"  # À remplacer par ton vrai MDP
        self.port = "5432"
        self.connexion = None

    def connecter(self):
        """Établit la connexion avec la base de données PostgreSQL."""
        if self.connexion is None:
            try:
                self.connexion = psycopg2.connect(
                    host=self.host,
                    database=self.database,
                    user=self.user,
                    password=self.password,
                    port=self.port
                )
                print(" Connexion à PostgreSQL réussie !")
            except OperationalError as e:
                print(self.connexion) # Sécurité d'affichage
                print(f" Erreur lors de la connexion à la BDD : {e}")
                self.connexion = None
        return self.connexion

    def deconnecter(self):
        """Ferme proprement la connexion et libère les ressources."""
        if self.connexion:
            self.connexion.close()
            print(" Connexion PostgreSQL fermée proprement.")
            self.connexion = None