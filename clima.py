# clima.py

class ClimaDiario:
    def __init__(self, temperatura=0.0, humedad=0.0, precipitacion=0.0):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__precipitacion = precipitacion

    def get_temperatura(self):
        return self.__temperatura

    def get_humedad(self):
        return self.__humedad

    def get_precipitacion(self):
        return self.__precipitacion


class ClimaSemanal:
    def __init__(self):
        self.dias = []

    def agregar_dia(self, clima_diario):
        if isinstance(clima_diario, ClimaDiario):
            self.dias.append(clima_diario)

    def promedio_semanal(self):
        if len(self.dias) == 0:
            return None
        n = len(self.dias)
        temp_total = sum(d.get_temperatura() for d in self.dias)
        hum_total = sum(d.get_humedad() for d in self.dias)
        prec_total = sum(d.get_precipitacion() for d in self.dias)
        return {
            "Temperatura": temp_total / n,
            "Humedad": hum_total / n,
            "Precipitación": prec_total / n
        }

    def lista_dias(self):
        return [(i, d.get_temperatura(), d.get_humedad(), d.get_precipitacion()) for i, d in enumerate(self.dias, start=1)]
