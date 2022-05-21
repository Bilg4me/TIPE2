from data_dump import ficheTechnique

class Aliment:
    
    def __init__(self, m_nom):
        self.nom = m_nom
        (self.id, self.image, self.nutriments) = ficheTechnique(m_nom)
        
        self.elo = 100
        
        self.regimeConvient = self.nutriments['healthLabels']
        self.dangers = self.nutriments['cautions']
        self.poids = self.nutriments['totalWeight']
        self.valNutritionellerbrut = self.nutriments['totalNutrients']
        self.valNutritionellerJournaliere = self.nutriments['totalDaily']
        
        self.lipides = self.valNutritionellerbrut['FAT']['quantity']
        self.calories = self.valNutritionellerbrut['ENERC_KCAL']['quantity']
        self.sucres = self.valNutritionellerbrut['SUGAR']['quantity']
        self.protéines = self.valNutritionellerbrut['PROCNT']['quantity']
        self.eau = self.valNutritionellerbrut['WATER']['quantity']
        
        self.tempsdigestion = 0
        self.famille = ""
        self.maxvaj = 0
        self.nutriscore = 0 
        
        
    def __str__(self):
        return "{}".format(self.nom)

class Utilisateur:

    def __init__(self, m_id,a,s,grp,al,ns):
        self.id = m_id
        self.age = a
        self.sexe = s
        self.grpsanguin = grp
        self.allergies = al
        self.niveausportif = ns
        self.preferences = []
        self.critere_privilegiés = []
    def __str__(self):
        return "je suis {}, j'ai {}, et plein d'autre parametres".format(self.id, self.age)

class Repas:
    
    def __init__(self, m_liste):
        self.liste_aliments = m_liste
        self.nutriscore = 0
    
    def ordonner_aliments(self):
        pass
