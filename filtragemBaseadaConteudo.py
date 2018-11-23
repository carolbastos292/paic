boats = {"N/M Parintins":              {"higiene": 2,  "Seguranca": 4, "Alimentacao": 3, "Tarifa": 4.5, "Pontualidade":5},
         "F/B Ana Beatriz V":          {"higiene": 3,  "Seguranca": 2, "Alimentacao": 1.5, "Tarifa": 1.5, "Pontualidade":3},
         "B/M El Shadai":              {"higiene": 4.5,  "Seguranca": 1, "Alimentacao": 1.5, "Tarifa": 2.5, "Pontualidade":4},
         "B/M Vitória da Conquista":   {"higiene": 1,  "Seguranca": 2, "Alimentacao": 2.5, "Tarifa": 2.5, "Pontualidade":5},
         "N/M Comte Sev. Ferreira":    {"higiene": 2,  "Seguranca": 3, "Alimentacao": 3, "Tarifa": 3.5, "Pontualidade":3},
         "N/M Monte Sinai II":         {"higiene": 3.5,  "Seguranca": 1, "Alimentacao": 4.5, "Tarifa": 3, "Pontualidade":1},
         "N/M PP Maués":               {"higiene": 4,  "Seguranca": 2, "Alimentacao": 5, "Tarifa": 5, "Pontualidade":2},
         "F/ Monte Cristo":            {"higiene": 2,  "Seguranca": 3, "Alimentacao": 3, "Tarifa": 3, "Pontualidade":4},
         "N/M Leão de Judá II":        {"higiene": 5.5,  "Seguranca": 4, "Alimentacao": 2, "Tarifa": 2, "Pontualidade":4},
         "F/B M. Monteiro II":         {"higiene": 2,  "Seguranca": 2, "Alimentacao": 1, "Tarifa": 1, "Pontualidade":5},
         "B/M São Francisco do Anamã": {"higiene": 3,  "Seguranca": 3, "Alimentacao": 2.5, "Tarifa": 4, "Pontualidade":4},
         "B/M Stenio Araújo":          {"higiene": 2.5,  "Seguranca": 3, "Alimentacao": 1, "Tarifa": 2.5, "Pontualidade":3},
         "F/B Diamante":               {"higiene": 3,  "Seguranca": 2.5, "Alimentacao": 2, "Tarifa": 3, "Pontualidade":4},
         "B/M PP Maués III":           {"higiene": 2,  "Seguranca": 1, "Alimentacao": 3, "Tarifa": 4, "Pontualidade":3},
         "N/M Parintins":              {"higiene": 4,  "Seguranca": 1, "Alimentacao": 4, "Tarifa": 5, "Pontualidade":5},
         "N/M Izabel I":               {"higiene": 3.5,  "Seguranca": 2, "Alimentacao": 5, "Tarifa": 3, "Pontualidade":5},
         "N/M M. Fernandes":           {"higiene": 2,  "Seguranca": 3, "Alimentacao": 5, "Tarifa": 2.5, "Pontualidade":2},
         "N/M Sagrado Cor. de Jesus":  {"higiene": 1,  "Seguranca": 4, "Alimentacao": 5, "Tarifa": 1, "Pontualidade":5},
         "M/S Iberostar Grand Amazon": {"higiene": 4,  "Seguranca": 1, "Alimentacao": 3, "Tarifa": 2.5, "Pontualidade":3},
         "N/M Cisne Branco":           {"higiene": 5,  "Seguranca": 5, "Alimentacao": 2, "Tarifa": 1.5, "Pontualidade":5}}

def manhattan(rating1, rating2):
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance

"""Função para encontrar a pessoa mais próxima"""
def computeNearestNeighbor(username, users):
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
    distances.sort()
    return distances

def recommend(username, users):
    """Pega a lista de Recomendações """
    nearest = computeNearestNeighbor(username, users)[0][1]
    recommendations = []
    neighborRatings = users[nearest]
    userRatings = users[username]
    for barco in neighborRatings:
        if not barco in userRatings:
            recommendations.append((barco, neighborRatings[barco]))
    return sorted(recommendations,
                  key=lambda barcoTuple: barcoTuple[1],
                  reverse = True)
         
            
        
            

         



















         


