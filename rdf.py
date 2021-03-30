#import libs
import json
import rdflib

#load triplestore
def start():
    g=rdflib.graph.ConjunctiveGraph()
    g.parse('Ontologie_version2_xml.owl',format="xml")
    return g

#sparql queries
def listeFontaines(g):
    qres = g.query("""
         
        SELECT ?Name ?Geo_Json ?Coord ?Arrondissements ?Description
        WHERE {
            ?s rdf:type :Fountains .
            ?s :Name ?Name .
            ?s :Geo_Json ?Geo_Json .
            ?s :Coord ?Coord .
            ?s :Arrondissements ?Arrondissements .
            ?s :Description ?Description .
            }""")
    return(qres)

def listeParcs1(g):
    qres = g.query("""
         
        SELECT ?Name ?Geo_Json ?Coord ?Adress ?Arrondissements ?Description ?Portion_Arbres_Hauts ?Horaires_Lundi ?Horaires_Mardi ?Horaires_Mercredi ?Horaires_Jeudi ?Horaires_Vendredi ?Horaires_Samedi  ?Horaires_Dimanche
        WHERE {
            ?s rdf:type :Low_Fresh_Parks .
            ?s :Name ?Name .
            ?s :Geo_Json ?Geo_Json .
            ?s :Coord ?Coord .
            ?s :Adress ?Adress .
            ?s :Arrondissements ?Arrondissements .
            ?s :Description ?Description .
            ?s :Portion_Arbres_Hauts ?Portion_Arbres_Hauts .
            ?s :Horaires_Lundi ?Horaires_Lundi .
            ?s :Horaires_Mardi ?Horaires_Mardi .
            ?s :Horaires_Mercredi ?Horaires_Mercredi .
            ?s :Horaires_Jeudi ?Horaires_Jeudi .
            ?s :Horaires_Vendredi ?Horaires_Venredi .
            ?s :Horaires_Samedi ?Horaires_Samedi .
            ?s :Horaires_Dimanche ?Horaires_Dimanche .
            }""")
    return(qres)

def listeParcs2(g):
    qres = g.query("""
         
        SELECT ?Name ?Geo_Json ?Coord ?Adress ?Arrondissements ?Description ?Portion_Arbres_Hauts ?Horaires_Lundi ?Horaires_Mardi ?Horaires_Mercredi ?Horaires_Jeudi ?Horaires_Vendredi ?Horaires_Samedi  ?Horaires_Dimanche
        WHERE {
            ?s rdf:type :Medium_Fresh_Parks .
            ?s :Name ?Name .
            ?s :Geo_Json ?Geo_Json .
            ?s :Coord ?Coord .
            ?s :Adress ?Adress .
            ?s :Arrondissements ?Arrondissements .
            ?s :Description ?Description .
            ?s :Portion_Arbres_Hauts ?Portion_Arbres_Hauts .
            ?s :Horaires_Lundi ?Horaires_Lundi .
            ?s :Horaires_Mardi ?Horaires_Mardi .
            ?s :Horaires_Mercredi ?Horaires_Mercredi .
            ?s :Horaires_Jeudi ?Horaires_Jeudi .
            ?s :Horaires_Vendredi ?Horaires_Venredi .
            ?s :Horaires_Samedi ?Horaires_Samedi .
            ?s :Horaires_Dimanche ?Horaires_Dimanche .
            }""")
    return(qres)

def listeParcs3(g):
    qres = g.query("""
         
        SELECT ?Name ?Geo_Json ?Coord ?Adress ?Arrondissements ?Description ?Portion_Arbres_Hauts ?Horaires_Lundi ?Horaires_Mardi ?Horaires_Mercredi ?Horaires_Jeudi ?Horaires_Vendredi ?Horaires_Samedi  ?Horaires_Dimanche
        WHERE {
            ?s rdf:type :High_Fresh_Parks .
            ?s :Name ?Name .
            ?s :Geo_Json ?Geo_Json .
            ?s :Coord ?Coord .
            ?s :Adress ?Adress .
            ?s :Arrondissements ?Arrondissements .
            ?s :Description ?Description .
            ?s :Portion_Arbres_Hauts ?Portion_Arbres_Hauts .
            ?s :Horaires_Lundi ?Horaires_Lundi .
            ?s :Horaires_Mardi ?Horaires_Mardi .
            ?s :Horaires_Mercredi ?Horaires_Mercredi .
            ?s :Horaires_Jeudi ?Horaires_Jeudi .
            ?s :Horaires_Vendredi ?Horaires_Venredi .
            ?s :Horaires_Samedi ?Horaires_Samedi .
            ?s :Horaires_Dimanche ?Horaires_Dimanche .
            }""")
    return(qres)

def listeActiv(g):
    qres = g.query("""
         
        SELECT ?Name ?Geo_Json ?Coord ?Adress ?Arrondissements ?Description ?Payant ?Horaires_Lundi ?Horaires_Mardi ?Horaires_Mercredi ?Horaires_Jeudi ?Horaires_Vendredi ?Horaires_Samedi  ?Horaires_Dimanche
        WHERE {
            ?s rdf:type :Fresh_place .
            ?s :Name ?Name .
            ?s :Geo_Json ?Geo_Json .
            ?s :Coord ?Coord .
            ?s :Adress ?Adress .
            ?s :Arrondissements ?Arrondissements .
            ?s :Description ?Description .
            ?s :Payant ?Payant .
            ?s :Horaires_Lundi ?Horaires_Lundi .
            ?s :Horaires_Mardi ?Horaires_Mardi .
            ?s :Horaires_Mercredi ?Horaires_Mercredi .
            ?s :Horaires_Jeudi ?Horaires_Jeudi .
            ?s :Horaires_Vendredi ?Horaires_Venredi .
            ?s :Horaires_Samedi ?Horaires_Samedi .
            ?s :Horaires_Dimanche ?Horaires_Dimanche .
            }""")
    return(qres)

def listeVelo(g):
    qres = g.query("""
         
        SELECT ?Name ?Geo_Json ?Coord  ?Arrondissements ?BiDirectional ?Sens_circulation
        WHERE {
            ?s rdf:type :bicycle_path .
            ?s :Name ?Name .
            ?s :Geo_Json ?Geo_Json .
            ?s :Coord ?Coord .
            ?s :Arrondissements ?Arrondissements .    
            ?s :BiDirectional ?BiDirectional .
            ?s :Sens_circulation ?Sens_circulation .
            }""")
    return(qres)

#to JSON
def arrayFontaine(qres):
    array =[]
    for results in qres:
        array.append({
            "Name": results[0],
            "Geo_Json": json.loads(results[1]),
            "Coord": [float(coord) for coord in results[2].split(",")],
            "Arrondissements":results[3],
            "Description":results[4],
            })
    return array

def arrayEvent(qres):
    array=[]
    for results in qres:
        array.append({
            "Name": results[0],
            "Geo_Json": json.loads(results[1]),
            "Coord": [float(coord) for coord in results[2].split(",")],
            "Adresse":results[3],
            "Arrondissements":results[4],
            "Description":results[5],
            "Payant":results[6],
            "Horaires_Lundi":results[7],
            "Horaires_Mardi":results[8],
            "Horaires_Mercredi":results[9],
            "Horaires_Jeudi":results[10],
            "Horaires_Vendredi":results[11],
            "Horaires_Samedi":results[12],
            "Horaires_Dimanche":results[13],
            }
            )
    return array

def arrayVelo(qres):
    array=[]
    for results in qres:
        array.append({
            "Name": results[0],
            "Geo_Json": json.loads(results[1]),
            "Coord": [float(coord) for coord in results[2].split(",")],
            "Arrondissements":results[3],
            "Bidirectionnel":results[4],
            "Sens de circulation":results[5],
            })
    return array

def arrayParcs(qres):
    array=[]
    for results in qres:
        array.append({
            "Name": results[0],
            "Geo_Json": json.loads(results[1]),
            "Coord": [float(coord) for coord in results[2].split(",")],
            "Adresse": results[3],
            "Arrondissements": results[4],
            "Description": results[5],
            "Portion d'arbres hauts": results[6],
            "Horaires_Lundi": results[7],
            "Horaires_Mardi": results[8],
            "Horaires_Mercredi": results[9],
            "Horaires_Jeudi": results[10],
            "Horaires_Vendredi": results[11],
            "Horaires_Samedi": results[12],
            "Horaires_Dimanche": results[13],
            })
    return(array)

def returnJson(type,g):
    if type=="fontaines":
        return json.dumps(arrayFontaine(listeFontaines(g)))
    elif type=="piste":
        return json.dumps(arrayVelo(listeVelo(g)))
    elif type=="activite":
        return json.dumps(arrayEvent(listeActiv(g)))
    elif type =="parc1":
        json.dumps(arrayParcs(listeParcs1(g)))
    elif type =="parc2":
        return json.dumps(arrayParcs(listeParcs2(g)))
    elif type =="parc3":
        return json.dumps(arrayParcs(listeParcs3(g)))

if __name__=="__main__":
    g=start()
    print(returnJson("parc1",g))