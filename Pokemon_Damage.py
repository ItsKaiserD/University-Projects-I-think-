#Importacion de los Modulos necesarios para el Programa
import math
import random
from random import uniform
from moves import get_move
import pandas as pd

#Apertura de los archivos "pokemon_data" y "tabla_efectividad"
df = pd.read_csv("pokemon_data.csv", names=["Pokemon_Names", "Pokemon_Type", "Pokemon_Health", "Pokemon_Physic_Attack",
                                            "Pokemon_Physic_Defense", "Pokemon_Special_Attack", "Pokemon_Special_Defense",
                                            "Pokemon_Speed", "Pokemon_Moves", "Pokemon_Info"])
#El archivo pokemon_data se abre y se le asignan los nombres a las columnas de acuerdo a que representa cada nombre y  número.
type_table = pd.read_csv("tabla_efectividad.csv", names = ["Atacante", "Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting",
                                                   "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock","Ghost", "Dragon", "Dark",
                                                   "Steel", "Fairy", "Defensor"])
#Similar al caso anterior, se abre el archivo tabla_efectividad.csv y se le asignan nombres a cada una de las columnas, en este caso los tipos de los Pokémon.
#PD: No tengo ni la más minima idea de que embarrada me mande, pero si borro el nombre "Defensor" dela lectura de archivo, no puedo sacar la efectividad de tipos,
#aun cuando "Defensor" no cumple ninguna funcion en el programa.

# Función para obtener nuestro pokemon
def get_ally_pokemon(selected_pokemon):
    for i in range(df.shape[0]): 
        if selected_pokemon.lower() == str(df["Pokemon_Names"][i]):
           #Usamos un iterador simple "i" para la mayoria de funciones, en este caso, es para checar la columna "Pokemon Names" en cada una de sus posiciones
           #para poder determinar si el Pokemon ingresado por el usuario existe en el archivo

           return "Compañero Pokemon seleccionado: ", selected_pokemon.title()
           #Si el pokemon existe, la funcion retorna esta frase

    if selected_pokemon not in df["Pokemon_Names"]:


       return "ERROR"
# Función para obtener el tipo de nuestro pokemon
def get_ally_type(selected_pokemon):
    for i in range(df.shape[0]):        
        if selected_pokemon.lower() == str(df["Pokemon_Names"][i]):
            ally_type = str(df["Pokemon_Type"][i])
            #Varias de estas funciones tienen el mismo tipo de razonamiento, se chequea que el pokemon existe en cierta columna, y si existe,
            #en este caso se retorna el tipo del pokemon, obtenido de la columna "Pokemon Type" con el indice correspondiente al pokemon.

    return ally_type

# Funcón para obtener al pokemon a atacar
def get_enemy_pokemon(enemy_pokemon):
    for i in range(df.shape[0]):
        if enemy_pokemon.lower() == str(df["Pokemon_Names"][i]):
            #Se chequea la columna "Pokemon Names", si el nombre del enemigo existe...

            #Se retorna esta frase
            return "El pokemon seleccionado como adversario ha sido ", enemy_pokemon.title()

    if enemy_pokemon not in df["Pokemon_Names"]:


        return "ERROR"

# Función para obtener el tipo del pokemon enemigo 
def get_enemy_type(enemy_pokemon):
    for i in range(df.shape[0]):
        #Misma logica que la funcion para el aliado, pero con el pokemon enemigo
        if enemy_pokemon.lower() == str(df["Pokemon_Names"][i]):
            enemy_type = str(df["Pokemon_Type"][i])


    return enemy_type

# Función para obtener las estadisticas base del pokemon aliado
def get_ally_stats(selected_pokemon):
    base_stats = []
    #Se crea una lista vacia para poder almacenar posteriormente las estadisticas
    for i in range(df.shape[0]):
        if selected_pokemon.lower() == str(df["Pokemon_Names"][i]):
            #Se revisa que el pokemon exista en el archivo, y si existe, se obtiene el valor
            #de cada una de las columnas de las estadisticas pokemon (Velocidad, Ataque, Ataque Especial, etc.)
            #con el indice del pokemon escogido anteriormente: por ejemplo, si Bulbasaur según el archivo es el
            #indice 0, se obtienen todas la estadisticas con ese indice en mente.
            Base_Hp = int(df["Pokemon_Health"][i])
            Base_Attack = int(df["Pokemon_Physic_Attack"][i])           
            Base_Defense = int(df["Pokemon_Physic_Defense"][i])         
            Base_SP_Attack = int(df["Pokemon_Special_Attack"][i])
            Base_SP_Defense = int(df["Pokemon_Special_Defense"][i])
            Base_Speed = int(df["Pokemon_Speed"][i])
    base_stats.extend([Base_Hp, Base_Attack, Base_Defense, Base_SP_Attack, Base_SP_Defense, Base_Speed])
    #Cuando se hallan obtenido todas las estadistcas correspondientes, se utiliza el metodo extend para agregarlas a la lista vacia, y se retorna la lista con las estadisticas
    #base

    return base_stats

# Función para obtener las estadisticas base del enemigo
def get_enemy_stats(enemy_pokemon):
    enemy_base_stats = []
    for i in range(df.shape[0]):                                            
        if enemy_pokemon.lower() == str(df["Pokemon_Names"][i]):
            #Sigue la misma logica que la funcion anterior, solo que acá puede que haya hecho demás, ya que
            #el programa solo requiere la vida, defensa y defensa especial del enemigo para funcionar, pero
            #esta cosa ya esta hecha, asi que ya que
            Enemy_Base_Hp = int(df["Pokemon_Health"][i])                    
            Enemy_Base_Attack = int(df["Pokemon_Physic_Attack"][i]) 
            Enemy_Base_Defense = int(df["Pokemon_Physic_Defense"][i])
            Enemy_Base_SP_Attack = int(df["Pokemon_Special_Attack"][i])
            Enemy_Base_SP_Defense = int(df["Pokemon_Special_Defense"][i])
            Enemy_Base_Speed = int(df["Pokemon_Speed"][i])
            enemy_base_stats.extend([Enemy_Base_Hp, Enemy_Base_Attack, Enemy_Base_Defense, Enemy_Base_SP_Attack, Enemy_Base_SP_Defense, Enemy_Base_Speed])

    
    return enemy_base_stats
    #Retornamos la lista de estadisticas base del enemigo

# Función para obtener los movimientos que puede aprender nuestro pokemon aliado
def pokemon_moves(selected_pokemon):
    #Una vez el programa encontro nuestro pokemon seleccionado, utilizando el indice correspondiente
    #a dicho pokemon, consigue todos los elemento anexos a la columna "Pokemon Moves", transformada a un
    #str, y como en el archivo los movimientos estan separado por un ";", utilizamos el metodo .split para
    #obtener una lista con todos los movimientos.
    for i in range(df.shape[0]):
        if selected_pokemon.lower() == str(df["Pokemon_Names"][i]):   
            moves = str(df["Pokemon_Moves"][i])                       
            moves.split(";")                                          
                                                                      

    return moves
    #Y retornamos dicha lista.

# Funcion para obtener las estadisticas a nivel 50 de nuestro aliado 
def get_lvl50_stats(selected_pokemon, base_stats):
    #Creamos una lista vacia para almacenar las estadisticas luego de hacer los calculos correspondientes
    #y se definen las constantes importantes para los calculos de estadisticas, como los IV, EV, y el nivel del pokemon
    lvl_50_stats = [] 
    IV = 31           
    level = 50
    EV = 250
    for i in range(len(base_stats)):
        #Usamos un iterador para poder recorrer el rango del largo de la lista de las estadisticas base"""
        if i == 0:
            lvl_50_HP = (((((base_stats[i] + IV) * 2) + (math.sqrt(EV)/4)) * level)/100) + 10 + level
        #Cuando el iterador vale 0, esto corresponde al HP base del pokemon, de acuerdo al orden asignado al archivo, por lo que se ocupa la formula del HP a nivel 50
            lvl_50_stats.append(lvl_50_HP)
        #Se utiliza el metodo .append para poder insertar las estadisticas calculadas a la lista vacia
        else:
        #Cuando el iterador es diferente a 0, las estadisticas corresponden al resto (velocidad, defensas, etc.), por lo que se utiliza la formula correspondiente para el resto
        #de estadisticas al nivel 50
            lvl_50_otherstat = (((((base_stats[i] + IV) * 2) + (math.sqrt(EV)/4))* level)/100) + 5
            lvl_50_stats.append(lvl_50_otherstat)


    return lvl_50_stats
    #Cuando se haya calculado todo, se retorna la lista con las estadisticas a nivel 50

# Funcion para obtener las estadisticas a nivel 50 del enemigo
def get_lvl50_enemy_stats(enemy_pokemon, enemy_stats):
    #Similar a la funcion anterior, solo que en este caso solamente se calcularan la vida, defensa y defensa especial de enemigo
    #pues el resto de estadisticas no se necesitan para esta calculadora de daño
    enemy_lvl50_stats = []  
    IV = 31                 
    level = 50
    EV = 250
    enemy_lvl50_HP = (((((enemy_stats[0] + IV) * 2) + (math.sqrt(EV)/4)) * level)/100) + 10 + level
    enemy_lvl50_Def = (((((enemy_stats[2] + IV) * 2) + (math.sqrt(EV)/4))* level)/100 )+ 5
    enemy_lvl50_SPDef = (((((enemy_stats[4] + IV) * 2) + (math.sqrt(EV)/4))* level)/100) + 5
    enemy_lvl50_stats.extend([enemy_lvl50_HP, enemy_lvl50_Def, enemy_lvl50_SPDef])


    return enemy_lvl50_stats
    #Retornamos la lista de las estadisticas a nivel 50 de nuestro enemigo

# Funcion para obtener el STAB 
def stab(ally_type, move_type):
    #El STAB es basicamente un modificador de daño, si el tipo del pokemon alido y el tipo del ataque a realizar son el mismo, el valor de STAB es 1.2,
    #si los tipos no coinciden, el STAB vale 1. Luego de que se realize dicha comparacion, se retorna el valor de STAB
    if ally_type == move_type:
        STAB = 1.2
    else:
        STAB = 1


    return STAB

# Funcion para obtener la efectividad del ataque con respecto al tipo del enemigo
def efectivness(move_type, enemy_type):
    #Con el iterador i, recorremos el archivo type_table.csv, para encontrar en que columna esta el tipo del ataque que nuestro pokemon realizara, y si
    #lo encuentra, creara una tabla llamada "efectivity_table" con los multiplicadores de daño que posee el tipo del ataque con todos los tipos pokemon.
    for i in range(type_table.shape[0]):
        if move_type == str(type_table.iloc[i][0]):
            efectivity_table = type_table.iloc[i]
            #Luego,con un iterador deiferente en la efectivity_table, se busca en la columna "Atacante" si existe el tipo del pokemon defensor, y si existe, creara la variable
            #"efectiveness", con el valor de del segundo iterador como indice de la efectivity_table.
            for j in range(type_table.shape[0]):
                if enemy_type == str(type_table["Atacante"][j]):
                    efectiveness = efectivity_table.iloc[j]


    return efectiveness
    #Se retorna el valor de efectiveness

def get_damage(move_power, move_attack_category, lvl50_stats, enemy_lvl50_stats,
           efectiveness, STAB):
    #Con toda la informacion como la potencia del ataque, su categoria (si es fisico o espcial), las estadisticas, etc., definimos esta
    #funcion para determinar el daño que le causara nuestro pokemmon al enemigo
    import random
    from random import uniform
    #Importamos random para generar un valor aleatorio entre 0.85 y 1 para la formula de daño
    random = random.uniform(0.85, 1)
    modifier = float(efectiveness) * float(STAB) * random * 1.0
    level = 50
    if move_attack_category == "special":
        #Si el movimiento es de categoria "special", las estadisticas a ocupar son el ataque especial de nuestro aliado y la defensa especial del enemigo
        A = lvl50_stats[3]
        D = enemy_lvl50_stats[2]
        #Formula del daño
        damage = (((((2*level/5) + 2) * move_power * (A/D)) / 50) + 2) * modifier
        dealt_damage = float(damage)
    else:
        #Si el movimiento a realizar es de la categoria "physical" (puesto que es la unica otra que existe, se utiliza el atque fisico del aliado y la defensa
        #fisica del enemigo
        A = float(lvl50_stats[1])
        D = float(enemy_lvl50_stats[1])
        damage = (((((2*level/5) + 2) * move_power * (A/D)) / 50) + 2) * modifier
        dealt_damage = float(damage)

    return dealt_damage
    #Se retorna el valor del daño infligido

if __name__ == "__main__":
    #Entrada N° 1: Seleccion del Pokemon
    selected_pokemon = str(input("Ingrese su pokemon a elegir: "))
    print(get_ally_pokemon(selected_pokemon))
    #Salida N°1: Pokemon Seleccionado / Posibilidad de Error
    if get_ally_pokemon(selected_pokemon) == "ERROR":
        print("El pokemon que ingreso no existe en el archivo")
    else:
        #Salida N°2: Estadisticas
        base_stats = get_ally_stats(selected_pokemon)
        #Mostrando las Estadisticas Base
        print("Estadisticas Base de ", selected_pokemon.title(), "\n", "1.-Hp: ", base_stats[0], "\n", "2.- Ataque Fisico: ", base_stats[1], "\n", "3.- Defensa Fisica: ",
              base_stats[2], "\n", "4.- Ataque Especial: ", base_stats[3], "\n", "5.- Defensa Especial: ", base_stats[4], "\n", "6.- Velocidad: ", base_stats[5])
        #Obteniendo el Tipo y Movimientos de nuestro Aliado
        ally_type = get_ally_type(selected_pokemon)
        move_list = pokemon_moves(selected_pokemon)
        pokemon_moves = move_list.split(";")
        print("Movimientos Disponibles de", selected_pokemon.title())
        #Ciclo Para Mostrar los Movimientos de manera Ordenada
        for i in range(len(pokemon_moves)):
            print(i, ".-", pokemon_moves[i])
        index_attack = int(input("Ingrese el numero del ataque que quiera realizar: "))
        #Ciclo para comprobar si el index_attack ingresado es mayor o menor a la cantidad de ataques disponibles
        if index_attack > len(pokemon_moves):
            print("ERROR: El indice ingresado no es valido")
        else:
            #Informacion del Movimiento Seleccionado
            selected_attack = str(pokemon_moves[index_attack])
            move_info = get_move(selected_attack)
            move_power = int(move_info[1])
            move_type = str(move_info[2])
            move_attack_category = str(move_info[3])
            print("Ataque seleccionado: ", pokemon_moves[index_attack])
            print("Potencia del Ataque: ", move_info[1])
            lvl50_stats = get_lvl50_stats(selected_pokemon, base_stats)
            #Mostrando las estadisticas a nivel 50 de nuestro Pokemon aliado
            print("Estadisticas a Nivel 50 de ", selected_pokemon.title(), "\n", "1.-Hp: ", lvl50_stats[0], "\n", "2.- Ataque Fisico: ", lvl50_stats[1], "\n", "3.- Defensa Fisica: ",
                  lvl50_stats[2], "\n", "4.- Ataque Especial: ", lvl50_stats[3], "\n", "5.- Defensa Especial: ", lvl50_stats[4], "\n", "6.- Velocidad: ", lvl50_stats[5])
            #Obteniendo la informacion del Pokemon Adversario
            enemy_pokemon = str(input("Ingrese el pokemon al que atacara: "))
            print(get_enemy_pokemon(enemy_pokemon))
            #Comprobando que el Pokemon Adversario exista 
            if get_enemy_pokemon(enemy_pokemon) == "ERROR":
                print("El pokemon que ingreso no existe en el archivo")
            else:
                #Obteniendo las estadisticas del enemigo, tanto base como a nivel 50
                enemy_stats = get_enemy_stats(enemy_pokemon)
                enemy_lvl50_stats = get_lvl50_enemy_stats(enemy_pokemon, enemy_stats)
                print("Estadisticas a Nivel 50 de ", enemy_pokemon.title(), "\n", "1.-Hp: ", enemy_lvl50_stats[0], "\n", "2.- Defensa Fisica: ",
                      enemy_lvl50_stats[1], "\n", "3.- Defensa Especial: ", enemy_lvl50_stats[2])
                #Obteniendo la informacion importante para el calculo de daño; STAB y Efectividad
                STAB = stab(ally_type, move_type)
                enemy_type = get_enemy_type(enemy_pokemon)
                efectiveness = efectivness(move_type, enemy_type)
                #Calculo de Daño
                dealt_damage = get_damage(move_power, move_attack_category, lvl50_stats, enemy_lvl50_stats,
                                          efectiveness, STAB)
                #Salida de la vida restante y del daño causado 
                print("Daño realizado por ", selected_pokemon.title(),"a ", enemy_pokemon.title(), ": ", dealt_damage)
                remaining_hp = float(enemy_lvl50_stats[0]) - dealt_damage
                print(enemy_pokemon.title(), "quedó con ", remaining_hp, "HP restantes")
