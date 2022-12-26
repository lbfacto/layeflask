
import json
import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ crée une connexion à la base de données SQLite
        specifié par le chemin du fichier passé en argument
    :param db_file: chemin du fichier db
    :return: un objet connexion ou renvoie none
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file) # on crée l'objet connexion
        return conn
    except Error as e: # gestion de l'erreur
        print(e) # affichage du message d'erreur
 
    return conn
 
 
def eval_type(var):
    """ renvoie le type de données sqlite correspondant à la variable passée en argument
    """
    if (type(var) is bool) or (type(var) is int): # si la valeur est du type booléen ou integer
        return 'integer'  
    else: # sinon
        if type(var) is float: # si la valeur est du type float
            return 'real'
        else: # sinon
            return 'text'
 
def create_table(conn, json_data, table_name, column_name, fk_column_name):
    """ crée une table en fonction des données json contenues dans la variable objet json_data
    arguments:
    conn: objet permettant la connexion à la base de données sqlite
    json_data: données json dont on extrait les noms des colonnes et leur type de données
    table_name: nom de la table à créer
    column_name: nom de la colonne de la table dans le cas ou il y a une seule colonne à ajouter en plus des clés
    fk_column_name: nom de la colonne clé étrangère
    """
 
    try:
 
        c = conn.cursor()
 
        id_column_name = table_name +  "_id"
        create_table_sql = """ CREATE TABLE IF NOT EXISTS """ + table_name + "(" + id_column_name + " integer PRIMARY KEY AUTOINCREMENT," # on ajoute le nom de la colonne identifiant et son type à la chaine sql
 
        if fk_column_name!='': # si la table doit comporter une clé étrangère
            create_table_sql = create_table_sql + "[" + fk_column_name + "] integer," # on ajoute le nom de la colonne clé étrangère et son type à la chaine sql
        else:
            column_name = table_name
 
        if type(json_data) is dict: # si c'est un dictionnaire
            for k,v in json_data.items(): # on parcourt ses éléments
                if (type(v) is not list) & (type(v) is not dict) & (v is not None): # si l'élément est une valeur
                    create_table_sql = create_table_sql + " [" + k + "] " + eval_type(v) + "," # on ajoute le nom de la colonne et son type à la chaine sql
        else: # sinon
            if (type(json_data) is list) & (json_data!=[]): # si c'est une liste non vide
                if (type(json_data[0]) is dict): # et si c'est une liste de dictionnaires
                    for k,v in json_data[0].items(): # on parcourt ses éléments
                        if (type(v) is not list) & (type(v) is not dict) & (v is not None): # si l'élément est une valeur
                            create_table_sql = create_table_sql + " [" + k + "] " + eval_type(v) + "," # on ajoute le nom de la colonne et son type à la chaine sql
                else: # sinon
                    create_table_sql = create_table_sql + " [" + column_name + "] " + eval_type(json_data[0]) + "," # on ajoute le nom de la colonne et son type à la chaine sql
            else:
                create_table_sql = create_table_sql + " [" + column_name + "] " + eval_type(json_data) + "," # on ajoute le nom de la colonne et son type à la chaine sql
 
        create_table_sql = create_table_sql[0:-1] + ")" # on constitue la chaine sql finale en ajoutant une parenthèse à la fin
 
        c.execute(create_table_sql) # on exécute le sql
 
        conn.commit() # on aussure que les données sont à jour
 
        return True
 
    except Error as e: # gestion d'erreur
        print(e) # message affiché en cas d'erreur
        return False
 
 
def add_data(conn, json_data, table_name, column_name, id_column_name, id_column_value, fk_column_name, fk_column_value):
    """ crée une table en fonction des données json contenues dans la variable objet json_data
    arguments :
    conn: objet permettant la connexion à la base de données sqlite
    json_data: données json dont on extrait les noms des colonnes et leur type de données
    table_name: nom de la table à créer
    column_name: nom de la colonne de la table dans le cas ou il y a une seule colonne à ajouter en plus des clés
    id_column_name: nom de la colonne identifiant 
    id_column_value: valeur de la colonne identifiant 
    fk_column_name: nom de la colonne clé étrangère
    fk_column_value: valeur de la colonne clé étrangère
    """
 
    try:
 
        c = conn.cursor()
 
        string_values = '('
        values = ()
 
        insert_table_sql = """ INSERT INTO """ + table_name + "([" + id_column_name + "]," # on ajoute le nom de la colonne identifiant et son type à la chaine sql
        string_values =  string_values  + '?,' # on constitue la liste des paramètres de la clause values dans la chaine sql
        values = values + (id_column_value,)
 
        if fk_column_name!='': # si la table doit comporter une clé étrangère
            insert_table_sql = insert_table_sql + "[" + fk_column_name + "]," # on ajoute le nom de la colonne à la chaine sql
            string_values =  string_values  + '?,' # on constitue la liste des paramètres de la clause values dans la chaine sql
            values = values + (fk_column_value,)
        else:
            column_name = table_name
 
        if type(json_data) is dict: # si c'est un dictionnaire
 
            for k,v in json_data.items(): # on parcourt ses éléments
                if (type(v) is not list) & (type(v) is not dict) & (v is not None):
                    insert_table_sql = insert_table_sql + " [" + k + "]," # on ajoute le nom de la colonne à la chaine sql
                    string_values =  string_values  + '?,' # on constitue la liste des paramètres de la clause values dans la chaine sql
                    values = values + (v,)
 
        else:
            if (type(json_data) is list) & (json_data!=[]): # si c'est une liste non vide
                if (type(json_data[0]) is dict): # et si c'est une liste de dictionnaires
                    for k,v in json_data[0].items(): # on parcourt ses éléments
                        if (type(v) is not list) & (type(v) is not dict) & (v is not None): # si l'élément est une valeur
                            insert_table_sql = insert_table_sql + " [" + k + "]," # on ajoute le nom de la colonne à la chaine sql
                            string_values =  string_values  + '?,' # on constitue la liste des paramètres de la clause values dans la chaine sql
                            values = values + (v,)
                else: # sinon
                    column_value = json_data[0]
                    insert_table_sql = insert_table_sql + " [" + column_name + "]," # on ajoute le nom de la colonne à la chaine sql
                    string_values =  string_values  + '?,' # on constitue la liste des paramètres de la clause values dans la chaine sql
                    values = values + (column_value,)
            else: # sinon
                column_value = json_data
                insert_table_sql = insert_table_sql + " [" + column_name + "]," # on ajoute le nom de la colonne à la chaine sql
                string_values =  string_values  + '?,' # on constitue la liste des paramètres de la clause values dans la chaine sql
                values = values + (column_value,)
 
        insert_table_sql = insert_table_sql[0:-1] + ")" 
        string_values =  string_values[0:-1] + ')'
 
        insert_table_sql = insert_table_sql + ' VALUES' + string_values # on constitue la chaine sql finale en ajoutant la clause VALUES
 
        c.execute(insert_table_sql,values) # on exécute le sql
 
        conn.commit() # on s'aussure que les données sont à jour
 
    except Error as e: # gestion d'erreur
        print(e) # message affiché en cas d'erreur
 
def get_id(conn, table_name, id_column_name):
 
    cur = conn.cursor()
 
    cur.execute("SELECT max(" + id_column_name + ") as id_max FROM " + table_name)
 
    data=cur.fetchone()
 
    if data[0]is None:
        return 1
    else:            
        return data[0] + 1    
 
 
def create_database(conn, json_data, table_name, column_name='', fk_column_name='', fk_column_value=0):
    """ crée la base de données sqlite en fonction des données json contenues dans la variable objet json_data
    arguments :
    conn: objet permettant la connexion à la base de données sqlite
    json_data: données json dont on extrait les noms des colonnes et leur type de données
    table_name: nom de la table à créer
    column_name: nom de la colonne de la table dans le cas ou il y a une seule colonne à ajouter en plus des clés, argument optionnel.
    fk_column_name: nom de la colonne clé étrangère, argument optionnel.
    fk_column_value: valeur de la colonne clé étrangère, argument optionnel.
    """
 
    if type(json_data) is list: # si c'est une liste
 
        # on crée la table dans la base sqlite
        create_table(conn, json_data, table_name, column_name, fk_column_name)
 
        for element in json_data: # on parcourt la liste des éléments de la liste
            create_database(conn, element, table_name, column_name, fk_column_name, fk_column_value) # on appelle la fonction avec comme argument l'élément de la liste
    else:                
        if type(json_data) is dict: # si c'est un dictionnaire
            # on crée la table dans la base sqlite
            create_table(conn, json_data, table_name, column_name, fk_column_name)            
 
            id_column_value = get_id(conn, table_name, table_name + '_id') # on récupère la valeur de l'identifiant
            # on ajoute les données du dictionnaire dans la table nouvellement crée
            add_data(conn, json_data, table_name, column_name, table_name + '_id', id_column_value, fk_column_name, fk_column_value)
 
            fk_column_name =  table_name + '_fk' # nom de la colonne clé étrangère
            fk_column_value = id_column_value # valeur de la colonne clé étrangère
 
            # on parcourt les éléments du dictionnaire
            for k, v in json_data.items():                
                column_name = k
                if (type(v) is list) or (type(v) is dict): # si l'élément est une valeur
                    create_database(conn, v, table_name + '_' + column_name, column_name, fk_column_name, fk_column_value) # on appelle la fonction avec comme argument l'élément du dictionnaire
 
 
 
def main(): # fonction principale
 
    database = r"C:\sqlite\db\sunuvilles.db" # chemin de la base de données
 
    # création de la connexion à la base de données sqlite
    conn = create_connection(database)
 
    # si la connexion a été réalisée
    if conn is not None:
 
        with open('ville.json', 'r', encoding='utf-8') as jsonfile: # on ouvre le fichier json situé dans le même dossier que le script python
 
            json_data = json.load(jsonfile) # on charge les données json dans une variable objet
            #create_database(conn, json_data, table_name, column_name='', fk_column_name='', fk_column_value=0)
            create_database(conn, json_data, 'ville') # on créé et on alimente la base de données sqlite        
 
    else:
        print("Erreur! impossible de créer la connexion à la base !")
 
 
if __name__ == '__main__':
    main()