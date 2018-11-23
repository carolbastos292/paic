users = {"Talisson": 	{"Maresia II": 1, "Maresia VII": 2, "Fênix": 3, "Monte Sinai": 5, "Estrela de Davi": 3 },
	 "Igor": 	{"Maresia II": 2, "Maresia VII": 2, "Expresso Kedson Araújo": 3, "Monte Sinai": 5, "Estrela de Davi": 3 },
	 "Flavia": 	{"Maresia VII": 2, "Maresia VII": 2, "Expresso Kedson Araújo": 4, "Monte Sinai": 5, "Estrela de Davi": 5 },
	 "Oseias": 	{"Fenix": 5, "Maresia VII": 2, "Expresso Kedson Araújo": 4, "Monte Sinai": 3, "Estrela de Davi": 2 },
         "Jackson": 	{"Monte Sinai": 5, "Maresia VII": 2, "Expresso Kedson Araújo": 3, "Monte Sinai": 1, "Estrela de Davi": 3 },
	 "Ane": 	{"Estrela de Davi": 5, "Maresia VII": 1, "Fênix": 3, "Elyon Fernandes": 5, "Estrela de Davi": 3 },
	 "Carol": 	{"Leao de Juda": 5, "Maresia VII": 2, "Fênix": 2, "Elyon Fernandes": 5, "Estrela de Davi": 3 },
	 "Bill": 	{"Eliyon Fernandes": 5, "Maresia VII": 2, "Fênix": 4, "Elyon Fernandes": 3, "Estrela de Davi": 4 },
	 "Chan": 	{"A Nunes": 5, "Maresia VII": 3, "Fênix": 3, "Monte Sinai": 5, "Estrela de Davi": 4 },
	 "Daniel": 	{"Jesus te Ama": 5, "Maresia VII": 4, "Fênix": 3, "Monte Sinai": 2, "Estrela de Davi": 4 },
	 "Andrea": 	{"Moreira da Silva III": 5, "Maresia VII": 2, "Fênix": 3, "Monte Sinai": 5, "Estrela de Davi": 4 },
	 "Vitor": 	{"Carlos Alberto": 4, "Maresia VII": 1, "Fênix": 3, "Monte Sinai": 3, "Estrela de Davi": 4 },
	 "Hugor": 	{"A Jato 2001": 3, "Maresia VII": 2, "Fênix": 3, "Monte Sinai": 5, "Estrela de Davi": 5 },
	 "Sergio": 	{"Cristal": 2, "Maresia VII": 2, "Leão de Judá": 4, "Monte Sinai": 3, "Estrela de Davi": 2 },
	 "Richardson":  {"Expresso Kedson Araújo": 1, "Maresia VII": 3, "Leão de Judá": 4, "Monte Sinai": 1, "Estrela de Davi": 3 },
	 "Raimundo": 	{"Maresia II": 1, "Maresia VII": 2, "Leão de Judá": 3, "Monte Sinai": 5, "Estrela de Davi": 3 },
	 "Andresa": 	{"Moreira da Silva III": 1, "Maresia VII": 3, "Fênix": 3, "Monte Sinai": 5, "Estrela de Davi": 3 },
	 "Polly": 	{"Maresia II": 4, "Maresia VII": 4, "Fênix": 4, "Monte Sinai": 5, "Estrela de Davi": 3 }}

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




