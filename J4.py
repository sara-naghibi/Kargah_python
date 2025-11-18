class Ketab:
    def __init__(self, onvan, nevisande, gheymat):
        self.onvan = onvan
        self.nevisande = nevisande
        self.gheymat = gheymat

    def namayesh_joziat(self):
        print("Onvan:", self.onvan)
        print("Nevisande:", self.nevisande)
        print("Gheymat:", self.gheymat)
        print("------------------------")

    def takhfif_dah(self, darsad):
        meghdar_takhfif = (self.gheymat * darsad) / 100
        self.gheymat = self.gheymat - meghdar_takhfif


print("Daneshgah Sadjad")

ketab1 = Ketab("Python Basics", "Ali Rezaei", 200)
ketab2 = Ketab("Learning Java", "Sara Ahmadi", 180)

print("Ghabl az takhfif:")
ketab1.namayesh_joziat()
ketab2.namayesh_joziat()

ketab2.takhfif_dah(10)

print("Bad az takhfif:")
ketab1.namayesh_joziat()
ketab2.namayesh_joziat()
