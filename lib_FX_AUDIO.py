#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, subprocess, commands

pas_volume = 2
VMAX = 96

class LibVolume() : 
	def volume_set(self,percent):
		os.system('amixer set PCM -- '+str(percent)+'%')

	def volume_get(self):
		output = commands.getoutput('amixer get PCM')
		tabs = output.split("[")
		i = 0
		index = 0
		for line in tabs :
			if line.find('%') != -1:
				print(line)
				index = i 
			i += 1
		volume = int(tabs[index].split('%')[0])
		return volume

	def volume_up(self):
		volume = self.volume_get()
		volume = volume + pas_volume  if volume < VMAX else VMAX
		self.volume_set(volume)

	def volume_down(self):
		volume = self.volume_get()
		volume = volume - pas_volume  if volume >= 0 else 0
		self.volume_set(volume)

class LibSpotifyConnect(): 
	def get_status(self):
		output = commands.getoutput('systemctl status raspotify')
		return output


if __name__ == '__main__':
	lfx = LibVolume()
	lfx.volume_up()
	print(lfx.volume_get())
