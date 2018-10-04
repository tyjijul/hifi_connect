#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, session,send_file, render_template,redirect, url_for, request, jsonify, Markup, flash , Response
from lib_FX_AUDIO import LibVolume, LibSpotifyConnect

lvolume = LibVolume()
lconnect = LibSpotifyConnect()
# from flask_restful import Resource, Api

app = Flask(__name__)
# api = Api(app)

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')

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

@app.route('/connect_get_status', methods = ['GET', 'POST'])
def connect_get_status():
	print('connect_get_status')
	status = lconnect.get_status()
	return jsonify(T1=status)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
