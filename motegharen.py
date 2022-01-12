a = input("array ro vared konid: ")

number_mot = a.split()


mot = len(number_mot)

mot_find = False

for i in range(mot):

     if number_mot[i] ==  number_mot[mot - 1]:

         mot_find = True
     else :

         mot_find = False

         break

     mot -= 1

if mot_find == False:

    print("motegharen nist")

else:
    
    print("motegharen hast")