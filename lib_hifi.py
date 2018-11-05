#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, subprocess, commands
import threading
import time

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

############################################################################
class LibSpotifyConnect(): 
    def get_status(self):
        output = commands.getoutput('systemctl status raspotify')
        return output

    def restart(self):
        output = commands.getoutput('systemctl restart raspotify')
        return "ok"



############################################################################
class LibTimer(threading.Thread):
 
    def __init__(self):
        threading.Thread.__init__(self)
        self.t = 0
 
    def run(self):
        global app
        t1 = int(time.time())
        while self.encore:
            t2 = int(time.time())
            if t2>t1:
                self.t -= t2-t1
                if self.t <= 0:
                    self.t = 0
                    self.encore = False
                t1 = t2
            time.sleep(0.01)
        self.timer_end()

    def set_time(self, h, m, s):
        self.t = h*3600 + m*60 + s
        print(self.t)
        self.encore = True

    def get_time(self):
        # print(t)
        print(self.t)
        return self.sec2hms(self.t)

    def stop(self):
        self.encore = False
        print("TIMER STOP")

    def timer_end(self):
        print("DO ACTION")


    def sec2hms(self,sd):
        """Transforme les secondes sd en chaine "hh:mm:ss" pour affichage"""
        h=0
        m=0
        s=sd
        if s >= 60:
            m = s//60
            s -= m*60
            if m >= 60:
                h = m//60
                m -= h*60
        return "%02d:%02d:%02d" % (h, m, s)


if __name__ == '__main__':
	lfx = LibVolume()
	lfx.volume_up()
	print(lfx.volume_get())
