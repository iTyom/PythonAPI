from flask import Flask, request, render_template, redirect
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import sqlite3

app = Flask(__name__)
api = Api(app)
conn = sqlite3.connect('ip_blacklist.db')

@app.route('/ipb', methods=['GET'])
def get():
    c = conn.cursor()
    c.execute("SELECT id, ip FROM ip_blacklist")
    rows = c.fetchall()
    print(rows[1][1])
    return render_template('showIPb.html', rows=rows)

@app.route('/ipb/add', methods=['POST'])
def postIPb():
    ipb = request.form['ip']
    c = conn.cursor()
    c.execute("INSERT INTO ip_blacklist(ip) VALUES('" +ipb+"')", )
    conn.commit()
    return redirect("/ipb", code=302)

@app.route('/ipb/delete/<ip>', methods=['GET'])
def deleteIP(ip):
    c = conn.cursor()
    c.execute("DELETE FROM ip_blacklist WHERE (ip = '" +ip+ "')")
    conn.commit()
    return redirect("/ipb", code=302)

@app.route('/ipw', methods=['GET'])
def getIPWhitelist():
    c = conn.cursor()
    c.execute("SELECT ip FROM ip_whitelist")
    rows = c.fetchall()
    return render_template('showIPw.html', rows=rows)

@app.route('/ipw/<ip>', methods=['GET'])
def postIPWhitelist(ip):
    c = conn.cursor()
    c.execute("INSERT INTO ip_whitelist(ip) VALUES('" +ip+"')", )
    conn.commit()
    return "done"

@app.route('/ipw/delete/<ip>', methods=['GET'])
def deleteIPWhiteliste(ip):
    c = conn.cursor()
    c.execute("DELETE FROM ip_whitelist WHERE (ip = '" +ip+ "')")
    conn.commit()
    return "done"


@app.route('/showlog', methods=['GET'])
def getLog():
    log = open("test.txt", "r")
    text = log.read()
    print log.read()
    return render_template('showLog.html', text=text)



app.run()
