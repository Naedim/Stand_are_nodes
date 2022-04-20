from pyvis.network import Network
import jsonreading

#Initialisation
Dicoviz = jsonreading.readJsonFileViz("data.json")
iso_net = Network(height='1500px', width='100%', bgcolor='#222222',font_color='white')

#Alimentation du réseau
##Création des nodes
for key,value in Dicoviz.items():
    iso_net.add_node(Dicoviz[key]["lien"],label=key)

##Creation des edges avec gestions des exceptions
for key,value in Dicoviz.items():
    url_src = Dicoviz[key]["lien"]
    url_dest = Dicoviz[key]["dependance"]
    for i in range(len(url_dest)):
        try:
            iso_net.add_edge(url_src,url_dest[i])
            print()
        except KeyError as e:
            iso_net.add_node(url_dest[i])
            iso_net.add_edge(url_src,url_dest[i])
            # print(e)
        except AssertionError as e:
            iso_net.add_node(url_dest[i])
            iso_net.add_edge(url_src,url_dest[i])
            # print(e)

#Utilisation d'algo
iso_net.barnes_hut()

#Affichage du réseau
iso_net.toggle_physics(True)
iso_net.show("iso_net.html")