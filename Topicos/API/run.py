from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for

app = Flask(__name__)

# Cursos:
cursos = [
    {
        'codigo': 1,
        'nome': u'Sistemas de Informação',
        'duracao': 4, 
        'ativo': True
    },
    {
        'codigo': 2,
        'nome': u'Engenharia Computação',
        'duracao': 5, 
        'ativo': False
    }
]



def make_public_curso(curso):
    new_curso = {}
    for field in curso:
        if field == 'codigo':
            new_curso['uri'] = url_for('get_curso', curso_codigo=curso['codigo'], _external=True)
        else:
            new_curso[field] = curso[field]
    return new_curso

@app.route('/flask/api/cursos', methods=['GET'])
def get_cursos():
    return jsonify({'cursos': [make_public_curso(curso) for curso in cursos]})

@app.route('/flask/api/cursos/<int:curso_codigo>', methods=['GET'])
def get_curso(curso_codigo):
    curso = [curso for curso in cursos if curso['codigo'] == curso_codigo]
    if len(curso) == 0:
        abort(404)
    return jsonify({'curso': [make_public_curso(curso[0])]})

@app.route('/flask/api/cursos', methods=['POST'])
def create_curso():
    curso = {
        'codigo': cursos[-1]['codigo'] + 1,
        'nome': request.json.get('nome', ""),
        'duracao': request.json.get('duracao', ""),
        'ativo': request.json.get('ativo', "")
    }
    validar_dados(curso)
    cursos.append(curso)
    return jsonify({'curso': [make_public_curso(curso)]}), 201

@app.route('/flask/api/cursos/<int:curso_codigo>', methods=['PUT'])
def update_curso(curso_codigo):
    curso = [curso for curso in cursos if curso['codigo'] == curso_codigo]
    validar_dados(curso)
    curso[0]['nome'] = request.json.get('nome', curso[0]['nome'])
    curso[0]['duracao'] = request.json.get('duracao', curso[0]['duracao'])
    curso[0]['ativo'] = request.json.get('ativo', curso[0]['ativo'])
    return jsonify({'curso': [make_public_curso(curso[0])]})
    
@app.route('/flask/api/cursos/<int:curso_codigo>', methods=['DELETE'])
def delete_curso(curso_codigo):
    curso = [curso for curso in cursos if curso['codigo'] == curso_codigo]
    if len(curso) == 0:
        abort(404)
    cursos.remove(curso[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def validar_dados(curso):
    if len(curso) == 0:
        abort(404)    
    if 'nome' in request.json and type(request.json['nome']) is not str:
        abort(400)
    if 'duracao' in request.json and type(request.json['duracao']) is not int:
        abort(400)
    if 'ativo' in request.json and type(request.json['ativo']) is not bool:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True)