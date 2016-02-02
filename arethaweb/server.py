import os
import socketio
import eventlet

import backendtasks
from celeryapp import app as celery_app
celery_app.set_current()


from flask import Flask, render_template
app = Flask('aretha-web')
app.debug = True

sio = socketio.Server()

@app.route('/')
def home():
  return render_template('base.html')

@sio.on('connect')
def connect(sid, environ):
    print "connected with sid: {}".format(sid)

@sio.on('luke')
def connect(sid, data):
    print "got event with sid: {} and data: {}".format(sid,data)
    sio.emit('luke','there {}'.format(sid), room = sid)

@sio.on('go')
def connect(sid, data):
    print "got go! event with sid: {} and data: {}".format(sid,data)
    result = backendtasks.submit_swarm.delay(config = 'what')
    sio.emit('luke',{'msg':'gone','id':result.id}, room = sid)

@sio.on('disconnect')
def disconnect(sid):
    print "disconnected from sid: {}".format(sid)


if __name__ == '__main__':
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)