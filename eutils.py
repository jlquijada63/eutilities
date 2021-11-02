
import requests
from bs4 import BeautifulSoup
import lxml



class Eutils:
	''' utilizacion de los servicios de la API eutilites para busquedas en pubmed '''

	def __init__(self,*term,ret_max=10):

		''' constructor que utiliza el servicio esearch y obtiene las variables de entorno (webenv y querykey) y una lista 
		de los pmid's '''

		url ="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"				#servicio esearch
		terms = "+".join(term)
		self.retmax = ret_max
		payload = {'db':'pubmed', 'term':terms, 'usehistory': 'y', 'retmax': self.retmax}
		response = requests.get(url,params=payload)
		soup = BeautifulSoup(response.text,'lxml')
		self.WebEnv = soup.find('webenv').text											#variable de entorno webenv
		self.query_key = soup.find('querykey').text										#variable de entorno query_key
		self.pmid = [e.text for e in soup.find_all('id')]	
		self.setTitle()							#lista de pmid's de los articulos

	def setTitle(self):
		''' obtiene los titulos de los articulos '''

		url ="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
		payload = {'db': 'pubmed', 'retmax':self.retmax, 'WebEnv':self.WebEnv, 'query_key': int(self.query_key)}
		response = requests.get(url,payload)
		soup = BeautifulSoup(response.text, 'lxml')
		titles = soup. find_all('item', {'name':'Title'})
		self._list_titles = [e.text for e in titles]

	@property
	def titles(self):
		''' nuestra la lista de titulos '''
		return self._list_titles







	
