import csv


# El programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
# region,provincia,distrito,dni,candidato,esvalido Si hay un candidato con >50% de votos válidos retornar un array
# con un string con el nombre del ganador Si no hay un candidato que cumpla la condicion anterior, retornar un array
# con los dos candidatos que pasan a segunda vuelta Si ambos empatan con 50% de los votos se retorna el que apareció
# primero en el archivo el DNI debe ser válido (8 digitos)

class CalculaGanador:

    def leerDatos(self, csv_file):
        data = []
        with open(csv_file, 'r') as csvfile:
            next(csvfile)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append(fila)
        return data

    def contarVotos(self, data):
        votosxcandidato = {}
        for fila in data:
            if not fila[4] in votosxcandidato:
                votosxcandidato[fila[4]] = 0
            if fila[5] == '1':
                votosxcandidato[fila[4]] = votosxcandidato[fila[4]] + 1
        totalVotos = sum(votosxcandidato.values())
        return votosxcandidato, totalVotos

    def calcularGanador(self, votosxcandidato, totalVotos):
        votosxcandidato = {k: v for k, v in sorted(votosxcandidato.items(), key=lambda item: item[1], reverse=True)}
        print(votosxcandidato)

        if votosxcandidato[list(votosxcandidato.keys())[0]] > totalVotos / 2:
            return [list(votosxcandidato.keys())[0]]

        if votosxcandidato[list(votosxcandidato.keys())[0]] == totalVotos / 2 and votosxcandidato[list(votosxcandidato.keys())[1]] == totalVotos / 2:
            return [list(votosxcandidato.keys())[0]]

        return [list(votosxcandidato.keys())[0], list(votosxcandidato.keys())[1]]


c = CalculaGanador()
datatest = [
    ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
    ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
]

data = c.leerDatos('0204.csv')
votos, total = c.contarVotos(data)
print('Ganador(es): ', c.calcularGanador(votos, total))
