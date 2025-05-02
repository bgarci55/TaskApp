from flask import Flask, render_template, request, redirect, url_for
from task_manager import TaskManager

app = Flask(__name__)

task_manager = TaskManager()

@app.route('/')
def index():
    return render_template('index.html', tasks=task_manager.tasks)

if __name__ == '__main__':
    app.run(debug=True)