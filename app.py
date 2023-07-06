import csv
import flask

app = flask.Flask(__name__)


class CalculaGanador:

    def leerDatos(self, csv_file):
        csv_file_data = csv_file.read().decode("utf-8").splitlines()[1:]
        data = []
        for row in csv_file_data:
            data.append(row.split(','))
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

    # return candidate name and votes
    def calcularGanador(self, votosxcandidato, totalVotos):
        votosxcandidato = {k: v for k, v in sorted(votosxcandidato.items(), key=lambda item: item[1], reverse=True)}

        if votosxcandidato[list(votosxcandidato.keys())[0]] > totalVotos / 2:
            return [{"name": list(votosxcandidato.keys())[0], "votes": votosxcandidato[list(votosxcandidato.keys())[0]]}]

        if votosxcandidato[list(votosxcandidato.keys())[0]] == totalVotos / 2 and votosxcandidato[
            list(votosxcandidato.keys())[1]] == totalVotos / 2:
            return [{"name": list(votosxcandidato.keys())[0], "votes": votosxcandidato[list(votosxcandidato.keys())[0]]}]

        return [{"name": list(votosxcandidato.keys())[0], "votes": votosxcandidato[list(votosxcandidato.keys())[0]]},
                {"name": list(votosxcandidato.keys())[1], "votes": votosxcandidato[list(votosxcandidato.keys())[1]]}]


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/ganador', methods=['POST'])
def ganador():
    csv_file = flask.request.files['results']
    c = CalculaGanador()
    data = c.leerDatos(csv_file)
    votos, total = c.contarVotos(data)
    return flask.jsonify(c.calcularGanador(votos, total))


if __name__ == '__main__':
    app.run(debug=False)
