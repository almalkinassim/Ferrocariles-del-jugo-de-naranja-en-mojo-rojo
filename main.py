import classes
import graphics 
import tkinter as tkr
import random as rd

#interface graphique
root = tkr.Tk()
root.title("Ferrocariles del jugo de naranja en mojo rojo galactico")
canvas = tkr.Canvas(root, width=1240, height=786, bg= "#2F1939")
boite_reglages = graphics.Reglages(root)
canvas.pack()

# garde les sprites pour eviter qu'ils soient garbage collected et disparaissent de l'affichage
simulation_state = {"sprites": []}
simulation_state2 = {"nombrePlanetList": []}

#boucle pour chaque generation 
def start_simulation():
    canvas.delete("all") # reinitialise le canvas
    

    #+1 temporales para evitar errores de indice, pero hay que cambiarlo despues en las galaxia/itinerarios
    nbp = boite_reglages.get_nbp() 
    nbi = boite_reglages.get_nbi() 
    #nbg = boite_reglages.get_nbg() #remettre apres avoir fait la partie generations

    galaxie = classes.Galaxia() # iniciar la galaxia
    galaxie.SamsungGalaxy(nbp) # generar los planetas
    nombrePlanet=galaxie.nombreCoplt
    sprites = []
    nombrePlanetList=[]
    Label = tkr.Label(root)
    for planet in galaxie.listPlnt:
        sprites.append(graphics.PlanetSprite(canvas, planet, f"Assets/planete_{rd.randint(1,8)}.png"))
        print(planet)
        place= Label.place(x=planet.x, y=planet.y)
        # label nos permitira de poner texto
        nombrePlanetList.append(Label.config(text=nombrePlanet))
        print(nombrePlanetList)
    simulation_state["sprites"] = sprites
    simulation_state2["nombrePlanetList"] = nombrePlanetList
    

    ittest = classes.Itinerarios(galaxie) # test de itinerarios
    ittest.genererRd(nbi) # generer les itinéraires

    for i in range(nbi):
        graphics.GalaxyPath(canvas, ittest.itinerarios[i])
 # la lista de los fitness para luego hacer la competicion y comparar los fitness
    fitness_list = []
    for chemin in ittest.itinerarios:
        d = ittest.Dist(chemin)
        if d != 0:
            f = 1 / d
        else:
            f = float('inf')  # max au cas ou distance nulle (1 planete)
        fitness_list.append((f))



    #crea lista con tantos 0 como caminos en la lista fitness
    scores = [0]* len(fitness_list)


    for i in range(50):  
    # selecciona a 5 itinerarios
        indices = rd.sample(range(len(fitness_list)), 5)
    # escoge al mejor
        best = indices[0]
        for i in indices:
            if fitness_list[i][1] > fitness_list[best][1]:
                best = i
    # suma un punto al vencedor
        scores[best] += 1


    resultats = []

    for i in range(len(fitness_list)):
        chemin, fitness, distance = fitness_list[i]
        score = scores[i]
        resultats.append((chemin, fitness, distance, score))

# stockea los 4 mejores
    meilleurs = resultats[:4]

    print("MEILLEURS CHEMINS :")
    for chemin, fitness, distance, score in meilleurs:
        print("Score :", score)
        print("Distance :", distance)
        print("Fitness :", fitness)
        print("--------------")

boite_reglages.start_cmd(start_simulation)

root.mainloop()# hace correr el programa no se debe de poner nada despues de esta linea segun stack overflow porque si no el programa lo ignorara