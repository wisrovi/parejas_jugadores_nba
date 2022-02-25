from lib.Base import Base
from lib.Decoradores import calcular_tiempo


class BusquedaHeuristica(Base):
    personas = list()

    def __busqueda_parejas(self, value: int) -> list:
        """
        me retorna la lista de alturas_pulgadas de las posibles parejas que coincidan con la solicitud
        para crear esta lista se usa la logica de ramificacion y poda,
        para asi no tener que buscar en todas las opciones sino en las mas prometedoras

        :param value: entero a evaluar para buscar parejas
        :return: lista de parejas de alturas que cumplen la condicion
        """

        pesos_correctos = list()
        opciones = list(set([int(elem.get("h_in")) for elem in self.data]))
        for opc in opciones:
            buscar = value - opc
            if min(opciones) > buscar > max(opciones):  # podamos para no seguir buscando
                break
            if buscar in opciones:
                pesos_correctos.append((opc, buscar))
        return pesos_correctos

    def __convertir_alturas_en_nombres(self, pesos_correctos: list) -> dict:
        """
        Para esta funcion se usa la logica de busqueda lineal
        Basicamente para las parejas de alturas busca los nombres de los jugadores que correspondan
        por ejemplo:
            si la altura es 70, entonces buscara todos los nombres de los jugadores que tengan dicha altura

        :param pesos_correctos: listado de parejas de alturas que cumplen la condicion
        :return: devuelve un diccionario de alturas, donde cada item del diccionario es una
        lista con los nombres de los jugadores de la NBA que tienen la altura señalada en la llave del diccionario
        """

        opciones = list(set([elem for pes in pesos_correctos for elem in pes]))
        personas_con_peso = {elem: [] for elem in opciones}
        for i, person in enumerate(self.data):
            if int(person.get("h_in")) in opciones:
                personas_con_peso.get(int(person.get("h_in"))).append(
                    f'{person.get("first_name")} {person.get("last_name")}')
        return personas_con_peso

    def __asociar_parejas_con_nombres(self, pesos_correctos: list, personas_con_peso: dict) -> list:
        """
        Para esta asociacion se usa la tecnica divide y venceras el objetivo de esta funcion es convertir las parejas
        de alturas en parejas de nombres, en tres pasos:

        1) Como algunas alturas pueden tener mas de un candidato de jugador, entonces se crean las combinaciones para
        las diferentes parejas de alturas pero pueden crearse parejas repetidas o redundantes, por ejemplo para la
        pareja a,b, se pueden crear dos combinaciones: ab y ba, que en terminos practicos son la misma pareja
        2) convertir cada pareja en nombres
        3) limpiar el resultado anterior para quitar las parejas redundantes Al dividir en tres pasos, se puede lograr
        que esta funcion no tenga complejidad O(n) sino complejidad O(0.05n), logrando optimizar el proceso y reducir la
        complejidad del algoritmo

        :param pesos_correctos: listado de parejas de alturas que cumplen la condición
        :param personas_con_peso: listado de nombres de las personas que cumplen las alturas del primer parametro
        :return:
        """

        temporal = list()
        for buscar in pesos_correctos:
            izq, der = personas_con_peso[buscar[0]], personas_con_peso[buscar[1]]
            [temporal.append(elem) for elem in
             [(izq[e[0]], e[1]) for i in range(len(izq)) for e in list(zip([i], der))]]

        for temp in temporal:
            opc1, opc2 = temp, (temp[1], temp[0])
            if (opc1 not in self.personas) and (opc2 not in self.personas) and (temp[1] != temp[0]):
                self.personas.append(temp)

    # @calcular_tiempo  # Decorador para medir el tiempo de ejecución usado por el algoritmo para resolver el problema
    def search(self, value: int) -> None:
        """
        Para tratar el problema se divide el mismo en tres bloques, haciendo uso de la logica divide y venceras para
        atacar el problema completo como subproblemas mas sencillos cuya suma resuelve el problema original.

        1) buscamos las combinaciones de parejas posibles para cumplir la condicion del problema donde con el numero dado
        se debe buscar parejas de jugadores cuya suma de alturas sea igual al valor a buscar, el parametro dado, pero
        en lugar de tratar el problema con todos los datos de entrada, se trata con solo una lista de las alturas posibles.
        2) para las parejas de alturas del bloque anterior, buscamos los nombres de los jugadores que tengan dicha altura
        3) relaciono los nombres de las personas con las parejas halladas en el bloque 1, y entrego la respuesta del bloque 1
        traducida en nombres de jugadores

        :param value: recibe un entero con el valor a buscar
        :return: No hay retorno de esta funcion debido a que la funcion solve es la encargada de retornar la respuesta
        """
        if not isinstance(value, int):
            assert isinstance(value, int) == True, "Debe proporcionar un valor int para el factor de busqueda"

        self.personas = list()
        pesos_correctos = self.__busqueda_parejas(value)  # Complejidad O(n)
        personas_con_peso = self.__convertir_alturas_en_nombres(pesos_correctos)  # Complejidad O(n)
        self.__asociar_parejas_con_nombres(pesos_correctos, personas_con_peso)  # Complejidad O(0.05n)

    def solve(self, out: bool = True) -> list:
        """
        Esta función devuelve el resultado del algoritmo, es decir la lista de parejas de nombres cuyas suma de alturas,
        sea igual al valor dado

        :param out: define si se imprime o no el texto:  "No se encontraron coincidencias", cuando no hay coincidencias,
        se pone en False para efectos de depuración
        :return:
        """
        if out:
            print("Busqueda por métodos heuristicos, complejidad O(2,05n)")

        if len(self.personas) > 0:
            return self.personas

        if out:
            print("No se encontraron coincidencias")


if __name__ == "__main__":
    rp = BusquedaHeuristica("https://mach-eight.uc.r.appspot.com/")
    rp.search(139)
    print(rp.solve())
