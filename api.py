from flask import Flask, request, render_template, redirect
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import sqlite3

app = Flask(__name__)
api = Api(app)
conn = sqlite3.connect('ip.db')
conn2 = sqlite3.connect('cert.db')

@app.route('/ipb', methods=['GET'])
def get():
    c = conn.cursor()
    c.execute("SELECT id, ip FROM blacklistip")
    rows = c.fetchall()
    print(rows[1][1])
    return render_template('showIPb.html', rows=rows)

@app.route('/ipb/add', methods=['POST'])
def postIPb():
    ipb = request.form['ip']
    c = conn.cursor()
    c.execute("INSERT INTO blacklistip(ip) VALUES('" +ipb+"')", )
    conn.commit()
    return redirect("/ipb", code=302)

@app.route('/ipb/delete/<ip>', methods=['GET'])
def deleteIP(ip):
    c = conn.cursor()
    c.execute("DELETE FROM blacklistip WHERE (ip = '" +ip+ "')")
    conn.commit()
    return redirect("/ipb", code=302)

@app.route('/ipw', methods=['GET'])
def getIPWhitelist():
    c = conn.cursor()
    c.execute("SELECT ip FROM whitelistip")
    rows = c.fetchall()
    print(rows)
    return render_template('showIPw.html', rows=rows)

@app.route('/ipw/add', methods=['POST'])
def postIPWhitelist():
    ipb = request.form['ip']
    c = conn.cursor()
    c.execute("INSERT INTO whitelistip(ip) VALUES('"+ipb+"')", )
    conn.commit()
    return redirect("/ipw", code=302)

@app.route('/ipw/delete/<ip>', methods=['GET'])
def deleteIPWhiteliste(ip):
    c = conn.cursor()
    c.execute("DELETE FROM whitelistip WHERE (ip = '"+ip+"')")
    conn.commit()
    return redirect("/ipw", code=302)


@app.route('/showlog', methods=['GET'])
def getLog():
    log = open("test.txt", "r")
    text = log.read()
    print log.read()
    return render_template('log.txt', text=text)





@app.route('/certificate', methods=['GET'])
def getCert():
    c = conn2.cursor()
    c.execute("SELECT id, ca FROM certificate")
    rows = c.fetchall()
    return render_template('showCert.html', rows=rows)

@app.route('/cert/add', methods=['POST'])
def postCert():
    ca = request.form['ca']
    c = conn2.cursor()
    c.execute("INSERT INTO certificate(ca) VALUES('" +ca+"')", )
    conn.commit()
    return redirect("/certificate", code=302)

@app.route('/cert/delete/<ca>', methods=['GET'])
def deleteCert(ca):
    c = conn2.cursor()
    c.execute("DELETE FROM certificate WHERE (ca = '"+ca+"')")
    conn.commit()
    return redirect("/certificate", code=302)





@app.route('/keys', methods=['GET'])
def getKeys():
    c = conn2.cursor()
    c.execute("SELECT id, key FROM keys")
    rows = c.fetchall()
    return render_template('showKeys.html', rows=rows)

@app.route('/keys/add', methods=['POST'])
def postKeys():
    ca = request.form['ca']
    c = conn2.cursor()
    c.execute("INSERT INTO keys(key) VALUES('" +ca+"')", )
    conn.commit()
    return redirect("/keys", code=302)

@app.route('/keys/delete/<key>', methods=['GET'])
def deleteKeys(key):
    c = conn2.cursor()
    c.execute("DELETE FROM keys WHERE (key = '"+key+"')")
    conn.commit()
    return redirect("/keys", code=302)
app.run()
