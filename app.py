from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

lista_tarefas = [{'nome' : 'teste', 'feito' : False}]


@app.route("/")
def index():
    return render_template("index.html", lista_tarefas=lista_tarefas)


@app.route("/add", methods=["POST"])
def add():
    nome_tarefa = request.form['nome_tarefa']
    lista_tarefas.append({'nome' : nome_tarefa, 'feito' : False})
    return redirect(url_for("index"))


@app.route("/edit/<int:index>", methods=['GET', 'POST'])
def edit(index):
    tarefa = lista_tarefas[index]
    if request.method == 'POST':
        tarefa['nome'] = request.form['nome_tarefa']
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", tarefa=tarefa, index=index)


@app.route("/check/<int:index>")
def check(index):
    lista_tarefas[index]['feito'] = not lista_tarefas[index]['feito']
    return redirect(url_for("index"))


@app.route("/delete/<int:index>")
def delete(index):
    del lista_tarefas[index]
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
