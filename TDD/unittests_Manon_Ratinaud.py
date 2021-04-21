import unittest
import OOPStella

class TestSharks(unittest.TestCase):
	Peeta=OOPStella.Whale_Sharks("Peeta","Florida",1000,"Krill","Friendly")
	Steve=OOPStella.Great_Whites("Steve","Brasil",800, 500,5)
	known_sharks = (Peeta,Steve)
	names=("Peeta","Steve")

	def test_getName(self):
		i=0
		for shark in self.known_sharks :
			self.assertEqual(OOPStella.Sharks.getName(shark),TestSharks.names[i])
			i+=1

	def test_krill(self):
		'''The shark cannot eat more than itself'''
		snackWeight = 200
		for shark in self.known_sharks:
				if isinstance(shark,OOPStella.Whale_Sharks) :
					init_weight=shark.weight
					if snackWeight>init_weight:
						print("Wow I'm not that hungry !")
					OOPStella.Whale_Sharks.krillTime(shark,snackWeight)
					self.assertEqual(shark.weight,init_weight+snackWeight)

	def test_teeth(self):
		for shark in self.known_sharks:
			if isinstance(shark,OOPStella.Great_Whites) :
				init_teeth=shark.teeth
				OOPStella.Great_Whites.teethReplacement(shark)
				self.assertEqual(init_teeth+100,shark.teeth)

	def test_initsharks(self):
		'''Vérifie que les requins sont bien initialisés'''
		l=(OOPStella.james,OOPStella.sharky)
		if isinstance(l[0].weight,str )or isinstance(l[1].weight,str) :
			print("Weight must be int")
			raise TypeError
		for shark in l:
			if isinstance(shark,OOPStella.Great_Whites) and (isinstance(shark.teeth,str)or isinstance(shark.age,str)):
				print("Number of teeth and age must be int")
				raise TypeError
		

if __name__ == '__main__':
	unittest.main()