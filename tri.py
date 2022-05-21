# from itertools import combinations
from operator import attrgetter
# from classes import Aliment

# Elo rating algo
import math

# Function to calculate the Probability
def Probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))

# Function to calculate Elo rating
# K is a constant.
# d determines whether
# Player A wins or Player B.
def EloRating(Ra, Rb, K, d):

	# To calculate the Winning
	# Probability of Player B
	Pb = Probability(Ra, Rb)

	# To calculate the Winning
	# Probability of Player A
	Pa = Probability(Rb, Ra)

	# Case -1 When Player A wins
	# Updating the Elo Ratings
	if (d == 1) :
		Ra = Ra + K * (1 - Pa)
		Rb = Rb + K * (0 - Pb)


	# Case -2 When Player B wins
	# Updating the Elo Ratings
	else :
		Ra = Ra + K * (0 - Pa)
		Rb = Rb + K * (1 - Pb)


	print("Updated Ratings:-")
	print("Ra =", round(Ra, 6)," Rb =", round(Rb, 6))

	return Ra,Rb

def matchs(a1,a2,w):
    
    if w == 1:
        r1,r2 = EloRating(a1.elo,a2.elo, 30, 1)
    else:
        r1,r2 = EloRating(a1.elo,a2.elo, 30, 0)
    
    a1.elo = r1 ; a2.elo = r2

def tri(liste, order):
    att = attrgetter('elo')
    T = sorted(liste, key=attrgetter('elo'), reverse=order)
    return [(a.nom,att(a)) for a in T]

# =============================================================================

# =============================================================================
# def matchs(a1,a2,w,str_att):
#     
#     att = attrgetter(str_att)
#     
#     if w == 1:
#         r1,r2 = EloRating(att(a1),att(a2), 30, 1)
#     else:
#         r1,r2 = EloRating(att(a1),att(a2), 30, 0)
#     
#     setattr(a1, str_att, r1) ; setattr(a2, str_att, r2)   
# 
# 
# =============================================================================



# =============================================================================
# def tri_par_opposition(liste, str_att,confrontation):
#     mes_aliments = liste # sample([Aliment(nom) for nom in liste], 4)
#     matches = list(combinations(mes_aliments, 2))
#     
#     for [a1,a2] in matches:
#         w = confrontation(a1,a2,str_att)
#         matchs(a1,a2,w,str_att)
#             
#     return mes_aliments
# 
# def tri_preferences(liste):
#     def pref(a1,a2,str_attr):
#         return int(input("{} (1) vs {} (2)".format(a1.nom,a2.nom)))
#     return tri_par_opposition(liste, 'elo', pref)
#     
# =============================================================================
# TODO : généraliser la fonction de tri par preference à un nombre de critères quelconques (les attributs des aliments)
# =============================================================================
# 
# def tri_critere(liste, critere, order):
#     att = attrgetter(critere)
#     T = sorted(liste, key=attrgetter(critere), reverse=order)
#     return [(a.nom,att(a)) for a in T]
# 
# =============================================================================
# =============================================================================
