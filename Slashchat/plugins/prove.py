"""!prove <LHS> <GOAL> will try to return proof for <LHS> = <GOAL>"""
from bs4 import BeautifulSoup
from re import findall
import urllib
import requests
import HTMLParser

h = HTMLParser.HTMLParser()

def prove(inp, goal="True"):
    query = urllib.quote(h.unescape(inp))
    goal = urllib.quote(h.unescape(goal))
	
    url = "http://www.proofmeister.com/results/?start={0}&goal={1}".format(query, goal)
    soup = BeautifulSoup(requests.get(url.decode('utf-8')).text)

    table = soup.select('table')

    if not table:
      return ":crying_cat_face: Sorry, we can not give you a proof!"

    table = table[0]
    data = []

    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    return '\n'.join(['\t'.join(col)
        .replace('&Wedge;', '&')
        .replace('&Vee;', 'v')
         for col in data])

def on_message(msg, server):
    text = msg.get("text", "")
    match = findall(r"!prove (.*) (.*)?", text)  # TODO: specify syntax for proofs 
    if not match:
        return ''
    # print(unquote(match[0][0].encode("utf8")),
    #     unquote(match[0][1].encode("utf8")))
    return prove(urllib.unquote(match[0][0].encode("utf8")),
        urllib.unquote(match[0][1].encode("utf8")))
