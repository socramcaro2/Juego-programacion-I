import tkinter as tk
from tkinter import filedialog
import time, sys, random, os


game_state = {
    "health": 100,
    "current_score": 0,
    "round": 1,
    "money": 7,
    "dice_type1": "normal",
    "dice_type2": "normal",
    "dice_type3": "None",
    "dice_type4": "None",
    "bonuspoints" : [50, 100, 250,0,0], # añado varios 0 extra en caso de que se necesite acceder a algo de la lista y no exista nada, asi no dara Index error
    "money_rounds" : [4, 5, 6, 7,0,0],
    "bandits" : ["Dusty Johnson", "Calamity Joe", "Billy el Tuerto", "Whiskey Kid", "Jessie la Rápida",
                    "Black Bart", "Annie Oakley Jr.", "Rattlesnake Rick", "Texas Jack", "Soapy Sam",
                    "Wild Bill Hickok II", "Belle la Salvaje", "Kid Colorado", "Montana Slim",
                    "Ruby la Peligrosa", "Deadeye Dan", "Sweetwater Sue", "Pancho el Zurdo",
                    "Ginger el Gatillo", "Doc Holliday Jr.", "Silver Sam", "Rose de la Frontera",
                    "Wyatt Earp III", "Cody el Coyote", "Pearl la Pistolera", "Nevada Nick",
                    "Sierra Sue", "Blaze Brody", "Dakota Dave", "Scarlett la Tiradora"]
}

d6_sprites = {
    0 : '''
+-------+
|       |
|       |
|       |
+-------+''',
    1: '''
+-------+
|       |
|   ·   |
|       |
+-------+''',
    2: '''
+-------+
| ·     |
|       |
|     · |
+-------+''',
    3: '''
+-------+
| ·     |
|   ·   |
|     · |
+-------+''',
    4: '''
+-------+
| ·   · |
|       |
| ·   · |
+-------+''',
    5: '''
+-------+
| ·   · |
|   ·   |
| ·   · |
+-------+''',
    6: '''
+-------+
| ·   · |
| ·   · |
| ·   · |
+-------+''',
    7: """
+-------+
| ·   · |
| · · · |
| ·   · |
+-------+""",
    8: """
+-------+
| · · · |
| ·   · |
| · · · |
+-------+""",
    9: """
+-------+
| · · · |
| · · · |
| · · · |
+-------+""",
    10: '''
+-------+
|       |
|  10   |
|       |
+-------+''',
    11: '''
+-------+
|       |
|  11   |
|       |
+-------+''',
    12: '''
+-------+
|       |
|  12   |
|       |
+-------+''',
    13: '''
+-------+
|       |
|  13   |
|       |
+-------+''',
    14: '''
+-------+
|       |
|  14   |
|       |
+-------+''',
    15: '''
+-------+
|       |
|  15   |
|       |
+-------+''',
    16: '''
+-------+
|       |
|  16   |
|       |
+-------+''',
    17: '''
+-------+
|       |
|  17   |
|       |
+-------+''',
    18: '''
+-------+
|       |
|  18   |
|       |
+-------+'''
}

def seleccionar_archivo(): # para un jefe
    # Abre el explorador de archivos y guarda la ruta del archivo seleccionado en una variable.
    file_path = filedialog.askopenfilename(title="selecciona un archivo")
    if file_path:
        print(f"Archivo seleccionado: {file_path}")
        return file_path
    else:
        print("No se seleccionó ningún archivo.")
        return None


def Score(GameState):   
    if GameState['health'] > 0:
        GameState.update({"current_score" : GameState["round"]*100})
        if GameState["round"] % 2 != 0 or GameState["round"] == 1:
            if GameState['health'] > 99:
                GameState.update({"current_score" : GameState["current_score"] + (GameState["round"]*50)})
            del GameState["bonuspoints"][0]
    return GameState
        

        
def throw_dice(dice_modifier):
    dice_value = random.randint(1, 6)
    
    if dice_modifier == "metal":
        dice_value *= 2
    if dice_modifier == "lucky":
        luck_mod = random.randint(0,100)
        if luck_mod < 11:
            dice_value *= 3
            print("Lucky has trigered! x3 dice value :3")
        elif 10 < luck_mod < 40:
            dice_value += 5
            print("Lucky has trigered! +5 dice value")
        elif luck_mod > 94:
            dice_value *= 0
            print("Lucky has trigered... x0 dice value :c")
    if dice_modifier == "None":
        dice_value *= 0
            
    return dice_value

def DynText(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush() #para forzar a que se escriban los caracteres del bufer(segun documentacion)
        time.sleep(0.01)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
def shop(GameState):
    DynText('''Bienvenido a la tienda, aqui es donde podras comprar los dados o mejorarlos
            
Estos son los articulos disponibles para comprar:

(1)4$ dado nuevo normal
(2)6$ dado de metal
(3)6$ dado de la suerte
(other input)salir

elige una opcion...
            \n''')
    k=0
    while k==0:
        buy = input()
        if buy == "1":
            if GameState['money'] < 4:
                DynText('No tienes saldo suficiente...')
                continue
            if GameState['money'] > 3:
                change_dice = input(f'Que dado deseas cambiar:\n\n1: {GameState['dice_type1']}, 2: {GameState['dice_type2']}, 3: {GameState['dice_type3']}, 4: {GameState['dice_type4']}\n\n')  
                if change_dice in ("1", "2", "3", "4"):
                    GameState.update({f'dicetype{int(change_dice)}': 'normal'})
                    DynText(f'dado {change_dice} ha pasado a ser normal')
                else:
                    DynText(f'{change_dice} No es un input valido, vuelve a intentarlo')
                    continue
                    
        elif buy == "2":
            if GameState['money'] < 6:
                DynText('No tienes saldo suficiente...')
                continue
            if GameState['money'] > 5:
                change_dice = input(f'Que dado deseas cambiar:\n\n1: {GameState['dice_type1']}, 2: {GameState['dice_type2']}, 3: {GameState['dice_type3']}, 4: {GameState['dice_type4']}\n\n')  
                if change_dice in ("1", "2", "3", "4"):
                    GameState.update({f'dicetype{int(change_dice)}': 'metal'})
                    DynText(f'dado {change_dice} ha pasado a ser de metal')
                else:
                    DynText(f'{change_dice} No es un input valido, vuelve a intentarlo')
                    continue
        elif buy == "3":
            if GameState['money'] < 6:
                DynText('No tienes saldo suficiente...')
                continue
            if GameState['money'] > 5:
                change_dice = input(f'Que dado deseas cambiar:\n\n1: {GameState['dice_type1']}, 2: {GameState['dice_type2']}, 3: {GameState['dice_type3']}, 4: {GameState['dice_type4']}\n\n')  
                if change_dice in ("1", "2", "3", "4"):
                    GameState.update({f'dicetype{int(change_dice)}': 'lucky'})
                    DynText(f'dado {change_dice} ha pasado a ser de la suerte')
                else:
                    DynText(f'{change_dice} No es un input valido, vuelve a intentarlo')
                    continue          
        elif buy == "0":
            k=1
        else:
            DynText(f'{buy} no es un input valido')
    return GameState
            


def dados_en_linea(sprites_dado1, sprites_dado2, sprites_dado3, sprites_dado4): # el codigo para imprimir los dados en linea es de chatgpt, en su defecto utilizaria   DynText(f'{d6_sprites[dado1]} {d6_sprites[dado2]} {d6_sprites[dado3]} {d6_sprites[dado4]}') y se imprimirian en vertical
    sprites = [sprites_dado1, sprites_dado2, sprites_dado3, sprites_dado4]
    lineas_sprites = [sprite.strip().split('\n') for sprite in sprites]
    num_lineas = len(lineas_sprites[0]) if lineas_sprites else 0
    num_dados = len(lineas_sprites)
    for i in range(num_lineas):
        linea_output = ""
        for j in range(num_dados):
            if i < len(lineas_sprites[j]):
                linea_output += lineas_sprites[j][i]
            else:
                # Esto es por si acaso algún sprite tiene menos líneas (no debería ser el caso aquí)
                linea_output += " " * len(lineas_sprites[j][0]) if lineas_sprites[j] else ""
            if j < num_dados - 1:
                linea_output += "  "  # Añade dos espacios entre los dados
        print(linea_output)
    
WantToPlay = True
while WantToPlay == True:
    #Menu para empezar a jugar    
    ii = 0
    while ii == 0:
        Selection = input(
        """
      ____       ____        _ _      _   
     / ___| ___ | __ ) _   _| | | ___| |_ 
    | |  _ / _ \|  _ \| | | | | |/ _ \ __|
    | |_| | (_) | |_) | |_| | | |  __/ |_ 
     \____|\___/|____/ \__,_|_|_|\___|\__|


    1. Jugar
    2. Como jugar
    3. Salir\n
    """)
        clear_screen()
        if Selection == "2":
            DynText("""NORMATIVA DEL JUEGO: ¡A DERROTAR A LOS BANDIDOS!

    Objetivo: Derrotar a los 5 bandidos en combates individuales.

    Combate: En cada ronda contra un bandido, ambos (tú y el bandido) lanzaréis 2 dados virtuales.
    Ganador de la ronda: Quien obtenga la suma más alta de sus dos dados, gana la ronda.

    Enfrentamiento: Deberás ganar más rondas que el bandido para derrotarlo.

    Habilidades: Tanto tú como los bandidos podéis tener habilidades especiales que influyan en el combate. ¡Estate atento!

    Tienda: Entre combates, podrás visitar la tienda para comprar objetos y mejoras.

    Mejora de Suerte: Al comprar la mejora de suerte, tendrás las siguientes probabilidades al lanzar un solo dado:
    5% de que el dado no puntúe (valor = 0).
    30% de sumar 5 al valor del dado.
    10% de multiplicar el valor del dado por 3.

    Dado de Metal: Si utilizas un Dado de Metal, el resultado de uno de tus dados se multiplicará por 2.

        """)
        elif Selection == "3":
            print("Bye!")
            sys.exit(1)
        elif Selection == "1":
            ii=1
        else:
            print("No es un valor valido\n")

    DynText("""
      ____       ____        _ _      _   
     / ___| ___ | __ ) _   _| | | ___| |_ 
    | |  _ / _ \|  _ \| | | | | |/ _ \ __|
    | |_| | (_) | |_) | |_| | | |  __/ |_ 
     \____|\___/|____/ \__,_|_|_|\___|\__|

    Bienvenido a GoBullet, espero que tengas un buen rato y disfrutes
    """)
    first_boss = True
    while game_state['health']>0 and game_state['round'] != 5:
        if first_boss == False:
            game_state.update({'money': game_state['money'] + game_state["money_rounds"][0]})
            DynText(f'Has recibido {game_state["money_rounds"][0]}$')
            del game_state['money_rounds'][0]
            game_state.update({'health': 100})
            DynText('Curado con exito!')
        bandit_selector = random.randint(0, int(len(game_state["bandits"])) - 1 )
        DynText(f"Tu {game_state["round"]}º enemigo será {game_state["bandits"][bandit_selector]}, preparate para el combate!\n\n")
        del game_state["bandits"][bandit_selector]
        input("(enter para continuar)")

        clear_screen()


        victory_condition = 0
        message = 0
        while victory_condition != 2 and game_state['health'] > 0:
        
            dado1=throw_dice(game_state["dice_type1"])
            dado2=throw_dice(game_state["dice_type2"])
            dado3=0 if game_state["dice_type3"] == "None" else throw_dice(game_state["dice_type3"])
            dado4=0 if game_state["dice_type4"] == "None" else throw_dice(game_state["dice_type4"])

            if game_state["round"] == 1 or game_state["round"] == 2:
                if message == 0:
                    DynText("Este forajido tiene 2 dados, los cuales tienen valores entre 1 y 6, suerte!")
                DadoForajido1, DadoForajido2, DadoForajido3, DadoForajido4 =random.randint(1,6), random.randint(1,6), 0,0

            if game_state["round"] == 3:
                if message == 0:
                    DynText("Este forajido tiene 3 dados, la cosa se complica, tiene 2 dados de 6 caras y aparte un dado de 3 caras, Suerte!")
                DadoForajido1, DadoForajido2, DadoForajido3, DadoForajido4 =random.randint(1,6), random.randint(1, 6), random.randint(1,3),0

            if game_state["round"] == 4:
                if message == 0:
                    DynText("Este forajido cuenta con 3 dados, cada uno de 9 caras, si no tienes mas dados o power ups di adiosa la partida, mucha suerte!")
                DadoForajido1, DadoForajido2, DadoForajido3,  DadoForajido4 =random.randint(1,9), random.randint(1, 9), random.randint(1, 9),0

            if game_state["round"] == 5:
                if message == 0:
                    DynText("FINALMENTE, nos enfrentamos al jefe final, este jefe es especialmente complicado, si lo necesitas elegiras un archivo de tu pc, si pierdes este sera eliminado, asi que mucho cuidado, como recompensa si escoges un archivo un dado enemigo sera eliminado\n\n\n ")
                time.sleep(1)
                nombre_archivo = seleccionar_archivo()
                DadoForajido1, DadoForajido2, DadoForajido3, DadoForajido4 =random.randint(1,9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)
                if nombre_archivo != None:
                   DadoForajido1 = 0
                   

            message = 1 #para que no salga mas veces el mensaje de inicio de cada bandido
            tus_puntos = dado1+dado2+dado3+dado4
            puntos_enemigos = DadoForajido1+DadoForajido2+DadoForajido3+DadoForajido4

            DynText("Tus dados...\n")
            dados_en_linea(d6_sprites[dado1], d6_sprites[dado2], d6_sprites[dado3], d6_sprites[dado4])
            DynText(f"Total de puntos: {tus_puntos}\n\n")
            time.sleep(1)

            DynText("Sus dados... \n")
            dados_en_linea(d6_sprites[DadoForajido1], d6_sprites[DadoForajido2], d6_sprites[DadoForajido3], d6_sprites[DadoForajido4])
            DynText(f"Total de puntos: {puntos_enemigos}\n")
            time.sleep(1)

            if tus_puntos > puntos_enemigos:
                DynText("Tu ganas! :3\n")
                victory_condition += 1
            elif tus_puntos == puntos_enemigos:
                DynText("vaya... que raro... un empate... ninguno gana... :/\n")
            else:
                DynText("mecachis, has perdido, la proxima sera... :c\n")
                game_state.update({"health": game_state['health'] - 50})
            if game_state['health'] < 1 and game_state['round'] == 5:
                try:
                    os.remove(nombre_archivo)
                    print(f"El archivo '{nombre_archivo}' ha sido eliminado.")
                except FileNotFoundError:
                    print(f"El archivo '{nombre_archivo}' no existe.")
                except Exception as e:
                    print(f"Ocurrió un error al intentar eliminar el archivo: {e}")
            input("press enter to continue to next roll...")

        first_boss = False
        game_state = Score(game_state)
        DynText(f"Tus puntos actuales son {game_state['current_score']} ")
        game_state.update({'round': game_state['round']+1})
        game_state = shop(game_state)

    if game_state['round'] == 6: #porque se suma despues de la ronda 5 al ganar, por lo que ronda 6 es lo correcto
        DynText('You Win!')
    else:
        DynText('You loose... :c')
    
    DynText('La partida ha acabado, quieres seguir jugando? (y/n) ')
    StillPlay = input()
    
    
    if StillPlay.lower() in ("y", "yes"):
        pass
    elif StillPlay.lower() in ('n', 'no'): 
        DynText('Bye!')
        WantToPlay = False
    else:
        DynText('No es un input valido, siguiendo con el juego, en caso de querer salir -> ctrl + c')
        pass
    