from flask import Flask, render_template, request
from dijkstra import dijkstra, distance
import networkx as nx
import json
from dijkstra import*
import sqlite3


import flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True
      

path= nx.dijkstra_path


