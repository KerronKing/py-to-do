from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  content = db.Column(db.String(200), nullable = False)
  completed = db.Column(db.Integer, default = 0)
  date_created = db.Column(db.DateTime, default = datetime.utcnow)

def __repr__(self):
  return '<Task %r>' % self.id

@app.route('/', methods = ['POST', 'GET'])

def index():
  if request.method == 'POST':
    todo_content = request.form['content']
    new_content = Todo(content = todo_content)

    try:
      db.session.add(new_content)
      db.session.commit()
      return redirect('/')
    except:
      return 'There was an issue adding the todo item'

  else:
    todos = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html', todos = todos)

@app.route('/delete/<int:id>')

def delete(id):
  todo_to_delete = Todo.query.get_or_404(id)
  
  try:
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect('/')
  except:
    return 'There was an error deleting that todo item'

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
  todo = Todo.query.get_or_404(id)

  if request.method == 'POST':
    todo.content = request.form['content']

    try:
      db.session.commit()
      return redirect('/')
    except:
      return 'There was an issue updating that todo item'

  else:
    return render_template('update.html', todo = todo)

if __name__ == '__main__':
  app.run(debug = True)