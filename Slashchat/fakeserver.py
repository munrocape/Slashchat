class FakeServer(object):
    def __init__(self, slack=None, config=None, hooks=None, db=None):
        self.slack = slack or FakeSlack()
        self.config = config
        self.hooks = hooks
        self.db = db

    def query(self, sql, *params):
        # XXX: what to do with this?
        return None

class FakeSlack(object):
    def __init__(self, server=None):
        self.server = server or FakeSlackServer()

class FakeSlackServer(object):
    def __init__(self, botname="Slashchat_test"):
        self.login_data = {
            "self": {
                "name": botname,
            }
        }

        self.users = {
            "Slashchat_test": {"name": "Slashchat_test"},
            "msguser": {"name": "msguser"},
            "slackbot": {"name": "slackbot"},
        }
