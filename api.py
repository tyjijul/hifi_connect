#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, session,send_file, render_template,redirect, url_for, request, jsonify, Markup, flash , Response
from lib_hifi import LibVolume, LibSpotifyConnect, LibTimer




lvolume = LibVolume()
lconnect = LibSpotifyConnect() 


app = Flask(__name__) 


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/temperature')
def temperature():
	return render_template('temperature.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')


#####  VOLUME  #############################################
@app.route('/volume_up', methods = ['GET', 'POST'])
def volume_up():
	print('volume up')
	lvolume.volume_up()
	volume = lvolume.volume_get()
	return jsonify(T1=str(volume)+"%")

@app.route('/volume_down', methods = ['GET', 'POST'])
def volume_down():
	print('volume down')
	lvolume.volume_down()
	volume = lvolume.volume_get()
	return jsonify(T1=str(volume)+"%")

@app.route('/volume_get', methods = ['GET', 'POST'])
def volume_get():
	print('volume get')
	volume = lvolume.volume_get()
	return jsonify(T1=str(volume)+"%")

#####  CONNECT  #############################################
@app.route('/connect_get_status', methods = ['GET', 'POST'])
def connect_get_status():
	print('connect_get_status')
	status = lconnect.get_status()
	return jsonify(T1=status)

@app.route('/connect_restart', methods = ['GET', 'POST'])
def connect_restart():
	print('connect_restart')
	status = lconnect.restart()
	return jsonify(T1=status)

#####  TIMER  #############################################
@app.route('/timer_start/<h>/<m>/', methods = ['GET', 'POST'])
def timer_start(h,m):
	print('timer_start')
	global chrono
	chrono = LibTimer()
	chrono.set_time(0,int(h),int(m))
	chrono.start()
	return jsonify(T1="ok")

@app.route('/timer_get', methods = ['GET', 'POST'])
def timer_get():
	print('timer_get')
	time = chrono.get_time()
	return jsonify(T1=time)

@app.route('/timer_stop', methods = ['GET', 'POST'])
def timer_stop():
	print('timer_stop')
	chrono.stop()
	return jsonify(T1="ok")

####  DATA TEMPERATURE  ###################################
@app.route('/graph', methods = ['GET', 'POST'])
def graph():
	print('graph_get')
	data = [["2h","3h","4h","5h","6h","7h","8h","9h"],[10,10,11,12,13,14,15,14],[2,3,4,6,5,3,2,1],[19,13,12,15,16,19,22,23]]
	return jsonify(T1=data)







if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
