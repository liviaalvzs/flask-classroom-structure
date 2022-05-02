from flask import Flask, jsonify, request

app = Flask(__name__) 
		
@app.route("/") 
def hello():
        print("rodei mesmo") 
        return "Hello World!"

@app.route("/nomes", methods=["GET"]) #no app,route, especificamos URL e verbo
def hello2():
        return "Eder, Ana e outros"   #a funcao retorna uma string

dados = {"alunos":[
                   {"nome":"lucas","id":15},
                   {"nome":"cicero","id":29},
                  ], 
        "professores":[]}

'''atende em /alunos, verbo GET'''
@app.route("/alunos", methods=["GET"])
def alunos():
    return jsonify(dados['alunos']) 
    'json ify = json ificar'
    "ele nao sabe retornar listas, mas sabe retornar strings"
    "entao, transforma a minha lista numa string json"

@app.route("/alunos/<int:nAluno>")
def alunoPorId(nAluno):
    for i in dados['alunos']:
        if i['id'] == nAluno:
            return i
    return {'erro':'aluno nao encontrado'}, 400

'''atende em /alunos, verbo POST'''
@app.route("/alunos", methods=["POST"])
def cria_aluno():
    dict = request.json #request.json representa um arquivo json enviado ao servidor
    #nosso servidor recebeu um arquivo e colocou nessa variavel
    dados['alunos'].append(dict)
    return jsonify(dados['alunos']) 


@app.route("/reseta", methods=["POST"])
def reseta():
    dados['alunos'] = []
    dados['professores'] = []
    return dados

@app.route("/alunos/<int:nAluno>", methods=["DELETE"])
def apaga(nAluno):
    indice = 0
    for i in dados['alunos']:
        if i['id'] == nAluno:
            del (dados['alunos'])[indice]
            return jsonify(dados['alunos'])
        indice += 1
    return {'erro':'aluno nao encontrado'}, 400
        
    
@app.route("/alunos/<int:nAluno>", methods=["PUT"])
def edita(nAluno):
    dictNome = request.json
    for i in dados['alunos']:
        if i['id'] == nAluno:
            i['nome'] = dictNome['nome']
            return dados
    return {'erro':'aluno nao encontrado'}, 400

        

if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)