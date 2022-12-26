import networkx as nx
from matplotlib import pyplot as plt
import pickle

S ={"dakar": {"pikine": 12, "guediawaye": 13},
    "pikine":{"dakar": 12, "keur massar" : 13, "rufisque": 18, "guediawaye":4},
    "guediawaye": {"pikine": 4, "dakar":13, "keur massar": 8},
    "keur massar":{"pikine":13, "guediawaye":8, "rufisque":11, "tivaouane":76, "kebemer":112},
    "rufisque":{"pikine":18, "keur massar":11, "thies":44, "mbour":68, "tivaouane":81},
    "mbour":{"rufisque":68, "thies":71},
    "thies":{"rufisque":44, "mbour":71, "tivaouane": 24, "bambey":65},
    "tivaouane":{"thies":24,"kebemer":63,"keur massar":76, "rufisque":81},
    "bambey":{"thies":65, "fatick":42, "diourbel":25},
    "kebemer":{"tivaouane":63,"louga":37,"mbacke":10, "keur massar":112},
    "louga":{"kebemer":37,"linguere":129, "saint louis":72},
    "saint louis":{"louga":72, "dagana":127},
    "linguere":{"louga":129, "mbacke":120, "ranerou":132},
    "mbacke":{"kebemer":100, "gossas": 64, "diourbel": 40, "kaffrine":108,"linguere":120},
    "diourbel":{"bambey":25, "fatick": 65, "gossas":27, "mbacke":40},
    "fatick":{"gossas": 50, "bambey":42, "diourbel": 65, "kaolack":46,"foudiougne":24},
    "gossas":{"fatick":50, "diourbel":27,"mbacke":64, "kebemer":100, "kaolack":38},
    "foudiougne":{"fatick":24},
    "kaolack":{"gossas":38, "fatick":46, "nioro du rip":56, "birkilane":39, "bignona":228,"ziguinchor":228},
    "birkilane":{"kaolack":39, "kaffrine":24},
    "kaffrine":{"birkilane":24, "koungheul":85, "mbacke":108, "malem-hodar":29},
    "koungheul":{"kaffrine":85, "malem-hodar":59, "koumpentoum":27},
    "malem-hodar":{"kaffrine":29, "koungheul":59},
    "koumpentoum":{"koungheul":27, "tambacounda":102},
    "tambacounda":{"koumpentoum":102,"velinguara":95,"kedougou":234,"goudiry":115},
    "velinguara":{"tambacounda":95, "kolda":132},
    "kedougou":{"tambacounda":234,"salemata":77,"saraya":50},
    "salemata":{"kedougou":77},
    "saraya":{"kedougou":50},
    "goudiry":{"tambacounda":115, "bakel":113},
    "bakel":{"goudiry":113, "matam":155},
    "matam":{"bakel":155,"ranerou":93, "podor":243,"dagana":292},
    "ranerou":{"matam":93, "linguere":132},
    "dagana":{"matam":292, "podor":95, "saint louis":127},
    "podor":{"dagana":95, "matam":243},
    "bignona":{"kaolack":228,"ziguinchor":33, "bounkiling":69},
    "ziguinchor":{"bignona":33,"oussouye":43,"goudompe":45},
    "oussouye":{"ziguinchor":43},
    "goudompe":{"ziguinchor":45, "sedhiou":97},
    "sedhiou":{"goudompe":97, "bounkiling":50,"kolda":146,"medina yero foula":111},
    "bounkiling":{"bignona":69,"kolda":108,"sedhiou":50},
    "kolda":{"bounkiling":108,"sedhiou":146,"medina yero foula":58,"velinguara":132},
    "medina yero foula":{"sedhiou":111,"kolda":58},
    "nioro du rip":{"kaolack":56}}
     
    



def dijkstra(S, source='dakar', destination ='thies'):
    assert all(S[u][v] >= 0 for u in S.keys() for v in S[u].keys())
    precedent = {x:None for x in S.keys()}
    dejaTraite = {x:False for x in S.keys()}
    distance =  {x:float('inf') for x in S.keys()}
    distance[source] = 0
    a_traiter = [(0, source)]
    while a_traiter:
        dist_noeud, noeud = a_traiter.pop()
        if not dejaTraite[noeud]:
            dejaTraite[noeud] = True
            for voisin in S[noeud].keys():
                dist_voisin = dist_noeud + S[noeud][voisin]
                if dist_voisin < distance[voisin]:
                    distance[voisin] = dist_voisin
                    precedent[voisin] = noeud
                    a_traiter.append((dist_voisin, voisin))
        a_traiter.sort(reverse=True)
    return distance, precedent

G = nx.Graph(S)
#G = nx.from_dict_of_lists(S)

nx.draw(G, with_labels=True,font_size=5)
#plt.figure(figsize=(30, 30)) 
nx.dijkstra_path(G,'dakar','louga')
plt.show()

distance, precedent = dijkstra(S)
path = nx.dijkstra_path(G, 'dakar','louga')
print('Distances minimum :',distance)
print('Liste des précédents :', precedent)
nx.dijkstra_path(G,'dakar','louga')




 

