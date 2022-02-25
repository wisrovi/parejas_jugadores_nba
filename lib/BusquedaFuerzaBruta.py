from Decoradores import calcular_tiempo
from Base import Base


class BusquedaFuerzaBruta(Base):
    personas = list()

    @calcular_tiempo
    def search(self, value):
        for i in range(len(self.data)):
            for j in range(i, len(self.data), 1):
                suma = int(self.data[i].get("h_in")) + int(self.data[j].get("h_in"))
                if suma == value:
                    self.personas.append(
                        (
                            f'{self.data[i].get("first_name")} {self.data[i].get("last_name")}',
                            f'{self.data[j].get("first_name")} {self.data[j].get("last_name")}'
                        )
                    )

    def solve(self):
        print("Fuerza Bruta, complejidad O(n^2)")
        return self.personas


if __name__ == "__main__":
    fb = BusquedaFuerzaBruta()
    fb.search(139)  # tiempo = 0.03
    print(fb.solve())