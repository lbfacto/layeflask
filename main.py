from flask import Flask, render_template, request
from dijkstra import dijkstra
import networkx as nx
import json
from dijkstra import*
import sqlite3
import csv
import pandas as pd

G = pd.read_pickle("Graph.pkl")  

conn = sqlite3.connect('sunuvilles.db')
cur = conn.cursor()
#cur.execute('SELECT diourbel FROM ville_gossas')
sunuvilles = cur.fetchall()
for sunuvilles in sunuvilles:
      print(f'{sunuvilles} ')
      



app = Flask(__name__)
G = nx.Graph()


@app.route('/')

def index():
    return(render_template("index.html"))


@app.route('/d')

def dijkstra():
    global G
    source=request.args['sourec'].lower().strip()
    destination=request.args['destination'].lower().strip()
    
    
    path = nx.dijsktra_path(G, source='dakar', destination='thies', weight='weignt')
    
    return json.dump(path)

    
    #return(render_template("form.html"))
if __name__ == "__main":
    
    #global G
    
    with open('ville.json', 'rb') as f:
        reader = json.reader(f)
        nodes=list(reader)       
    
    for i in nodes:
             
        G.add_node(i[0])    
    #app.run(debug=True)    
    with open('ville.josn', 'rb') as f: 
        reader = json.reader(f)
        edge =list(reader)    
    
    for i in edge:
        G.add_edge(i[0], i[1]) 
#print('Liste des précédents :', precedent)

    #app.run(host='0.0.0.0', port=3000, use_reloader=False)
    app.run(debug=True)    




#path = nx.dijkstra_path(G, 'dakar','louga')
#print('Distances minimum :',distance)
#print('Liste des précédents :', precedent)
#nx.dijkstra_path(G,'dakar','kolda')     
    
    #return(render_template("form.html"))  
conn.close()



