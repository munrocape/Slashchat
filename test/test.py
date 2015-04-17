# -*- coding: UTF-8 -*-
import logging
from mock_handler import MockHandler
import os
import sqlite3
import tempfile
from nose.tools import eq_

import Slashchat

# TODO: kill logging output into stderr.
# TODO: test logging to STDERR

# test plugin hooks
#
# TODO: test init_plugins with unicode plugins
# TODO: test init_plugins with invalid plugins
# TODO: test init_plugins with plugin without on_
# TODO: test init_plugins __doc__ handling
# TODO: test plugin that throws exception (on import, init and message)
# TODO: test command line interface

DIR = os.path.dirname(os.path.realpath(__file__))
PARENT = os.path.split(DIR)[0]

os.environ["SLASHCHAT_LOGFILE"] = "/tmp/deleteme"

def test_plugin_success():
    hooks = Slashchat.init_plugins("test/plugins")
    eq_(len(hooks), 2)
    assert "message" in hooks
    assert isinstance(hooks, dict)
    assert isinstance(hooks["message"], list)
    eq_(len(hooks["message"]), 2)

def test_plugin_invalid_dir():
    try:
        Slashchat.init_plugins("invalid/package")
    except Slashchat.InvalidPluginDir:
        return
    1 / 0

def test_plugin_logs():
    mhdr = MockHandler()
    logging.getLogger("Slashchat.Slashchat").addHandler(mhdr)
    Slashchat.init_plugins("test/plugins")
    mhdr.check("debug", "attaching message hook for echo")

# test run_hook

def test_run_hook():
    hooks = Slashchat.init_plugins("test/plugins")
    eq_(Slashchat.run_hook(hooks, "message", {"text": u"!echo bananas"}, None), [u"!echo bananas"])

def test_missing_hook():
    hooks = Slashchat.init_plugins("test/plugins")
    eq_(Slashchat.run_hook(hooks, "nonexistant", {"text": u"!echo bananas"}, None), [])

# test handle_message

def test_handle_message_subtype():
    server = Slashchat.FakeServer()
    eq_(Slashchat.handle_message({"subtype": "bot_message"}, server), None)
    eq_(Slashchat.handle_message({"subtype": "message_changed"}, server), None)

def test_handle_message_ignores_self():
    server = Slashchat.FakeServer()
    event = {"user": "Slashchat_test"}
    eq_(Slashchat.handle_message(event, server), None)

def test_handle_message_ignores_slackbot():
    server = Slashchat.FakeServer()
    event = {"user": "slackbot"}
    eq_(Slashchat.handle_message(event, server), None)

def test_handle_message_basic():
    msg = u"!echo Iñtërnâtiônàlizætiøn"
    event = {"user": "msguser", "text": msg}

    hooks = Slashchat.init_plugins("test/plugins")
    server = Slashchat.FakeServer(hooks=hooks)

    eq_(Slashchat.handle_message(event, server), msg)

def test_init_db():
    tf = tempfile.NamedTemporaryFile()
    db = Slashchat.init_db(tf.name)
    eq_(type(db), type(sqlite3.connect(":memory:")))

class FakeSlackClient(object):
    def __init__(self, connect=True):
        self.connect = connect

    def rtm_connect(self):
        return self.connect
