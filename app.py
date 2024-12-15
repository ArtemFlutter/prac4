from flask import Flask, render_template 

app = Flask(__name__, template_folder='D:/DevOps/prac4/templates')

@app.route('/')
def home():
    return render_template('movie_or_music.html')

@app.route('/movie')
def movie():
    return render_template('movie.html')

@app.route('/music')
def music():
    return render_template('music.html')

if __name__ == '__main__':
    app.run(debug=True)