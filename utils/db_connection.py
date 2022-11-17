from db.lib import Session


class DbConnection(object):
    def __enter__(self):
        self.conn = Session()
        return self.conn

    def __exit__(self, *args):
        self.conn.close()