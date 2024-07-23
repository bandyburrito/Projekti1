def tekst():
    num_students = int(input("Shkruani numrin total te nxeneseve ne klase: "))
    
    students = {}
    for i in range(num_students):
        emri = input(f"Shkruani emrin e nxenesit {i+1}: ")
        while True:
            try:
                nota = float(input(f"Shkruani noten e nxenesit {emri}: "))
                break
            except ValueError:
                print("Ju lutem shkruani nje numer valid per noten.")
        
        students[emri] = nota
    
    notat = list(students.values())
    nota_minimale = min(notat)
    nota_maximale = max(notat)
    mesatarja_e_notave = sum(notat) / num_students
    
    print(f"\nRezultatet")
    print(f"Nota minimale ne klase eshte: {nota_minimale}")
    print(f"Nota maximale ne klase eshte: {nota_maximale}")
    print(f"Mesatarja e notave ne klase eshte: {mesatarja_e_notave:.2f}")
    
    nxenesit_kalojne = {}
    nxenesit_nuk_kalojne = {}
    
    for emri, nota in students.items():
        if nota >= 3:
            nxenesit_kalojne[emri] = nota
        else:
            nxenesit_nuk_kalojne[emri] = nota
    
    return nxenesit_kalojne, nxenesit_nuk_kalojne
            
def kaluar(nxenesit_kalojne):
    print("\nNxenesit qe kane kaluar")
    if nxenesit_kalojne:
        for emri, nota in nxenesit_kalojne.items():
            print(f"Emri: {emri}, Nota: {nota}")
    else:
        print("Nuk ka nxenes qe kane kaluar me noten me te madhe se 3.")
        
def ngel(nxenesit_nuk_kalojne):
    print("\nNxenesit qe nuk kane kaluar")
    if nxenesit_nuk_kalojne:
        for emri, nota in nxenesit_nuk_kalojne.items():
            print(f"Emri: {emri}, Nota: {nota}")
    else:
        print("Nuk ka nxenes qe nuk kane kaluar me noten me te vogel se 3.")

if __name__ == "__main__":
    nxenesit_kalojne, nxenesit_nuk_kalojne = tekst()
    kaluar(nxenesit_kalojne)
    ngel(nxenesit_nuk_kalojne)