from ..db.lib import engine


class DbConnection(object):
    def __enter__(self):
        self.conn = engine.connect()
        return self.conn()

    def __exit__(self):
        self.conn.close()