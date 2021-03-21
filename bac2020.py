
coef = 100 # les coef
l = [ ]   
    
def sett(app,l):    
  valeur=int(input("Quel est votre moyenne en " + app + "?\n"))   # fonction qui nous permet d'eviter d'ecrire "votre moyenne est ?\n"
  while valeur > 20:                                              #  permet aussi que si le nombre est plus grand que 20 s'affiche un message d'error
    print("error vous avez saisi un nombre plus grand que 20 ")
    valeur=int(input("Quel est votre moyenne en " + app + "?\n"))
  if valeur < 10 :                                                # et sa nour permet que si un nombre est moins que 10 on le enregistre en liste de l[ ]      
    l.append(app) 
  return valeur 

dictt={}   
                                                                  # le dictionnaire nous permet d'enregistre chaque questions par rapport a sa matiere 
dictt["bulletin"]=sett("bulletin scolaire",[])                    # classe de de Première
dictt["histoire"]=sett("histoire",l)
dictt["langue_vivante1"]=sett("langue_vivante1",l)
dictt["langue_vivante2"]=sett("langue_vivante2",l)
dictt["Ens"]=sett("Ens",l)
dictt["spe1"]=sett("spe1",l)
dictt["ecrit"]=sett("ecrit",l)
dictt["oral"]=sett("orale",l)


dictt["EPS"]=sett("EPS",l)                                       # classe de Terminale
dictt["spe2"]=sett("spe2",l)                                    
dictt["spe3"]=sett("spe3",l)
dictt["philo"]=sett("philo",l)
dictt["Grand_oral"]=sett("Grand_oral",l)

diccof={}                                                         # j'ai remis le dictionnaire pour pouvoir mettre chaque coef avec chaque matiere       
diccof["bulletin"]=10
diccof["histoire"]=5
diccof["langue_vivante1"]=5
diccof["langue_vivante2"]=5
diccof["Ens"]=5
diccof["spe1"]=5
diccof["ecrit"]=5
diccof["oral"]=5
diccof["EPS"]=5
diccof["spe2"]=16
diccof["spe3"]=16
diccof["philo"]=8
diccof["Grand_oral"]=10

table = [["\tbulletin","\t 10",dictt["bulletin"]],                # un petit tableau qui nous permet juste d'afficher les donnees 
         ["Histoire-géographie","\t 5",dictt["histoire"]],
         ["Langue vivante 1","\t 5",dictt["langue_vivante1"]],
         ["Langue vivante 2","\t 5",dictt["langue_vivante2"]],
         ["ENns scientifique","\t 5",dictt["Ens"]],
         ["\tspé 1 \t","\t 5",dictt["spe1"]],
         ["Francais Ecrit ","\t 5",dictt["ecrit"]],
         ["Francais Oral","\t 5",dictt["oral"]],
         ["\tEPS\t","\t 5",dictt["EPS"]],
         ["\tspé 2\t","\t 16",dictt["spe2"]],
         ["\tspé 3\t","\t 16",dictt["spe3"]],
         ["Philosophie\t","\t 8",dictt["philo"]],
         ["Grand oral \t","\t 10",dictt["Grand_oral"]],]
        
print("\t| nom de la matiere \t| \tcoef  \t|\t note \t |\n")
for item in table:
    print("\t|",item[0],"\t|",item[1],"\t|\t",item[2],"\t |")

total_point=0

for key,value in dictt.items():                                     # boucle que nous permet d'eviter d'ecrire chaque fois la meme chose   
    total_point = total_point + value * diccof[key]  

total = (total_point/coef)                                          # on calcule la moyenne  
points = (total_point-1000)                                         # on calcule les points    

print("\n votre moyenne =  \t",total,"et voici vos points\t",total_point)

if(points <= -210  ):
    print("\n vous n avez pas eu votre bac et vous ne pouvez pas aller au rattrapage \n")

elif (points >= -210 and points < 0  ):
    print("\n vous allez au rattrapage vous avez  ",abs(points),"points a rattraper\n")
    print("voici les matiere que vous avez pas eu la moyenne :\n",l)
    print("vous devez choisir 2 matiere pour passer le rattrapage dessus\n")
    reponse = int(input("\n votre premiere choix en chiffre \t "))-1
    reponse1 = int(input("\n votre deuxieme choix en chiffre \t "))-1
    print(l[reponse]+"\t et \t"+l[reponse1])
    j=dictt[l[reponse]]*diccof[l[reponse]]+dictt[l[reponse1]]*diccof[l[reponse1]]
   
    total_point=total_point-j

    dictt[l[reponse]]=sett(l[reponse]+" au rattrapage",l)
    dictt[l[reponse1]]=sett(l[reponse1]+" au rattrapage",l)
    j=dictt[l[reponse]]*diccof[l[reponse]]+dictt[l[reponse1]]*diccof[l[reponse1]]
    total_point=total_point+j

    print ("\n voici vos total des points \t",total_point)
    points = (total_point-1000)
    
    if total_point >= 1000:
        print("\n vous avez attraper votre retard et vous avez eu votre bac  \n voici vos points\t",total_point,"\t et vous avez",points," d'avance \n")
    else:
        print("\n vous avez pas eu votre bac au rattrapage il vous manquer \t",abs(points),"points") 
        

    

elif(points >=  0 and points < 200 ):
    print("\n vous avez eu votre bac sans mention avec ",points,"points d'avance")

elif (points >= 200 and points < 400  ):
    print("\n vous avez eu votre bac avec mention assez bien avec ",points,"points d'avance"  )

elif (points >= 400 and points < 600  ):
    print("\n vous avez eu votre bac avec mention bien avec ",points,"points d'avance" )

elif (points >= 600 and  points < 800  ):
    print("\n vous avez eu votre bac avec mention tres bien avec ",points,"points d'avance" )

else:
    print("\n vous avez eu votre bac avec les Félicitations du Jury avec ",points,"points d'avance" )





