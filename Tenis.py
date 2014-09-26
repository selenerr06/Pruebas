
#/usr/bin/env python
import unittest

class Tenis():
	j1=0
	j2=0
	sets1=0
	sets2=0
	
	
	def anotar(texto):
		puntaje=0
		if(texto=="jugador1"):
			if(j1==0):
				j1=15
			if(j1==15):
				j1=30
			if(j1==30):
				j1=40
			if(j1==40):
				j1="set"
			if(j1=="set"):
				j1="deuse"
			if(j1=="set"):
				j1="deuse"
			if(j1=="deuse"):
				j1="adv"
			if(j1=="adv"):
				j1="Ganado"
			puntaje=j1
		if(texto=="jugador2"):
			if(j2==0):
				j2=15
			if(j2==15):
				j2=30
			if(j2==30):
				j2=40
			if(j2==40):
				j2="set"
			if(j2=="set"):
				j2="deuse"
			if(j2=="set"):
				j2="deuse"
			if(j2=="deuse"):
				j2="adv"
			if(j2=="adv"):
				j2="Ganado"
		
			puntaje=j2
		return puntaje;
	

	def anotar(jugador):
		res="";
		if(texto=="jugador1"):
			if(sets1+2==sets2):
				res= "J1="+j1+"\n"+"J2="+j2+"\nJ2=GANADOR"
			if(sets2+2==sets1):
				res= "J1="+j1+"\n"+"J2="+j2+"\nJ1=GANADOR"
				
		elif(texto=="jugador2"):
			if(sets1+2==sets2):
				res= "J1="+j1+"\n"+"J2="+j2+""+"\nJ2=GANADOR"
			if(sets2+2==sets1):
				res= "J1="+j1+"\n"+"J2="+j2+""   +"\nJ1=GANADOR"  
				
		return res;	
