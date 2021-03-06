class Records(db.model):
    __tablename__ = 'fb_records'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    sid = db.Column(db.String(32),nullable = False)
    stime = db.Column(db.Datetime,nullable = False)
    intro = db.Column(db.Text,nullable = True)
    itime = db.Column(db.Datetime,nullable = True)
    mood = db.Column(db.String(16), nullable=False)
    mtime = db.Column(db.Datetime, nullable=True)
    c1 = db.Column(db.String(16), nullable=False)
    c1t = db.Column(db.Datetime, nullable=False)
    c2 = db.Column(db.String(16), nullable=False)
    c2t = db.Column(db.Datetime, nullable=False)
    c3 = db.Column(db.String(16), nullable=False)
    c3t = db.Column(db.Datetime, nullable=False)
    c4 = db.Column(db.String(16), nullable=False)
    c4t = db.Column(db.Datetime, nullable=False)
    c5 = db.Column(db.String(16), nullable=False)
    c5t = db.Column(db.Datetime, nullable=False)
    c6 = db.Column(db.String(16), nullable=False)
    c6t = db.Column(db.Datetime, nullable=False)
    c7 = db.Column(db.String(16), nullable=False)
    c7t = db.Column(db.Datetime, nullable=False)
    c8 = db.Column(db.String(16), nullable=False)
    c8t = db.Column(db.Datetime, nullable=False)
    c9 = db.Column(db.String(16), nullable=False)
    c9t = db.Column(db.Datetime, nullable=False)
    c10 = db.Column(db.String(16), nullable=False)
    c10t = db.Column(db.Datetime, nullable=False)
    c11 = db.Column(db.String(16), nullable=False)
    c11t = db.Column(db.Datetime, nullable=False)
    c12 = db.Column(db.String(16), nullable=False)
    c12t = db.Column(db.Datetime, nullable=False)
    c13 = db.Column(db.String(16), nullable=False)
    c13t = db.Column(db.Datetime, nullable=False)
    c14 = db.Column(db.String(16), nullable=False)
    c14t = db.Column(db.Datetime, nullable=False)
    c15 = db.Column(db.String(16), nullable=False)
    c15t = db.Column(db.Datetime, nullable=False)
    c16 = db.Column(db.String(16), nullable=False)
    c16t = db.Column(db.Datetime, nullable=False)
    c17 = db.Column(db.String(16), nullable=False)
    c17t = db.Column(db.Datetime, nullable=False)
    c18 = db.Column(db.String(16), nullable=False)
    c18t = db.Column(db.Datetime, nullable=False)
    c19 = db.Column(db.String(16), nullable=False)
    c19t = db.Column(db.Datetime, nullable=False)
    c20 = db.Column(db.String(16), nullable=False)
    c20t = db.Column(db.Datetime, nullable=False)
    o1 = db.Column(db.Text, nullable=False)
    o1t = db.Column(db.Datetime, nullable=False)
    o2 = db.Column(db.Text, nullable=False)
    o2t = db.Column(db.Datetime, nullable=False)
    o3 = db.Column(db.Text, nullable=False)
    o3t = db.Column(db.Datetime, nullable=False)
    o4 = db.Column(db.Text, nullable=False)
    o4t = db.Column(db.Datetime, nullable=False)
    o5 = db.Column(db.Text, nullable=False)
    o5t = db.Column(db.Datetime, nullable=False)
    o6 = db.Column(db.Text, nullable=False)
    o6t = db.Column(db.Datetime, nullable=False)
    o7 = db.Column(db.Text, nullable=False)
    o7t = db.Column(db.Datetime, nullable=False)
    o8 = db.Column(db.Text, nullable=False)
    o8t = db.Column(db.Datetime, nullable=False)
    age = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.String(8), nullable=False)
    personality = db.Column(db.Text, nullable=False)
    etime = db.Column(db.Datetime, nullable=False)
    sqans = db.Column(db.String(64), nullable=False)
    sqtime = db.Column(db.Datetime, nullable=False)
    soq1 = db.Column(db.Text, nullable=False)
    soq2 = db.Column(db.Text, nullable=False)
    soq3 = db.Column(db.Text, nullable=False)
    soqtime = db.Column(db.Datetime, nullable=False)
    step = db.Column(db.Integer, nullable=False)


class Botlog(db.model):
    __tablename__ = 'fb_botlog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chat = db.Column(db.Text)
    userid = db.Column(db.String(64))
    qid = db.Column(db.Integer)
    qc = db.Column(db.Text)
    etime = db.Column(db.Datetime)


class Coupon(db.model):
    __tablename__ = 'fb_coupon'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uuid = db.Column(db.String(32))
    ctime = db.Column(db.Datetime)
    used = db.Column(db.Integer)
    uid = db.Column(db.String(64))
