from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    tasks.append({'title': title, 'complete': False})
    return redirect(url_for('index'))

@app.route('/update/<int:id>')
def update_task(id):
    tasks[id]['complete'] = not tasks[id]['complete']
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    del tasks[id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)