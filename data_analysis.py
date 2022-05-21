# 1 - Data dump
# 2 - Model selection and evaluation
# 3 - Prediction

# from classes import Aliment
# from random import choice, triangular
# import matplotlib.pyplot as plt
# import numpy as np
# from sklearn import linear_model
# from sklearn.metrics import mean_squared_error, r2_score

# =========================== Data Preprocessing ======================================
# with open('dataatester') as file:
#     fichier = file.readlines()
# 
# def testData():
#     valide = []
#     pas_valide = []
#     for i in range(len(fichier)):
#         nom = fichier[i][:-1]
#         
#         try:
#             a = Aliment(nom)
#             valide.append(nom + '\n')
#         except Exception:
#             pas_valide.append(nom+ '\n')
#         
#     
#     # a.elo = triangular(10,12)*a.calories + triangular(5,7)*a.sucres
#     return valide,pas_valide
# =============================================================================

# Data preprocessing
# =============================================================================
# 
# panier = [ randomAliment() for _ in range(500)]
# 
# nutritional = [(a.calories,a.glucides) for a in panier]
# ranks = [a.elo for a in panier]
# 
# nutritional_train,ranks_train = nutritional[:-100],ranks[:-100]
# nutritional_test,ranks_test = nutritional[-100:],ranks[-100:]
# 
# =============================================================================

# Entrainement du modèle et évaluation
# =============================================================================
# reg = linear_model.LinearRegression()
# reg.fit(nutritional_train,ranks_train)
# ranks_pred = reg.predict(nutritional_test)
# 
# print("Coefficients: \n", reg.coef_)
# # The mean squared error
# print("Mean squared error: %.2f" % mean_squared_error(ranks_test, ranks_pred))
# # The coefficient of determination: 1 is perfect prediction
# print("Coefficient of determination: %.2f" % r2_score(ranks_test, ranks_pred))
# 
# =============================================================================

# ========================== One feature linear model plotting ==========================================
# Plot outputs

# plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
# plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)
# 
# plt.xticks(())
# plt.yticks(())
# 
# plt.show()

# 
# =============================================================================
