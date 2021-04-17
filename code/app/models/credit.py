from db import db

class CreditModel(db.Model):
    __tablename__ = 'credit'

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(6))
    job = db.Column(db.Integer)
    housing = db.Column(db.String(4))
    saving_accounts = db.Column(db.String(20))
    checking_account = db.Column(db.String(20))
    credit_amount = db.Column(db.Integer)
    duration = db.Column(db.Integer())
    purpose = db.Column(db.String(20))
    risk = db.Column(db.String(20))

    def __init__(self, age, sex, job, housing, saving_accounts, checking_account, credit_amount, duration, purpose, risk):
        self.age = age
        self.sex = sex
        self.job = job
        self.housing = housing
        self.saving_accounts = saving_accounts
        self.checking_account = checking_account
        self.credit_amount = credit_amount
        self.duration = duration
        self.purpose = purpose
        self.risk = risk

    def json(self):
        return {
            'id': self.id,
            'age': self.age,
            'sex': self.sex,
            'job': self.job,
            'housing': self.housing,
            'saving_accounts': self.saving_accounts,
            'checking_account': self.checking_account,
            'credit_amount': self.credit_amount,
            'duration': self.duration,
            'purpose': self.purpose,
            'risk': self.risk
        }

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first() #posso colocar varios filter_by 

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()