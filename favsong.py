from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:bowbow#21@localhost/favsongs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class favsongs(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	artist= db.Column(db.String(30))
	song = db.Column(db.String(2000))


@app.route('/')
def index():
	result = favsongs.query.all()
	return render_template('index.html', result=result)


@app.route('/favsong')
def favsong():
	 return render_template('favsong.html')

@app.route('/process', methods =['POST'])
def process():
# artist=''
	# try :
	artist = request.form['artist']
	# except :
	# print('dibs!')
	song = request.form['song']
	songdata =favsongs(artist=artist,song=song)
	db.session.add(songdata)
	db.session.commit()

	return redirect(url_for('index'))
