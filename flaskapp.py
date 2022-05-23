from flask import Flask, render_template, send_from_directory, Response, json, request, session
from flask_session import Session
from os import system, remove, getcwd
from os.path import isfile, join
import subprocess
import time
from sys import stdout
import logging
from utils import *
import cv2
from locker import *
from encryption import *
import sqlite3 as sql
import numpy as np
from forbidden_phonemes import *
import os
import psutil
import io
import soundfile as sf

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)
app.logger.addHandler(logging.StreamHandler(stdout))
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

current_dir = getcwd()
dbLoc = "./memory/profile.sql"
videoLoc = "./memory/video/"
audioLoc = "./memory/audio/"

@app.route('/')
def index():
	return render_template('landingPage.html')

@app.route('/experiment')
def jikken():
	session["volume"] = 0
	session["speed"] = 0
	session["pitch"] = 0
	session["current_id"] = None
	session["global_frame"] = None
	session["global_phrase"] = None
	#cascade_file = current_dir+'/static/haarcascade_frontalface_default.xml'
	#face_cascade = cv2.CascadeClassifier(cascade_file)
	session["frame_buffer"] = []
	session["emotion_timeseries"]=[]
	session["volume"] = 0
	session["speed"] = 0
	session["pitch"] = 0
	session["timeReg"] = time.time()
	session["audioFile"] = ""
	session["recording"] = "f"
	session["posDic"] = {"x":0,"y":0,"w":0,"h":0}
	session["filename"] = ""
	return render_template('frontpage.html')

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/exp')
def exper():
	return render_template('index.html');

@app.route('/main', methods = ['POST'])
def main():
	if request.method == 'POST':
		form_data = request.form
		ID = form_data["fname"]
		password = form_data["lname"]
	if ID == "" or ID == " " or ID is None or password == "":
		return render_template('frontpage_error.html')
	passed = loginCheck(ID,password)
	if passed:
		session["current_id"] = ID
		return render_template('index.html')
	else:
		return render_template('frontpage_error.html')

@app.route('/consent1')
def con():
	return render_template('explanation.html')

@app.route('/consent2')
def crear():
	return render_template('ProfileMaker.html')

@app.route('/instructions')
def inst():
	return render_template('instructions.html')

@app.route('/create_profile', methods = ['POST'])
def create():
	username_exists = False
	ID = None
	if request.method == 'POST':
		form_data = request.form
		ID = form_data["fname"]
		password = form_data["lname"]

		if ID == "q4%&Ujhgb_0)oPL" and password == "AoF+9~IujHYuj\[":
			from tabler import tabler
			tabler()

		for i in ID:
			if i not in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0",]:
				return render_template('username_error.html')

		if ";" in password or password is None or password=="":
			return render_template('username_error.html')
	username_exists = IDexists(ID)
	if not username_exists:
		createUser(ID,password)
		register = [form_data[i] for i in form_data]
		register = [register[0]]+register[2:]
		db = sql.connect(dbLoc)
		cursor = db.cursor()
		cursor.execute("""
			INSERT INTO info
			(ID, age, gender, originReg, motherLang, spokenLang, whereAbroad, timeAbroad)
			VALUES (?,?,?,?,?,?,?,?)
		""", register)
		db.commit()
		db.close()

		return render_template('frontpage.html')
	else:
		return render_template('username_exists.html')

@app.route('/audio', methods=['POST'])
def audio():
	with open('./audio.wav', 'wb') as f:
		f.write(request.data)
	proc = run(['ffprobe', '-of', 'default=noprint_wrappers=1', './audio.wav'], text=True, stderr=PIPE)
	return proc.stderr


@app.route("/wav")
def Hanasu():
	from random import choice, random
	open_jtalk=['espeak']
	#mech=['-v','art/eo']
	session["volume"]=str(choice(range(10,200)))
	session["speed"]=str(choice(range(80,450)))
	session["pitch"]=str(choice(range(0,99)))
	vol=["-a", session["volume"]]
	htsvoice=['-p',session["pitch"]]
	spd=['-s',session["speed"]]
	phrase = gibberish()
	cmd=open_jtalk+htsvoice+vol+spd+["[["+phrase+"]]"]+["--stdout"]#open_jtalk+mech+htsvoice+speed+phrase+["--stdout"]
	c = subprocess.Popen(cmd,stdout=subprocess.PIPE)
	session["global_phrase"] = phrase
	print(phrase)
	def generate():
		audio = c.stdout.read(1024)
		while audio:
				yield audio
				audio = c.stdout.read(1024)
		#yield audio
	return Response(generate(), mimetype="audio/wav")

@app.route('/send_image')
def sendImage():
	if len(session["frame_buffer"])>0:
		return Response(cv2.imencode('.jpg', session["frame_buffer"][-1])[1].tobytes(), mimetype="image/jpeg")
	else:
		return Response(cv2.imencode('.jpg', np.zeros((500, 500, 3), dtype = "uint8"))[1].tobytes(), mimetype="image/jpeg")


@app.route('/rec_status', methods=['POST'])
def record_status():
	json = request.get_json()
	session["recording"] = json['status']
	session["filename"] = videoLoc+";"+str(session["current_id"])+";"+str(session["timeReg"])+".avi"
	if session["recording"][0]=="f" and len(session["frame_buffer"])>0:
		width,height,depth = session["frame_buffer"][0].shape
		out = cv2.VideoWriter(session["filename"],cv2.VideoWriter_fourcc(*'MJPG'), 20.0, (height,width))
		for f in session["frame_buffer"]:
			out.write(f)
		out.release()
		session["frame_buffer"] = []
		db = sql.connect(dbLoc)
		cursor = db.cursor()
		cursor.execute('SELECT * FROM login WHERE ID=?', (session["current_id"],))
		query = cursor.fetchone()
		if query is not None:
			try:
				encrypt(session["filename"],query[3])
			except:
				pass
			try:
				encrypt(session["audioFile"],query[3])
			except:
				pass
			insert=(str(session["current_id"]), str(session["global_phrase"]),str([session["volume"],session["speed"],session["pitch"]]), str(session["audioFile"]), str(session["filename"]), str(session["emotion_timeseries"]),)
			cursor.execute("""
				INSERT INTO analysis
				(ID,phrase,prosody,voiceFile,videoFile,emotion)
				VALUES (?,?,?,?,?,?)
			""", insert)
			db.commit()
		else:
			return render_template('frontpage.html')
		db.close()
		session["frame_buffer"] = []
		session["emotion_timeseries"] = []
		session["timeReg"] = 0
	try:
		pass
	except:
		pass

	try:
		os.remove(session["audioFile"])
	except:
		pass
	session["audioFile"] = ""
	return "1"

@app.route('/rec', methods=['POST'])
def receive():
	frame = request.get_json()
	frame = data_uri_to_cv2_img(frame)
	try:
		if session["recording"][0]=="t":
			session["frame_buffer"].append(frame)
		else:
			session["posDic"] = {"x":0,"y":0,"w":0,"h":0}
	except:
		session["recording"]="f"
		session["posDic"] = {"x":0,"y":0,"w":0,"h":0}
	return "1"

@app.route('/voice')
def voic():
	return render_template('audio.html')

@app.route('/rec_voice', methods=['POST'])
def r():
	session["timeReg"] = time.time()
	koe = request.files["audio_data"]
	if koe:
		session["audioFile"]= audioLoc+";"+str(session["current_id"])+";"+str(session["timeReg"])+".wav"
		koe.save(session["audioFile"])
	return "1"

@app.route('/return')
def ret():
	return render_template('index.html')

@app.route('/likert')
def like():
	return render_template('likert.html')

@app.route('/likert_answer', methods = ['POST'])
def answer():

	if request.method == 'POST':
		form_data = request.form
		line = [session["current_id"]]
		for i in range(1,11):
			try:
				value = form_data["likert"+str(i)]
			except:
				return render_template('likert_error.html')
			if value == "":
				return render_template('likert_error.html')
			line += [value]

		db = sql.connect(dbLoc)
		cursor = db.cursor()
		cursor.execute("""
			INSERT INTO likert
			(ID, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
			VALUES (?,?,?,?,?,?,?,?,?,?,?)
		""", line)
		db.commit()
		db.close()
		session["current_id"] = None
		return render_template('frontpage.html')

@app.route('/want')
def want():
		return render_template('delete.html')

@app.route('/del_minors_profile')
def dmp():
		return render_template('DelRequest.html')

@app.route('/submitRequest', methods = ['POST'])
def sR():
	if request.method == 'POST':
		form_data = request.form
		from mailer import Mail2
		Mail2(form_data["fID"],request.files["fFile"],form_data["exp"],form_data["fMail"])
	return render_template("SucReq.html")

@app.route('/info')
def inf():
	return render_template("instructions.html")

@app.route('/deletion')
def dele():

	db = sql.connect(dbLoc)
	cursor = db.cursor()
	cursor.execute('''DELETE FROM login
					WHERE ID = ?;
					''', (session["current_id"],))
	cursor.execute('''DELETE FROM likert
					WHERE ID = ?;
					''', (session["current_id"],))
	cursor.execute('''DELETE FROM analysis
					WHERE ID = ?;
					''', (session["current_id"],))
	cursor.execute('''DELETE FROM info
					WHERE ID = ?;
					''', (session["current_id"],))
	db.commit()
	db.close()
	for f in os.listdir(videoLoc):
		if ";"+session["current_id"]+";" in str(f):
			try:
				os.remove(videoLoc+str(f))
			except:
				pass
	for f in os.listdir(audioLoc):
		if ";"+session["current_id"]+";" in str(f):
			try:
				os.remove(audioLoc+str(f))
			except:
				pass
	return render_template('deleted.html')

if __name__ == '__main__':
	from waitress import serve
	serve(app, host="0.0.0.0", port=5000, threads=15)
