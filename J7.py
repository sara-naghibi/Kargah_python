import csv

class Mokhatab:
    def __init__(self, nam, shomare):
        if not shomare.isdigit():
            raise ValueError("shomare tel bayad faghat adad bashad")
        self.nam = nam
        self.shomare = shomare

class DaftarcheTelfon:
    def __init__(self):
        self.liste_mokhatabin = []

    def afzoodan_mokhatab(self, nam, shomare):
        try:
            jadid = Mokhatab(nam, shomare)
            self.liste_mokhatabin.append(jadid)
            print("Mokhatab ba movafaghiat ezafe shod.")
        except ValueError as e:
            print(f"Khataye format: {e}")

    def zakhire_dar_csv(self, nam_file):
        with open(nam_file, mode='w', newline='') as f:
            nevisande = csv.writer(f)
            for m in self.liste_mokhatabin:
                nevisande.writerow([m.nam, m.shomare])

    def bazyabi_az_csv(self, nam_file):
        try:
            with open(nam_file, mode='r') as f:
                khanande = csv.reader(f)
                for satr in khanande:
                    try:
                        nam = satr[0]
                        shomare = satr[1]
                        self.liste_mokhatabin.append(Mokhatab(nam, shomare))
                    except (ValueError, IndexError):
                        continue
        except FileNotFoundError:
            print("File peyda nashod, daftarche taze ijad shod.")

    def namayeshe_hame(self):
        if not self.liste_mokhatabin:
            print("Daftarche khali ast.")
        for m in self.liste_mokhatabin:
            print(f"Nam: {m.nam} | Tel: {m.shomare}")

daftarche = DaftarcheTelfon()
daftarche.bazyabi_az_csv("contacts.csv")

while True:
    print("\n1. Afzoodan\n2. Namayesh\n3. Zakhire o Khorooj")
    entekhab = input("Gozine ra entekhab konid: ")

    if entekhab == "1":
        n = input("Nam: ")
        s = input("Shomare: ")
        daftarche.afzoodan_mokhatab(n, s)
    
    elif entekhab == "2":
        daftarche.namayeshe_hame()
    
    elif entekhab == "3":
        daftarche.zakhire_dar_csv("contacts.csv")
        break
    
    else:
        try:
            adad = int(entekhab)
            print("In gozine dar list nist.")
        except ValueError:
            print("Lotfan faghat adad vared konid.")
