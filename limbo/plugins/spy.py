"""!spy <url> checks url every hour for a more than 10% difference-- EXPERIMENTAL STILL"""
from difflib import SequenceMatcher
from zlib import compress
from bs4 import BeautifulSoup
import re
import requests
import sched
import time
import threading

scheduler = sched.scheduler(time.time, time.sleep)

def spy(url, copy="", c_level=9):
	if(copy == ""):
		bs = BeautifulSoup(requests.get(url).text)
		return spy(url, compress(bs.encode(), c_level))
	return check_match(url, copy, c_level)


def check_match(url, initial, c_level=9):
	bs = BeautifulSoup(requests.get(url).text)
	s = SequenceMatcher(lambda x: x == " ", initial,
			compress(bs.encode(), c_level))
	if(s.real_quick_ratio() > 0.90):
		scheduler.enter(3600, 10, check_match, [url, initial, c_level])
		t = threading.Thread(target=scheduler.run)
		t.start()
	else:
		return 'Threshold exceeded for ' + url + ' spy: ' + ' update detected'
	return 'Threshold not exceeded for ' + url + ' spy: ' + ' update not detected yet'

def on_message(msg, server):
    text = msg.get("text", "")
    if not '|' in text:
    	return
    site = text.split('|')[0]
    return spy(site[site.find('<')+1:])