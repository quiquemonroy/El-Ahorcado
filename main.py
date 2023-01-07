import random, os, time
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
END = "\033[0m"
HANGMANPICS = [
  '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]
para_rand = ['ablandar', 'aborigen', 'abreviar', 'acarrear', 'acogedor', 'adjetivo', 'adjuntar', 'afrontar', 'agrícola', 'alcayata', 'almohada', 'aminorar', 'aparecer', 'apreciar', 'arbitrar', 'atenazar', 'atrevido', 'aventura', 'avestruz', 'bailarín', 'baluarte', 'baratija', 'barbacoa', 'bebedizo', 'bendecir', 'blancura', 'bofetada', 'bombilla', 'bordillo', 'braguero', 'cabestro', 'cafetera', 'calcular', 'califato', 'callejón', 'calzador', 'camarero', 'capturar', 'carruaje', 'carrusel', 'cartilla', 'cartucho', 'castillo', 'catarata', 'celebrar', 'cellisca', 'cerilla', 'chistera', 'circuito', 'circular', 'codorniz', 'cofradía', 'colgante', 'colonial', 'comparar', 'comparsa', 'concebir', 'conceder', 'concepto', 'consulta', 'contrato', 'converso', 'convicto', 'convulso', 'correcto', 'corredor', 'creación', 'creativo', 'creencia', 'culminar', 'cultural', 'dactilar', 'decisión', 'degradar', 'degustar', 'delgadez', 'deprimir', 'desacato', 'desatino', 'descoser', 'descuido', 'desguace', 'deshacer', 'destacar', 'destapar', 'destello', 'devuelto', 'dictamen', 'diminuto', 'diputado', 'disolver', 'dolorido', 'dualidad', 'duradero', 'efectuar', 'elevador', 'embeleso', 'empalmar', 'emplazar', 'encantar', 'encestar', 'endémico', 'enfático', 'ensalada', 'entender', 'envuelto', 'erupción', 'escalope', 'escombro', 'espinoso', 'espumoso', 'esquimal', 'estatura', 'estofado', 'estudiar', 'eventual', 'evocador', 'exaltado', 'explorar', 'expulsar', 'extracto', 'fabricar', 'fabuloso', 'fanático', 'fandango', 'favorito', 'fechoría', 'fecundar', 'femenino', 'festejar', 'flaqueza', 'florista', 'folletín', 'fonética', 'forajido', 'frondoso', 'gabinete', 'galápago', 'garbanzo', 'generoso', 'genética', 'grabador', 'graduado', 'guisante', 'guitarra', 'habanero', 'hechizar', 'herético', 'holgazán', 'homónimo', 'hospital', 'humildad', 'ilustrar', 'imaginar', 'imprenta', 'impulsar', 'incienso', 'incierto', 'inculpar', 'indultar', 'inocente', 'insignia', 'insuflar', 'insumiso', 'intentar', 'invasión', 'isotermo', 'jabalina', 'jacobino', 'jilguero', 'justicia', 'juventud', 'labranza', 'ladrillo', 'langosta', 'lanzador', 'lastimar', 'licencia', 'liquidez', 'luchador', 'magnolia', 'maletero', 'mamífero', 'maniobra', 'medieval', 'mercader', 'merendar', 'misterio', 'molestar', 'molinero', 'moraleja', 'nebulosa', 'nervioso', 'obelisco', 'octaedro', 'olfatear', 'ondulado', 'opositor', 'original', 'orquídea', 'pabellón', 'palomita', 'paraguas', 'pasajero', 'pastoril', 'percutor', 'perdurar', 'perezoso', 'perfecto', 'pergeñar', 'pistacho', 'pleitear', 'poltrona', 'populoso', 'portería', 'precepto', 'préstamo', 'probable', 'probador', 'producto', 'profesor', 'provocar', 'puñetazo', 'purgante', 'raspador', 'reactivo', 'reavivar', 'recortar', 'reiterar', 'renegado', 'reproche', 'repuesto', 'reservar', 'revolcar', 'rupestre', 'sacudida', 'seductor', 'segmento', 'sencillo', 'sensible', 'servicio', 'simetría', 'sobornar', 'sorpresa', 'subsuelo', 'suciedad', 'sufragio', 'sustento', 'taburete', 'tangente', 'terminar', 'tornillo', 'torrente', 'traducir', 'travesía', 'vainilla', 'variedad', 'ventisca', 'vocativo', 'vorágine', 'acuciante', 'agridulce', 'aguerrido', 'alabastro', 'alambique', 'alcaparra', 'altercado', 'aspillera', 'automóvil', 'autoridad', 'bandidaje', 'belladona', 'bendición', 'bergantín', 'bocadillo', 'cabalgata', 'cajetilla', 'caldereta', 'caligrama', 'callejero', 'carbonero', 'centurión', 'chasquear', 'cobertura', 'codificar', 'comadreja', 'comandante', 'compresor', 'confitura', 'contrario', 'debilitar', 'decadente', 'derrotero', 'desajuste', 'desplante', 'diciembre', 'dictadura', 'dispuesto', 'domicilio', 'economato', 'educativo', 'ejercicio', 'eléctrico', 'engranaje', 'espárrago', 'esquiador', 'estupendo', 'extractor', 'ferrovial', 'flautista', 'forastero', 'fotocopia', 'fotógrafo', 'fragmento', 'gabardina', 'ganadería', 'gladiador', 'grafitero', 'guerrilla', 'hacendado', 'hidrógeno', 'hipódromo', 'hipogrifo', 'hortelano', 'humanista', 'idealista', 'impostura', 'impresora', 'increíble', 'indefenso', 'indirecta', 'inquilino', 'intelecto', 'intervalo', 'jardinero', 'juguetero', 'juramento', 'kamasutra', 'kilovatio', 'labandera', 'lactancia', 'liderazgo', 'limpiador', 'magistral', 'malaquita', 'maleficio', 'mandarina', 'mantecado', 'maravilla', 'masajista', 'melodrama', 'menguante', 'mercancía', 'merendero', 'militante', 'miserable', 'modalidad', 'monarquía', 'municipal', 'narrativa', 'naufragio', 'necesidad', 'netiqueta', 'notificar', 'nutritivo', 'obediente', 'obstáculo', 'obstinado', 'ocultismo', 'oleoducto', 'optimizar', 'ordenanza', 'organismo', 'paciencia', 'palabrota', 'palaciego', 'palosanto', 'panadería', 'pandereta', 'paparazzi', 'parihuela', 'paritario', 'parroquia', 'partitura', 'patología', 'peliaguda', 'pergamino', 'periferia', 'pescadero', 'petirrojo', 'petrolero', 'pistolero', 'plusmarca', 'polvareda', 'populacho', 'postventa', 'prematuro', 'productor', 'profesión', 'promiscuo', 'propileno', 'proyectil', 'quebranto', 'rabadilla', 'ralladura', 'ramillete', 'rastafari', 'reasignar', 'rebobinar', 'recepción', 'recorrido', 'redefinir', 'reestreno', 'refugiado', 'registrar', 'rematador', 'repostero', 'requisito', 'resguardo', 'respuesta', 'resquicio', 'restaurar', 'restregar', 'revulsivo', 'rodillera', 'rotuliano', 'rutinario', 'sacerdote', 'sacrificio', 'sacristía', 'sagitario', 'salchicha', 'sarcófago', 'sarmiento', 'seguridad', 'semejante', 'seminario', 'servicial', 'significa', 'siguiente', 'simulacro', 'sintético', 'sobrepeso', 'sociólogo', 'sombrilla', 'tabernero', 'tabulador', 'televisor', 'temporada', 'trampolín', 'transcurso', 'tranquilo', 'traspasar', 'triángulo', 'trimestre', 'trinchera', 'trinquete', 'turístico', 'utensilio', 'vectorial', 'vencedora', 'veraniego', 'vestuario', 'vinagreta', 'voracidad', 'zanahoria', 'zapatilla', 'abanderado', 'abecedario', 'abolladura', 'abominable', 'absorbente', 'abstenerse', 'abundancia', 'acantilado', 'accionista', 'acelerante', 'acribillar', 'adoquinado', 'afirmativo', 'aglomerado', 'agorafobia', 'aguafuerte', 'alienígena', 'alquimista', 'anatomista', 'animosidad', 'apariencia', 'arqueólogo', 'aspiradora', 'astronomía', 'autocracia', 'aventurero', 'baloncesto', 'benefactor', 'bestseller', 'bombardero', 'caballería', 'calculador', 'campanario', 'cangrejera', 'carburador', 'casualidad', 'celebridad', 'certificar', 'cibernauta', 'cilíndrico', 'ciudadanía', 'coagulante', 'combustión', 'comprender', 'contemplar', 'continente', 'contrabajo', 'contrapeso', 'contrariar', 'contrastar', 'convención', 'cordillera', 'cuatrienio', 'daltonismo', 'decadencia', 'decorativo', 'defectuoso', 'definitivo', 'desacierto', 'desaliento', 'desarrollo', 'descontrol', 'despectivo', 'despreciar', 'destructor', 'devastador', 'diferencia', 'diligencia', 'directorio', 'disentería', 'divergente', 'documental', 'dominguero', 'draconiano', 'eficiencia', 'emigración', 'emotividad', 'encasillar', 'energético', 'entorpecer', 'entrenador', 'entrevista', 'equilibrar', 'escalinata', 'escrutinio', 'esperpento', 'estanquero', 'estornudar', 'explotador', 'fantástico', 'fascinante', 'federación', 'feldespato', 'festividad', 'feudalismo', 'financiero', 'formidable', 'futbolista', 'gobernador', 'habichuela', 'hazmerreír', 'hemorragia', 'hidratante', 'hipertexto', 'hormiguero', 'impaciente', 'inconcluso', 'individual', 'iniciativa', 'injusticia', 'inmediatez', 'inofensivo', 'insurgente', 'interrogar', 'invencible', 'inventario', 'itinerante', 'itinerario', 'justiciero', 'justificar', 'legionario', 'lentejuela', 'litografía', 'lucernario', 'madreperla', 'madriguera', 'manzanilla', 'matemático', 'matriarcal', 'medallista', 'melancolía', 'metalurgia', 'militancia', 'monasterio', 'multicolor', 'napolitana', 'narcisista', 'negociador', 'nigromante', 'nobiliario', 'paquidermo', 'petroglifo', 'precipicio', 'preparador', 'pseudónimo', 'publicidad', 'purgatorio', 'quijotesco', 'raciocinio', 'realizador', 'recolector', 'relevancia', 'remolcador', 'repiqueteo', 'resolutivo', 'retrovisor', 'ropavejero', 'sacerdocio', 'secretario', 'septiembre', 'sinceridad', 'sobrecoste', 'sobresalir', 'subjuntivo', 'terciopelo', 'torrefacto', 'transporte', 'trementina', 'vocacional', 'voluntario']
palabra = random.choice(para_rand)
palabra_st = palabra

aciertos = 0
intentos = 0
fallos = 0
lista_palabra = []
lista_rallitas = []
usadas = []
lista_palabra_sintilde = []
def randomColor(frase):
  BLACK = "\033[0;30m"
  RED = "\033[0;31m"
  GREEN = "\033[0;32m"
  BROWN = "\033[0;33m"
  BLUE = "\033[0;34m"
  PURPLE = "\033[0;35m"
  CYAN = "\033[0;36m"
  LIGHT_GRAY = "\033[0;37m"
  DARK_GRAY = "\033[1;30m"
  LIGHT_RED = "\033[1;31m"
  LIGHT_GREEN = "\033[1;32m"
  YELLOW = "\033[1;33m"
  LIGHT_BLUE = "\033[1;34m"
  LIGHT_PURPLE = "\033[1;35m"
  LIGHT_CYAN = "\033[1;36m"
  LIGHT_WHITE = "\033[1;37m"
  END = "\033[0m"
  colores = [RED, BLUE, BLACK, RED, GREEN, BROWN, BLUE, PURPLE, CYAN, LIGHT_GRAY, DARK_GRAY, LIGHT_RED, LIGHT_GREEN, YELLOW, LIGHT_BLUE, LIGHT_PURPLE, LIGHT_CYAN, LIGHT_WHITE,END]
  rand = random.choice(colores)
  for letra in frase:
    print(random.choice(colores), end= "")
    print(letra, end="")
  print(END)
def tildes(word):
  for letra in word:
    if letra == "á":
      letra = letra.replace(letra,"a")
      lista_palabra_sintilde.append(letra)
    elif letra == "é":
      letra = letra.replace(letra,"e")
      lista_palabra_sintilde.append(letra)
    elif letra == "í":
      letra = letra.replace(letra,"i")
      lista_palabra_sintilde.append(letra)
    elif letra == "ó":
      letra = letra.replace(letra,"o")
      lista_palabra_sintilde.append(letra)
    elif letra == "ú" or letra == "ü":
      letra = letra.replace(letra,"u")
      lista_palabra_sintilde.append(letra)
    else:
      lista_palabra_sintilde.append(letra)
def tiempo(segundos):
  time.sleep(segundos)
def limpiar():
  os.system("clear")
def rallitas(word):
  for letra in word:
    lista_rallitas.append("__")
    

def palabras(word):
  for letra in word:
    lista_palabra.append(letra)
def lista_print(lista_):
  for i in lista_:
    print(i.capitalize(), end = " ")
  print("\n")




rallitas(palabra)#mete las rallitas en la lista(antes del bucle)
palabras(palabra)#mete la palabra en la lista(antes del bucle)
tildes(palabra)
def empezar():
  palabra = random.choice(para_rand)
  aciertos = 0
  intentos = 0
  fallos = 0
  lista_palabra = []
  lista_rallitas = []
  usadas = []
  usadas.clear()
  rallitas(palabra)
  palabras(palabra)
  return palabra, aciertos,intentos,fallos,lista_palabra,lista_rallitas,usadas,rallitas(palabra),palabras(palabra)
while True:
  print()
  titulo = "         --Juego del ahorcado--".upper()
  randomColor(titulo)
  print()
  print(f"La palabra que buscas tiene {RED}{len(palabra)}{END} letras.")
  print(GREEN)
  print(HANGMANPICS[fallos])
  print(LIGHT_CYAN, end="")
  lista_print(lista_rallitas)
  print(RED,end="")
  lista_print(usadas)
  print(END, end ="")
  print(f"Llevas {GREEN}{intentos}{END} intentos.")
  print()
  if aciertos >= len(palabra):
    time.sleep(0.3)
    print()
    print(f"{GREEN}¡GANASTE! HAS SALVADO EL CUELLO!{END}")
    print()
    time.sleep(2)
    otra = input(f"{YELLOW}Quieres jugar otra vez? {RED}(s/n)\n >{GREEN} ")
    print(END)
    if otra == "s":
      para_rand.remove(palabra)
      lista_palabra_sintilde.clear()
      lista_palabra.clear()
      lista_rallitas.clear()
      usadas.clear()
      aciertos = 0
      intentos = 0
      fallos = 0
      palabra = random.choice(para_rand)
      rallitas(palabra)
      palabras(palabra)
      tildes(palabra)
      #print(lista_palabra)
      #print(lista_rallitas)
      #empezar()
      tiempo(1)
      limpiar()
      continue
    elif otra == "n":
      os.system("clear")
      print()
      print("Ok, espero que lo hayas pasado bien.")
      time.sleep(2)
      print()
      print("Hecho por ",end="")
      randomColor("quique.")
      time.sleep(2)
      os.system("clear")
      exit()
  if fallos == 6:
    print(f"{RED}¡HAS MUERTO!{END}")
    print()
    print(f"La palabra que buscabas era {RED}{palabra.upper()}{END}")
    print()
    otra = input(f"{YELLOW}Quieres jugar otra vez? {RED}(s/n)\n >{GREEN} ")
    print(END)
    if otra == "s" or otra == "":
      para_rand.remove(palabra)
      lista_palabra_sintilde.clear()
      lista_palabra.clear()
      lista_rallitas.clear()
      usadas.clear()
      aciertos = 0
      intentos = 0
      fallos = 0
      palabra = random.choice(para_rand)
      rallitas(palabra)
      palabras(palabra)
      tildes(palabra)
      #print(lista_palabra)
      #print(lista_rallitas)
      #empezar()
      tiempo(1)
      limpiar()
      continue
    elif otra == "n":
      os.system("clear")
      print()
      print("Ok, espero que lo hayas pasado bien.")
      time.sleep(2)
      print()
      print("Hecho por ",end="")
      randomColor("quique.")
      time.sleep(2)
      os.system("clear")
      exit()
  guess = input(f"ELIGE UNA LETRA Y PULSA ENTER:\n\n{LIGHT_CYAN} > ").strip().upper()
  print(END)
  if guess.lower() == palabra_st.lower():
    for i in range(0,len(palabra)):
      lista_rallitas[i] = palabra[i].upper()
    print(f"{LIGHT_CYAN}YEAH!!{END}")
    aciertos += len(palabra)
    tiempo(1)
    limpiar()
    continue#esto es por si acierta la palabra entera.
  if guess not in usadas:
    usadas.append(guess)
    bien = 0
    intentos +=1
    for i in range(0,len(palabra)):
      if guess.lower() == lista_palabra_sintilde[i].lower():
        bien +=1
        aciertos += 1
        lista_rallitas[i] = lista_palabra[i].capitalize()
      else:
        continue
    if bien > 0:
      print(f"La letra {guess.capitalize()} está {GREEN}{bien} {END}veces")
      print()
      time.sleep(1)
      os.system("clear")
      continue
    else:
      print(f"{RED}-----Nope-----{END}")
      fallos +=1
      time.sleep(1)
      os.system("clear")
  else:
    print("No repitas letras!".upper())
    time.sleep(1)
    os.system("clear")
    continue