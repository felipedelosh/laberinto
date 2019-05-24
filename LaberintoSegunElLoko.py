"""
@Felipedelosh

a los 3 dias de julio de 2018


Se ingresa un laberinto

1: es el muro
0: es camino
A: es el origen
B: es el destino


1 - se tiene que cargar un mapa que  este en un txt

2 - el Usuario debe identificar el origen y el final

3 - se debe de inngresar una matrix cuadrada, el tiempo
limite son la cantidad de saltos maximos para  encontrar el destino
en este caso el programa lo calcula automaticamente

4- hay un metodo que se llama resolverLaberinto(self, pivX, pivY, tiempo_transcurrido, ruta):
funciona con backtracking

pivx :  es la pos x inicial
pivy : es la pos  y inicial
tiempo_t  : es el tiempo que lleva... sirve para controlar  que  no de  vueltas infinitamente
ruta: le entra [] y controla el camino que se debe recorrer


"""

class Laberinto:
    def __init__(self):
        self.mapa = []
        self.cargarMapa()
        self.origen = None
        self.definirOrigen()
        self.destino = None
        self.definirDestino()
        self.tiempoLimite = None
        self.definirTiemoLimite()
        self.solucionLaberinto = []


    """
    Se carga un archivo desde HDD
    luego de ello se organiza el self.mapa
    para dejarlo mas manejable
    """
    def cargarMapa(self):
        try:
            f = open('labLoko.txt', 'r')
            rutas = f.read()

            vec = []
            for i in str(rutas).split('\n'):
                for j in i:
                    vec.append(j)
                self.mapa.append(vec)
                vec = []
        except:
            print('error faltal, no puedo cargar el  mapa!!!')


    def definirOrigen(self):
        print('Vamos  a ingresar (x, y) el  origen:')
        x = input('X Ingresa un numero menor a '+str(len(self.mapa[0]) - 1)+':\n')
        y = input('Y Ingresa un numero menor a ' + str(len(self.mapa) - 1) + ':\n')

        try:
            if  0 <= int(x) < len(self.mapa[0]) - 1 and 0 <= int(y) < len(self.mapa) - 1:
                self.origen =  int(x), int(y)
                self.mapa[int(y)][int(x)] = 'A'
            else:
                print('Error Fatal!, ingresando origen')
        except:
            print('Error Fatal!, ingresando origen')

    def definirDestino(self):
        print('Vamos  a ingresar (x, y) el  Destiino:')
        x = input('X Ingresa un numero menor a ' + str(len(self.mapa[0]) - 1) + ':\n')
        y = input('Y Ingresa un numero menor a ' + str(len(self.mapa) - 1) + ':\n')

        try:
            if 0 <= int(x) < len(self.mapa[0]) - 1 and 0 <= int(y) < len(self.mapa) - 1:
                self.destino = int(x), int(y)
                self.mapa[int(y)][int(x)] = 'B'
            else:
                print('Error Fatal!, ingresando origen')
        except:
            print('Error Fatal!, ingresando origen')


    def definirTiemoLimite(self):
        self.tiempoLimite = len(self.mapa) * len(self.mapa[0])


    def resolverLaberinto(self, pivX, pivY, tiempo_transcurrido, ruta):

        ruta.append((pivX, pivY))

        # si encontre el destino
        if pivY == self.destino[1] and pivX == self.destino[0]:


            # Yo estoy parado en la solucion
            # Si es la primera vez guardo el camino y no tengo que comparar
            if len(self.solucionLaberinto) == 0:
                # Ojo no me  sirve que apunte a  la  misma pos de memoria
                for i  in ruta:
                    self.solucionLaberinto.append(i)


            # si la ruta es mas corta la guardo
            if len(ruta) < len(self.solucionLaberinto):
                # Ojo no me  sirve que apunte a  la  misma pos de memoria
                for i in ruta:
                    self.solucionLaberinto.append(i)

            return tiempo_transcurrido

        # si no tiene solucion
        if tiempo_transcurrido == self.tiempoLimite:
            return 'no  hay solucion'

        # Marco el mapa para no volver a pasar por ahi
        self.mapa[pivY][pivX] = '1'

        # Este vector contiene los tiempos
        tiempos = []


        # Puedo echar para Arriba ?
        if pivY > 0 and self.mapa[pivY - 1][pivX] != '1':

            tiempo = self.resolverLaberinto(pivX, pivY - 1, tiempo_transcurrido + 1, ruta)
            if tiempo:
                tiempos.append(tiempo)



        # Puedo echar para Abajo ?
        if pivY < len(self.mapa) - 1 and self.mapa[pivY + 1][pivX] != '1':

            # me  voy pa abajo
            tiempo = self.resolverLaberinto(pivX, pivY + 1,  tiempo_transcurrido + 1, ruta)

            if tiempo:
                tiempos.append(tiempo)


        # Puedo echar para Derecha ?
        if pivX < len(self.mapa[0]) - 1 and self.mapa[pivY][pivX + 1] != '1':

            # me voy pa la derecha
            tiempo = self.resolverLaberinto(pivX + 1, pivY, tiempo_transcurrido + 1,  ruta)

            if tiempo:
                tiempos.append(tiempo)

        # Puedo echar para izquierda ?
        if pivX > 0 and self.mapa[pivY][pivX - 1] != '1':

            # me voy pa atraz
            tiempo = self.resolverLaberinto(pivX - 1, pivY, tiempo_transcurrido + 1,  ruta)

            if tiempo:
                tiempos.append(tiempo)

        # como ya se dio el paso se habilita  otra vez la celda
        self.mapa[pivY][pivX] = '0'

        return min(tiempos) if tiempos else None


    def verMapa(self):
        for i in self.mapa:
            print(i)

#  Se crea el mapa
l =  Laberinto()
resp = l.resolverLaberinto(l.origen[0], l.origen[1], 0, [])
print('la Solucion del  laberinto esta en :'+str(resp))
print(l.solucionLaberinto)
