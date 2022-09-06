#!/usr/bin/env python3
from flask import (Flask, render_template, send_from_directory,
                   Response, json, request, session)
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
from waitress import serve
from mailer import Mail2
from random import choice, random
#from tabler import tabler

## @mainpage Talk to Kotaro: a novel open-source web-based crowdsourcing platform for human-robot interaction experiments
## Talk to Kotaro was created during the height of the COVID-19 pandemic, when
## performing Human-robot interaction (HRI) experiments in person became
## nearly impossible. Like everything else, HRI research had to go online.
## Many distinct research groups were developing their own solutions, but very
## few of these were made available for the HRI community. Thus, came the idea
## of making Talk to Kotaro open-source. It was presented at RO-MAN 2022.
## authors: Antonio Galiza Cerdeira Gonzalez; Wingsum Lo and Ikuo Mizuuchi.
## contacts: {antonio,sam,ikuo}@mizuuchi.lab.tuat.ac.jp
## version: 2.7
## 2022-09-07

## @package flaskapp Main script of Talk to Kotaro, containing the
## Flask app which serves the webpages for the browser side and executes every
## back-end function.

## Flask app instance.
## @param __name__ name of the flask app instance.
app = Flask(__name__)
## Session type for flask_session, storing the current session information as
## files in the flask_session folder in the server or in the docker container.
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)
app.logger.addHandler(logging.StreamHandler(stdout))
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

## Current location where the main script is running.
current_dir = getcwd()
## Location of the SQLite database.
dbLoc = "./memory/profile.sql"
## Location where the video of the facial expression of volunteers are stored.
videoLoc = "./memory/video/"
## Location where the audio recordings of what volunteers tell Kotaro are
## stored.
audioLoc = "./memory/audio/"


## Renders the landing page for the experiment, containing explanation about it.
@app.route('/')
def index():
	return render_template('landingPage.html')


## Renders the login page for experiment while setting all session variables as
## their default values.
@app.route('/experiment')
def jikken():
	## Volume of the last generated utterance, int between 0 and 200.
	session["volume"] = 0
	## Speed of the last generated utterance, int between 80 and 500.
	session["speed"] = 0
	## Pitch of the last generated utterance, int between 0 and 99.
	session["pitch"] = 0
	## ID of the user in the current session; str.
	session["current_id"] = None
	## Most recent frame of the video of the volunterr's facial expression;
	## np.array.
	session["global_frame"] = None
	## Contents of the most recent utterance; str.
	session["global_phrase"] = None

	#cascade_file = current_dir+'/static/haarcascade_frontalface_default.xml'
	#face_cascade = cv2.CascadeClassifier(cascade_file)
	## Buffer for the video frames waiting to be written.
	session["frame_buffer"] = []
	## List of the latest estimated impression from the facial expression video
	## frames; used only when real time estimation is enabled.
	session["emotion_timeseries"]=[]
	## Registers the time when the user started the latest part of the
	## conversation with Kotaro.
	session["timeReg"] = time.time()
	## Name of the latest audio file from a volunteer.
	session["audioFile"] = ""
	## Registers if the site is currently recording. str, f if false, t
	## otherwise.
	session["recording"] = "f"
	## Dictionary containing the x, y position coordinates, width and height of
	## the square which denotes that the face of a volunteer has been detected.
	session["posDic"] = {"x":0,"y":0,"w":0,"h":0}
	## File name of the video of the latest user facial expressions.
	session["filename"] = ""
	return render_template('frontpage.html')


## Loads the Talk to Kotaro icon on the browser side.
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(join(app.root_path, 'static'), 'favicon.ico',
	                           mimetype='image/vnd.microsoft.icon')


## Loads the login page of the experiment without resetting the session.
@app.route('/exp')
def exper():
	return render_template('index.html');


## Login function which checks if username and password are correct. Loads
## the experiment main page if correct, loads login error page otherewise.
@app.route('/main', methods = ['POST'])
def main():
	if request.method == 'POST':
		## contains ID and password information from the login page, dict.
		form_data = request.form
		## ID inserted at the login page, str.
		ID = form_data["fname"]
		## contains the password inserted at the login page, str.
		password = form_data["lname"]
	if ID == "" or ID == " " or ID is None or password == "":
		return render_template('frontpage_error.html')
	#Stores if the ID and password have been successfully validated; bool.
	passed = loginCheck(ID,password)
	if passed:
		session["current_id"] = ID
		return render_template('index.html')
	else:
		return render_template('frontpage_error.html')


##Loads the consent form and experiment explanation page.
@app.route('/consent1')
def con():
	return render_template('explanation.html')


## Loads the profile creation page.
@app.route('/consent2')
def crear():
	return render_template('ProfileMaker.html')


## Loads the page which contains the instructions for the experiment.
@app.route('/instructions')
def inst():
	return render_template('instructions.html')


## Function which handles the creation of volunteers' profiles. Returns to the
## login page if there are no errors, loads the profile creation error page
## otherwise.
@app.route('/create_profile', methods = ['POST'])
def create():
	## Contains the result of the check if the ID already exists.
	username_exists = False
	## Tentative ID inserted during profile creation.
	ID = None
	if request.method == 'POST':
		## Contains the profile information.
		form_data = request.form
		ID = form_data["fname"]
		## Tentative password inserted during profile creation.
		password = form_data["lname"]

		# Secret master code which is used to create a new correctly formated
		# SQLite database; choose your own or comment this.
		# if ID == "PUT YOUR OWN" and password == "PUT YOUR OWN":
		# 	tabler()

		for i in ID:  # checks if the ID only contains allowed characters.
			if i not in ["a","b","c","d","e","f","g","h","i","j","k","l","m",
			             "n","o","p","q","r","s","t","u","v","w","x","y","z",
						 "A","B","C","D","E","F","G","H","I","J","K","L","M",
						 "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
						 "1","2","3","4","5","6","7","8","9","0",]:
				return render_template('username_error.html')

		if ";" in password or password is None or password=="":
			return render_template('username_error.html')
	username_exists = IDexists(ID)  #checks if the tentative ID already exists.
	if not username_exists:
		createUser(ID,password)  # creates user in the SQLite database.
		## contains a list of the contents of the profile information dict.
		register = [form_data[i] for i in form_data]
		register = [register[0]]+register[2:]
		## SQLite database.
		db = sql.connect(dbLoc)
		## Cursor to write in the SQlite database.
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


## URL call which receives the latest audio file of a volunteer.
@app.route('/audio', methods=['POST'])
def audio():
	with open('./audio.wav', 'wb') as f:
		f.write(request.data)
	## process for saving the audio data.
	proc = run(['ffprobe', '-of', 'default=noprint_wrappers=1',
	           './audio.wav'], text=True, stderr=PIPE)
	return proc.stderr


## URL call for serving the audio file of Kotaro's synthesized speech to the
## browser side..
@app.route("/wav")
def Hanasu():
	open_jtalk = ['espeak']
	# Randomly selects prosody values for the gibberish speech.
	session["volume"] = str(choice(range(10,200)))
	session["speed"] = str(choice(range(80,450)))
	session["pitch"] = str(choice(range(0,99)))
	vol = ["-a", session["volume"]]
	htsvoice=['-p',session["pitch"]]
	spd = ['-s',session["speed"]]
	## contents of the generated gibberish speech.
	phrase = gibberish()
	## Command for the subprocess call of espeak; list.
	cmd = open_jtalk+htsvoice+vol+spd+["[["+phrase+"]]"]+["--stdout"]
	## Subprocess call of espeak in such a way where the output audio is
	## available as binary data.
	c = subprocess.Popen(cmd,stdout=subprocess.PIPE)
	session["global_phrase"] = phrase
	print(phrase)
	## Sends the Gibberish speech audio data packages.
	def generate():
		audio = c.stdout.read(1024)
		while audio:
				yield audio
				audio = c.stdout.read(1024)
		#yield audio
	return Response(generate(), mimetype="audio/wav")


## URL call which sends an image file from the browser side to the server. This
## function is currently only used for receiving images for requesting the
## deletion of the profile of underage volunteers.
@app.route('/send_image')
def sendImage():
	if len(session["frame_buffer"])>0:
		return Response(cv2.imencode('.jpg',
		                             session["frame_buffer"][-1])[1].tobytes(),
									 mimetype="image/jpeg")
	else:
		return Response(cv2.imencode('.jpg',
		                             np.zeros((500, 500, 3),
									 dtype = "uint8"))[1].tobytes(),
									 mimetype="image/jpeg")


## URL call which checks the current state of audio and video recording at the
## browser side. If there is a frame buffer and recording has stopped, the
## server side saves the video and audio, cryptographs them, stores the latest
## utterance information (speech contents and prosody) at the SQLite database
## and deletes original non-cryptographed files.
@app.route('/rec_status', methods=['POST'])
def record_status():
	## json request response from the browser side containing the current
	## recording status.
	json = request.get_json()
	session["recording"] = json['status']
	session["filename"] = videoLoc + ";" + str(session["current_id"]) + ";" + str(session["timeReg"]) + ".avi"
	if session["recording"][0] == "f" and len(session["frame_buffer"]) > 0:
		## Width, height and depth (1 if grayscale, 3 if RGB) of the received
		## frames of the volunteer's face expressions; int, int, int.
		width, height, depth = session["frame_buffer"][0].shape
		## OpenCV2 video writer.
		out = cv2.VideoWriter(session["filename"],
		                      cv2.VideoWriter_fourcc(*'MJPG'),
							  20.0,
							  (height,width))
		for f in session["frame_buffer"]:
			out.write(f)
		out.release()
		session["frame_buffer"] = []
		## SQlite database.
		db = sql.connect(dbLoc)
		## Cursor for acessing the SQLite database.
		cursor = db.cursor()
		cursor.execute('SELECT * FROM login WHERE ID=?',
		               (session["current_id"],))
		## Results of the cursor's query to the database.
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
			insert=(str(session["current_id"]), str(session["global_phrase"]),
			        str([session["volume"],session["speed"],session["pitch"]]),
					str(session["audioFile"]), str(session["filename"]),
					str(session["emotion_timeseries"]),)
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
		os.remove(session["filename"])
	except:
		pass

	try:
		os.remove(session["audioFile"])
	except:
		pass
	session["audioFile"] = ""
	return "1"


## Receives a single frame of the current facial expression of a volunteer,
## converts it to an np.array and, if real time face detection is enabled,
## performs haarcascade face detection and stores the size and location of
## the first face to be detected.
@app.route('/rec', methods=['POST'])
def receive():
	## frame of the current facial expression of a volunteer.
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


# MARKED FOR DELETION, THOROUGLY CHECK BEFORE DOING SO.
# @app.route('/voice')
# def voic():
# 	return render_template('audio.html')


## Saves the latest recording of the volunteer's speech with correct filename
## convention.
@app.route('/rec_voice', methods=['POST'])
def r():
	session["timeReg"] = time.time()
	koe = request.files["audio_data"]
	if koe:
		session["audioFile"]= audioLoc + ";" + str(session["current_id"]) + ";" + str(session["timeReg"]) + ".wav"
		koe.save(session["audioFile"])
	return "1"


# MARKED FOR DELETION, THOROUGLY CHECK BEFORE DOING SO.
# @app.route('/return')
# def ret():
# 	return render_template('index.html')


## Renders the optional Likert Scale questionnaire page.
@app.route('/likert')
def like():
	return render_template('likert.html')


## Receives and stores the answers of the Likert Scale questionnaire at the
## SQLite database and sends the volunteer back to the login page.
@app.route('/likert_answer', methods = ['POST'])
def answer():

	if request.method == 'POST':
		## Data of the likert scale questionnaire response; dict.
		form_data = request.form
		## stores the current ID in a list.
		line = [session["current_id"]]
		for i in range(1,11):  # accesses every prompt's response.
			try:
				## value of the response of a single Likert prompt; int between
				## 1 and 5.
				value = form_data["likert"+str(i)]
			except:
				return render_template('likert_error.html')
			if value == "":
				return render_template('likert_error.html')
			line += [value]
		## SQLite database.
		db = sql.connect(dbLoc)
		## Cursor for accessing the database.
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


## Sends users who want to delete the data they have contibuted so far to the
## deletion request web page.
@app.route('/want')
def want():
		return render_template('delete.html')


## Sends the responsible guardian of a minor to the minor's profile and data
## deletion request webpage.
@app.route('/del_minors_profile')
def dmp():
		return render_template('DelRequest.html')


## Sends an email requesting the deletion of a minor's profile containing its
## ID and picture for identification purposes.
@app.route('/submitRequest', methods = ['POST'])
def sR():
	if request.method == 'POST':
		## Contains the form data for the deletion request email; dict.
		form_data = request.form
		Mail2(form_data["fID"], request.files["fFile"], form_data["exp"],
		      form_data["fMail"])
	return render_template("SucReq.html")


# MARKED FOR DELETION, CHECK CAREFULLY BEFORE DOING SO.
# @app.route('/info')
# def inf():
# 	return render_template("instructions.html")


## URL call which handles the deletion of a volunteer's profile and all data
## related to it.
@app.route('/deletion')
def dele():
	## SQLite database.
	db = sql.connect(dbLoc)
	## Cursor for accessing the SQLite database.
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
		if ";" + session["current_id"] + ";" in str(f):
			try:
				os.remove(videoLoc + str(f))
			except:
				pass
	for f in os.listdir(audioLoc):
		if ";" + session["current_id"] + ";" in str(f):
			try:
				os.remove(audioLoc + str(f))
			except:
				pass
	return render_template('deleted.html')


if __name__ == '__main__':
	serve(app, host="0.0.0.0", port=5000, threads=15)
