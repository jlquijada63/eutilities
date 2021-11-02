

from argparse import *
from eutils import Eutils


parser = ArgumentParser(description= "Utilizacion de la libreria eutilities")
parser.add_argument('-t', '--terms', type = str,help="terminos de busqueda")
parser.add_argument('-s', '--retmax', type= int,help="numero de articulos maximo a recibir")

params= parser.parse_args()



if __name__ == '__main__':

	question = Eutils(params.terms, ret_max = params.retmax)
	for title in question.titles:
		print (title)


