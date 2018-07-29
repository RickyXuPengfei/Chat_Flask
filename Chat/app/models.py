from datetime import datetime
from app import db

class UserAccounts(db.Model):
    __tablename__ = 'UserAccounts'

    Id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(64), unique=True)
    Password = db.Column(db.String(64))
    MugShot = db.Column(db.String(64))
    Key = db.Column(db.String(50))
    CreateDate = db.Column(db.DateTime)
    ModifiedDate = db.Column(db.DateTime)

    def __init__(self,
                 user_name,
                 password,
                 mugshot,
                 key,
                 create_date=datetime.now(),
                 modified_date=datetime.now()):
        self.UserName = user_name
        self.Password = self.psw_to_md5(password)
        self.MugShot = mugshot
        self.Key = key
        self.CreateDate = create_date
        self.ModifiedDate = modified_date

    @staticmethod
    def psw_to_md5(str_psw):
        import hashlib
        if not str_psw:
            return None
        else:
            m = hashlib.md5(str_psw.encode(encoding='utf-8'))
            return m.hexdigest()

    def __repr__(self):
        return "<User {0}>".format(self.UserName)


class Message(db.Model):
    __tablename__ = 'Message'

    Id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(64))
    Messages = db.Column(db.LargeBinary)
    CreateDate = db.Column(db.DateTime)

    def __init__(self,
                 user_name,
                 messages,
                 create_date):
        self.UserName = user_name
        self.Messages = messages
        self.CreateDate = create_date

    def __repr__(self):
        return "<Message {0}>".format(self.Messages)

# if __name__ == '__main__':
#     db.create_all()
