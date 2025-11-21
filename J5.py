class Vasile:
    def init(self, mark, sal):
        self.mark = mark
        self.sal = sal

    def namayesh_etelaat(self):
        print("Mark:", self.mark)
        print("Sal:", self.sal)


class Mashin(Vasile):
    def init(self, mark, sal, tedade_dar):
        super().init(mark, sal)
        self.tedade_dar = tedade_dar

    def namayesh_etelaat(self):
        super().namayesh_etelaat()
        print("Tedade dar:", self.tedade_dar)


class Motor(Vasile):
    def init(self, mark, sal, sidecar_darad):
        super().init(mark, sal)
        self.sidecar_darad = sidecar_darad

    def namayesh_etelaat(self):
        super().namayesh_etelaat()
        print("Sidecar darad:", self.sidecar_darad)



v = Vasile("Saipa", 1401)
c = Mashin("Pride", 1402, 4)
m = Motor("Tiba", 1400, False)


v.namayesh_etelaat()
c.namayesh_etelaat()
m.namayesh_etelaat()