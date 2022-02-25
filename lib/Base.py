"""
Clase encargada de descargar los datos y cargarlos en un archivo json
"""


class Base:
    import requests

    def __init__(self, url: str):
        """
        Esta clase descarga los datos de la web señalada y una vez la descarga sea completa, almacena el json descargado
        """
        if not isinstance(url, str):
            assert isinstance(url, str) == True, "Debe proporcionar una url en formato str"

        self.URL = url
        self.data = self.__download_data()
        if self.data is not None:
            self.data = self.data.get("values")

    def __download_data(self):
        """
        Esta función va a la web señalada y descarga los datos para resolver el problema

        :return: json con los datos traidos de la web
        """
        with self.requests.get(url=self.URL, params={}) as response:
            if response.status_code == 200:
                return response.json()