print("In ce an sunteti:")
print("1")
print("2")
print("3")
an=int(input("Enter your input:"))

print("Ce greutate ar trebui sa aiba materia:")
print("0 Usor")
print("1 Mediu")
print("2 Greu")
theChose0=int(input("Enter your input:"))

print("Cat de interesanta sa fie materia")
print("0 Nu ma intereseaza atat timp cat trec")
print("1 Interesant, dar nu vreau sa ma lupt cu ea")
print("2 Greu")
theChose1=int(input("Enter your input:"))

print("Sa fie o materie bazata pe practica, teorie sau ambele ?")
print("0 Practica")
print("1 Teorie")
print("2 Practica si Teorie")
theChose2=int(input("Enter your input:"))

if an==1:
    print("Nu exista optionale")


materii=[
            #an 2
        #Greutate
            [
                [
                 ["CDC","PLP","AG"],
                 ["PLP","AG"],
                 ["AG","QC"]
                ],
        #Interesant
                [
                 ["PLP","AG"],
                 ["CDC","PLP","AG"],
                 ["AG","QC"]
                ],
        #Practic
                [
                 ["CDC","PLP","QC"],
                 ["PLP","AG"],
                 ["AG"]
                ]
            ],

            #an 3
        #Greutate
            [
                 [
                  [".NET","DSFUM","RN"],
                  ["RN","AN3D","PMP"],
                  ["AN3D","PMP","RM","SO","ISSA"]
                 ],
        #Interesant
                [
                  [".NET","DSFUM","RN"],
                  ["RM","SO","ISSA","DSFUM"],
                  ["AN3D","PMP","RM","SO"]
                ],
        #Practic
                [
                  ["PMP","RM","SO"],
                  ["RM","SO","DSFUM","RN"],
                  [".NET","AN3D","ISSA"]
                ]
            ]
        ]

def intersection(tuple1,tuple2):
    aux=[]
    for i in tuple1:
        if i in tuple2:
            aux.append(i)
            print(i)
    return aux

def materiiAlese(anul,greutatea,interesanta,practica):
    a=materii[anul-2][0][greutatea]
    b=materii[anul-2][1][interesanta]
    c=materii[anul-2][2][practica]

    final = intersection(a,b)
    final = intersection(final,c)

    print("Materii pentru anul "+str(anul)+" sunt: "+str(final))

if an==1:
    print("nu exista optionale")
else:
    materiiAlese(an,theChose0,theChose1,theChose2)