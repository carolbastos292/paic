avaliacoesUsuario = {
         'Ana': 
		{'Maresia II': 2.5, 
		 'N/M Leão de Judá II': 3.5,
		 'F/B M. Monteiro II': 3.0, 
		 'B/M São Francisco do Anamã': 3.5, 
		 'B/M Stenio Araújo': 2.5, 
		 'F/B Diamante': 3.0},
	 
	  'Marcos': 
		{'Maresia II': 3.0, 
		 'N/M Leão de Judá II': 3.5, 
		 'F/B M. Monteiro II': 1.5, 
		 'B/M São Francisco do Anamã': 5.0, 
		 'F/B Diamante': 3.5, 
		 'B/M Stenio Araújo': 3.0}, 

	  'Pedro': 
	        {'Maresia II': 2.5, 
		 'N/M Leão de Judá II': 3.0,
		 'B/M São Francisco do Anamã': 3.5, 
		 'F/B Diamante': 4.0},
			 
	  'Claudia': 
		{'Maresia II': 3.5, 
		 'N/M Leão de Judá II': 3.5,
		 'F/B M. Monteiro II': 3.0, 
		 'B/M São Francisco do Anamã': 4.0, 
		 'B/M Stenio Araújo': 2.5,
                 'F/B Diamante': 4.5},
				 
	  'Adriano': 
		{'Maresia II': 3.0, 
		 'N/M Leão de Judá II': 4.0, 
		 'F/B M. Monteiro II': 2.0, 
		 'B/M São Francisco do Anamã': 3.0, 
		 'F/B Diamante': 3.0,
		 'B/M Stenio Araújo': 2.0}, 

	  'Janaina': 
                 {'Maresia II': 3.0, 
                  'N/M Leão de Judá II': 4.0,
                  'B/M São Francisco do Anamã': 5.0,  
                  'B/M Stenio Araújo': 3.5,
                  'F/B Diamante': 3.0},
              
	  'Leonardo': 
                {'N/M Leão de Judá II':4.5,
                 'B/M São Francisco do Anamã':4.0,
                 'B/M Stenio Araújo': 1.0},
}

avaliacoesBarcos = {
        'Maresia II': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Pedro': 2.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0 },
	 
	 'N/M Leão de Judá II': 
		{'Ana': 3.5, 
		 'Marcos': 3.5,
		 'Pedro': 3.0, 
		 'Claudia': 3.5, 
		 'Adriano': 4.0, 
		 'Janaina': 4.0,
		 'Leonardo': 4.5 },
				 
	 'F/B M. Monteiro II': 
		{'Ana': 3.0, 
		 'Marcos:': 1.5,
		 'Claudia': 3.0, 
		 'Adriano': 2.0 },
	
	 'B/M São Francisco do Anamã': 
		{'Ana': 3.5, 
		 'Marcos:': 5.0 ,
		 'Pedro': 3.5, 
		 'Claudia': 4.0, 
		 'Adriano': 3.0, 
		 'Janaina': 5.0,
		 'Leonardo': 4.0},
				 
	 'B/M Stenio Araújo': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Claudia': 2.5, 
		 'Adriano': 2.0, 
		 'Janaina': 3.5,
		 'Leonardo': 1.0},
				 
	 'F/B Diamante': 
		{'Ana': 3.0, 
		 'Marcos:': 3.5,
		 'Pedro': 4.0, 
		 'Claudia': 4.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0},
}

from math import sqrt

def euclidiana(base, usuario1, usuario2):
    si = {}
    for item in base[usuario1]:
       if item in base[usuario2]: si[item] = 1

    if len(si) == 0: return 0

    soma = sum([pow(base[usuario1][item] - base[usuario2][item], 2)
                for item in base[usuario1] if item in base[usuario2]])
    return 1/(1 + sqrt(soma))

def getSimilares(base, usuario):
    similaridade = [(euclidiana(base, usuario, outro), outro)
                    for outro in base if outro != usuario]
    similaridade.sort()
    similaridade.reverse()
    return similaridade[0:30]
    
def getRecomendacoesUsuario(base, usuario):
    totais={}
    somaSimilaridade={}
    for outro in base:
        if outro == usuario: continue
        similaridade = euclidiana(base, usuario, outro)

        if similaridade <= 0: continue

        for item in base[outro]:
            if item not in base[usuario]:
                totais.setdefault(item, 0)
                totais[item] += base[outro][item] * similaridade
                somaSimilaridade.setdefault(item, 0)
                somaSimilaridade[item] += similaridade
    rankings=[(total / somaSimilaridade[item], item) for item, total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings[0:30]     

def calculaItensSimilares(base):
    result = {}
    for item in base:
        notas = getSimilares(base, item)
        result[item] = notas
    return result

def getRecomendacoesItens(baseUsuario, similaridadeItens, usuario):
    notasUsuario = baseUsuario[usuario]
    notas={}
    totalSimilaridade={}
    for (item, nota) in notasUsuario.items():
        for (similaridade, item2) in similaridadeItens[item]:
            if item2 in notasUsuario: continue
            notas.setdefault(item2, 0)
            notas[item2] += similaridade * nota
            totalSimilaridade.setdefault(item2,0)
            totalSimilaridade[item2] += similaridade
    rankings=[(score/totalSimilaridade[item], item) for item, score in notas.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
        


























