from flask import Flask, jsonify, request, render_template, session, url_for, redirect
import math
import time
import os
import hashlib
# from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from nltk.tokenize import sent_tokenize
import nltk
from pymysql.converters import escape_string
import random
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

# nltk.download('punkt')

'''
=================== Config ======================
'''
app = Flask(__name__)
# app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/formbot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# session 的密钥，过期时间7天
app.config['SECRET_KEY'] = '1123581321'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
# CORS(app)
# 创建数据库连接
db = SQLAlchemy(app)
# tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
# model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")

'''
===================  DATABASE =====================
'''


class Records(db.Model):
    __tablename__ = 'fb_records'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sid = db.Column(db.String(32), nullable=False)
    device = db.Column(db.String(256), nullable=False)
    atime = db.Column(db.DateTime, nullable=False)
    category = db.Column(db.Integer, nullable=True)
    stime = db.Column(db.DateTime, nullable=False)
    intro = db.Column(db.Text, nullable=True)
    itime = db.Column(db.DateTime, nullable=True)
    mood = db.Column(db.String(16), nullable=True)
    mtime = db.Column(db.DateTime, nullable=True)
    ltime = db.Column(db.DateTime, nullable=True)
    c1 = db.Column(db.String(16), nullable=True)
    c1t = db.Column(db.DateTime, nullable=True)
    c2 = db.Column(db.String(16), nullable=True)
    c2t = db.Column(db.DateTime, nullable=True)
    c3 = db.Column(db.String(16), nullable=True)
    c3t = db.Column(db.DateTime, nullable=True)
    c4 = db.Column(db.String(16), nullable=True)
    c4t = db.Column(db.DateTime, nullable=True)
    c5 = db.Column(db.String(16), nullable=True)
    c5t = db.Column(db.DateTime, nullable=True)
    c6 = db.Column(db.String(16), nullable=True)
    c6t = db.Column(db.DateTime, nullable=True)
    c7 = db.Column(db.String(16), nullable=True)
    c7t = db.Column(db.DateTime, nullable=True)
    c8 = db.Column(db.String(16), nullable=True)
    c8t = db.Column(db.DateTime, nullable=True)
    c9 = db.Column(db.String(16), nullable=True)
    c9t = db.Column(db.DateTime, nullable=True)
    c10 = db.Column(db.String(16), nullable=True)
    c10t = db.Column(db.DateTime, nullable=True)
    c11 = db.Column(db.String(16), nullable=True)
    c11t = db.Column(db.DateTime, nullable=True)
    c12 = db.Column(db.String(16), nullable=True)
    c12t = db.Column(db.DateTime, nullable=True)
    c13 = db.Column(db.String(16), nullable=True)
    c13t = db.Column(db.DateTime, nullable=True)
    c14 = db.Column(db.String(16), nullable=True)
    c14t = db.Column(db.DateTime, nullable=True)
    c15 = db.Column(db.String(16), nullable=True)
    c15t = db.Column(db.DateTime, nullable=True)
    c16 = db.Column(db.String(16), nullable=True)
    c16t = db.Column(db.DateTime, nullable=True)
    c17 = db.Column(db.String(16), nullable=True)
    c17t = db.Column(db.DateTime, nullable=True)
    c18 = db.Column(db.String(16), nullable=True)
    c18t = db.Column(db.DateTime, nullable=True)
    c19 = db.Column(db.String(16), nullable=True)
    c19t = db.Column(db.DateTime, nullable=True)
    c20 = db.Column(db.String(16), nullable=True)
    c20t = db.Column(db.DateTime, nullable=True)
    rbtime = db.Column(db.DateTime, nullable=True)
    cscore = db.Column(db.Integer, nullable=True)
    ratime = db.Column(db.DateTime, nullable=True)
    otime = db.Column(db.DateTime, nullable=True)
    o1 = db.Column(db.Text, nullable=True)
    o1t = db.Column(db.DateTime, nullable=True)
    o2 = db.Column(db.Text, nullable=True)
    o2t = db.Column(db.DateTime, nullable=True)
    o3 = db.Column(db.Text, nullable=True)
    o3t = db.Column(db.DateTime, nullable=True)
    o4 = db.Column(db.Text, nullable=True)
    o4t = db.Column(db.DateTime, nullable=True)
    o5 = db.Column(db.Text, nullable=True)
    o5t = db.Column(db.DateTime, nullable=True)
    o6 = db.Column(db.Text, nullable=True)
    o6t = db.Column(db.DateTime, nullable=True)
    o7 = db.Column(db.Text, nullable=True)
    o7t = db.Column(db.DateTime, nullable=True)
    moodn = db.Column(db.String(16), nullable=True)
    mntime = db.Column(db.DateTime, nullable=True)
    ftime = db.Column(db.DateTime, nullable=True)
    age = db.Column(db.String(64), nullable=True)
    gender = db.Column(db.String(8), nullable=True)
    loc = db.Column(db.String(64), nullable=True)
    edu = db.Column(db.String(64), nullable=True)
    faculty = db.Column(db.String(64), nullable=True)
    mental = db.Column(db.String(64), nullable=True)
    personality = db.Column(db.Text, nullable=True)
    etime = db.Column(db.DateTime, nullable=True)
    sqans = db.Column(db.String(64), nullable=True)
    sqp1ans = db.Column(db.String(64), nullable=True)
    sqtime = db.Column(db.DateTime, nullable=True)
    soq1 = db.Column(db.Text, nullable=True)
    soq2 = db.Column(db.Text, nullable=True)
    soq3 = db.Column(db.Text, nullable=True)
    soq4 = db.Column(db.Text, nullable=True)
    soq5 = db.Column(db.Text, nullable=True)
    soqtime = db.Column(db.DateTime, nullable=True)
    step = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(128), nullable=True)
    f2f = db.Column(db.Integer, nullable=False)
    draw = db.Column(db.Integer, nullable=False)


class Botlog(db.Model):
    __tablename__ = 'fb_botlog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chat = db.Column(db.Text)
    userid = db.Column(db.String(64))
    qid = db.Column(db.Integer)
    qc = db.Column(db.Text)
    etime = db.Column(db.DateTime)
    gtime = db.Column(db.Float)


class Coupon(db.Model):
    __tablename__ = 'fb_coupon'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uuid = db.Column(db.String(32))
    ctime = db.Column(db.DateTime, nullable=False)
    used = db.Column(db.Integer)
    uid = db.Column(db.String(64), nullable=False)


# database end

'''
====================APP STSRT =======================
'''


@app.route('/')
def index1():
    return render_template("index.html")


@app.route('/index')
def index2():
    return render_template("index.html")


@app.route('/chatbot/<id>')
def index3(id):
    if session.get('sid') and session.get('step') == 2:
        return render_template("index.html")
    else:
        return redirect(url_for('index2'))


@app.route('/interview')
def index4():
    if session.get('sid') and session.get('step') == 3:
        return render_template("index.html")
    else:
        return redirect(url_for('index2'))


@app.route('/about')
def index5():
    if session.get('sid') and session.get('step') == 4:
        return render_template("index.html")
    else:
        return redirect(url_for('index2'))


@app.route('/info')
def index6():
    if session.get('sid') and session.get('step') == 1:
        return render_template("index.html")
    else:
        return redirect(url_for('index2'))


@app.route('/add', methods=['POST'])
def add():
    """
    新建一条记录，在首页点击
    :return:
    """
    if session.get('sid') and session.get('uuid') is True:
        return jsonify({'status': 2})
    elif session.get('sid') and session.get('id'):
        session['step'] = 1
        return jsonify({'id': session.get('id'), 'sid': session.get('sid'), 'status': 1})
    else:
        data = request.get_json(silent=True)
        atime = time.localtime(data['atime'] / 1000)
        stime = time.strftime('%Y-%m-%d %H:%M:%S')
        m = hashlib.md5(stime.encode(encoding='utf8'))
        sid = m.hexdigest()
        record = Records(sid=sid, stime=stime, atime=atime, step=0, device=data['device'])
        db.session.add(record)
        db.session.flush()
        id = record.id
        db.session.commit()
        # 设置一个session存储用户的加密信息
        session['id'] = record.id
        session['sid'] = sid
        session['step'] = 1
        session['uuid'] = False
        # print(session)
        return jsonify({'id': id, 'sid': sid, 'status': 1})


@app.route('/self', methods=['POST'])
def self():
    """
    自我介绍
    :return:
    """
    data = request.get_json(silent=True)
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    # print(record.sid,record.id)
    record.intro = data['intro']
    record.category = data['category']
    record.itime = time.localtime(data['itime'] / 1000)
    db.session.commit()
    return jsonify({'status': 'success'})


@app.route('/mood', methods=['GET', 'POST'])
def mood():
    """
    心情选择
    :return:
    """
    data = request.get_json(silent=True)
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    record.mood = data['mood']
    record.mtime = time.localtime(data['mtime'] / 1000)
    db.session.commit()
    return jsonify({'status': 'success'})


@app.route('/ucla', methods=['GET', 'POST'])
def ucla():
    """
    ucla测试单条更新
    :return:
    """
    data = request.get_json(silent=True)
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    setattr(record, data['citem'], data['content'])
    setattr(record, (data['citem'] + 't'), time.localtime(data['ctime'] / 1000))
    db.session.commit()
    return jsonify({'status': 'success'})


@app.route('/uclaf', methods=['GET', 'POST'])
def uclaf():
    """
    ucla测试表单更新
    :return:
    """
    data = request.get_json(silent=True)
    cq = []
    for item in data['content']:
        if item != '':
            cq.append(item)
    q3 = [1, 10, 13]
    q10 = [1, 5, 9, 10, 12, 13, 15, 17, 18, 19]
    itemscore = {'Never': 1, 'Rarely': 2, 'Sometimes': 3, 'Always': 4}
    itemrscore = {'Never': 4, 'Rarely': 3, 'Sometimes': 2, 'Always': 1}
    item3score = {'Hardly Ever': 1, 'Some of the Time': 2, 'Often': 3}
    score = 0
    print(cq)
    # subsql = []
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    if len(cq) == 3:
        for num, i in enumerate(cq):
            score += item3score[i]
            setattr(record, ('c' + str(q3[num] + 1)), i)
            setattr(record, ('c' + str(q3[num] + 1) + 't'), time.localtime(data['ctime'] / 1000))
    elif len(cq) == 10:
        for num, i in enumerate(cq):
            rev = [1, 2, 6, 8, 9]
            if num in rev:
                score += itemrscore[i]
            else:
                score += itemscore[i]
            setattr(record, ('c' + str(q10[num] + 1)), i)
            setattr(record, ('c' + str(q10[num] + 1) + 't'), time.localtime(data['ctime'] / 1000))
    elif len(cq) == 20:
        for num, i in enumerate(cq):
            rev20 = [0, 4, 5, 8, 9, 14, 15, 18, 19]
            if num in rev20:
                score += itemrscore[i]
            else:
                score += itemscore[i]
            setattr(record, ('c' + str(num + 1)), i)
            setattr(record, ('c' + str(num + 1) + 't'), time.localtime(data['ctime'] / 1000))
    # 记录成绩
    record.cscore = score
    db.session.commit()
    return jsonify({'status': 'success', 'score': score})


@app.route('/openq', methods=['GET', 'POST'])
def openq():
    """
    开放域的问题更新
    :return:
    """

    data = request.get_json(silent=True)
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    setattr(record, data['oitem'], data['content'])
    setattr(record, (data['oitem'] + 't'), time.localtime(data['otime'] / 1000))
    db.session.commit()
    # 第几个问题
    oitem = int(data['oitem'][1:]) - 1
    if oitem == 6:
        session['step'] = 3
        time.sleep(2)
        return jsonify({'status': 'success',
                        'bot': 'I know it is quite common that people suffer from loneliness during the pandemic. We '
                               'have some practical suggestions for coping with loneliness.'})
    else:
        if len(data['content']) >= 10:
            tans = [
                'Thank you.I really appreciate your input.',
                'I see.Thanks for the feedback.',
                'Thank you for your thoughtful input.',
                'Thank you very much for sharing.',
                'Thanks for letting me know.',
                'Thanks for telling me.'
            ]
            fin_res = tans[random.randint(0, 5)]
        else:
            tans = ['I noticed.', 'Got it.', 'I understand.', 'I hear you.', 'I take your point.', 'I know what you mean.']
            fin_res = tans[random.randint(0, 5)]
        time.sleep(2)
        return jsonify({'status': 'success', 'bot': fin_res})
        # UTTERANCE = opdquestions[oitem] + '</s><s>' + data['content']
        # print(UTTERANCE)
        # inputs = tokenizer([UTTERANCE], return_tensors='pt')
        # reply_ids = model.generate(**inputs)
        # bot = tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
        # print(bot)
        # 从字符串末尾查找
        # qindex = bot.rfind("?")
        # 句子里面没有问句
        # if qindex == -1:
        #     gtime = time.time() - (data['otime'] / 1000)
        #     botlog = Botlog(chat=bot, userid=session.get('sid'), qid=oitem, qc=data['content'],
        #                     etime=time.localtime(time.time()), gtime=gtime)
        #     db.session.add(botlog)
        #     db.session.commit()
        #     return jsonify({'status': 'success', 'bot': bot})
        # else:
        #     # 分句
        #     sent_tokenize_list = sent_tokenize(bot)
        #     botmsg = []
        #     for item in sent_tokenize_list:
        #         if item[-1] != '?':
        #             botmsg.append(item)
        #     if len(botmsg) == 0:
        #         randres = ['Ok.', 'Got it.', 'thank you. I really appreciate your input.',
        #                    'I see. Thanks for the feedback.',
        #                    'Thank you for your thoughtful input.', 'Thank you very much for sharing.',
        #                    'Thanks for letting me know.', 'I understand.', 'I hear you.']
        #         botmsg.append(randres[random.randint(0, 9)])
        #     # 将回复写入日志
        #     fin_res = " ".join(botmsg)
        #     gtime = time.time() - (data['otime'] / 1000)
        #     botlog = Botlog(chat=fin_res, userid=session.get('sid'), qid=oitem, qc=data['content'],
        #                     etime=time.localtime(time.time()), gtime=gtime)
        #     db.session.add(botlog)
        #     db.session.commit()
        #     return jsonify({'status': 'success', 'bot': fin_res})


@app.route('/person', methods=['GET', 'POST'])
def person():
    """
    个人信息和性格的更新
    :return:
    """
    data = request.get_json(silent=True)
    str_personality = [str(i) for i in data['personality']]
    str_sqp1ans = [str(i) for i in data['sqp1ans']]
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    print(record)
    record.age = data['age']
    record.gender = data['gender']
    record.loc = data['location']
    record.edu = data['education']
    record.faculty = data['faculty']
    record.mental = data['mental']
    record.personality = ",".join(str_personality)
    record.sqp1ans = ",".join(str_sqp1ans)
    record.etime = time.localtime(data['etime'] / 1000)
    db.session.commit()
    # if record.category == 0:
    #     qnum = 0
    # elif record.category == 1 or record.category == 2:o
    #     qnum = 3
    # elif record.category == 3 or record.category == 4:
    #     qnum = 10
    # else:
    #     qnum = 20
    # category = record.category % 2
    session['step'] = 2
    return jsonify({'status': 'success'})


@app.route('/sqans', methods=['GET', 'POST'])
def sqans():
    """
    survey的问题提交
    :return:
    """
    data = request.get_json(silent=True)
    str_qans = [str(i) for i in data['qans']]
    print(str_qans)
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    record.sqans = ",".join(str_qans)
    record.sqtime = time.localtime(data['sqtime'] / 1000)
    db.session.commit()
    return jsonify({'status': 'success'})


@app.route('/finish', methods=['GET', 'POST'])
def finish():
    """
    openended的问题提交
    :return:
    """
    data = request.get_json(silent=True)
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    record.soq1 = data['soq1']
    record.soq2 = data['soq2']
    record.soq3 = data['soq3']
    record.soq4 = data['soq4']
    record.soq5 = data['soq5']
    record.soqtime = time.localtime(data['soqtime'] / 1000)
    db.session.commit()
    # interview界面结束
    session['step'] = 4
    if checkfinish():
        session['uuid'] = True
    return jsonify({'status': 'success'})


@app.route('/getcode', methods=['GET', 'POST'])
def getcode():
    """
    检查资格如果有效返回码
    :return:
    """
    if session.get('sid') and session.get('uuid') == True:
        # 判断有无记录
        code = Coupon.query.filter(Coupon.uid == session.get('sid')).first()
        print(code)
        if code is None:
            print(2)
            # 没有兑换记录
            newcode = Coupon.query.filter(Coupon.used == 0).first()
            if newcode is None:
                print(3)
                return jsonify({'uuid': 'All coupons have been issued, thank you for your participation.', 'status': 1})
            else:
                print(4)
                print(newcode)
                newcode.uid = session.get('sid')
                newcode.used = 1
                newcode.ctime = time.localtime(time.time())
                db.session.flush()
                db.session.commit()

                return jsonify({'uuid': newcode.uuid, 'status': 1})
        else:
            print(5)
            return jsonify({'uuid': code.uuid, 'status': 1})
    else:
        print(6)
        return jsonify({'uuid': None, 'status': 0})


def checkfinish():
    checkitem = ['intro', 'mood', 'o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'age', 'gender', 'personality',
                 'sqans', 'sqp1ans', 'soq2', 'soq3', 'soq4', 'soq5']
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    # 有记录了
    if record is not None:
        for item in checkitem:
            if getattr(record, item) is None:
                return False
        return True
    else:
        return False


@app.route('/email', methods=['POST'])
def email():
    """
    用户email提交
    :return:
    """
    data = request.get_json(silent=True)
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    record.email = data['email']
    record.f2f = data['f2f']
    record.draw = data['draw']
    db.session.commit()
    return jsonify({'status': 1})


@app.route('/setscore', methods=['POST'])
def setscore():
    """
    用户ucla成绩提交提交
    :return:
    """
    data = request.get_json(silent=True)
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    record.cscore = data['score']
    record.rbtime = time.localtime(data['rbtime'] / 1000)
    db.session.commit()
    return jsonify({'status': 1})


@app.route('/closescore', methods=['POST'])
def closescore():
    """
    用户关闭ucla表单的时间
    :return:
    """
    data = request.get_json(silent=True)
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    record.ratime = time.localtime(data['ratime'] / 1000)
    db.session.commit()
    return jsonify({'status': 1})


@app.route('/setrbtime', methods=['POST'])
def setrbtime():
    """
    用户打开ucla表单的时间
    :return:
    """
    data = request.get_json(silent=True)
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    record.rbtime = time.localtime(data['rbtime'] / 1000)
    db.session.commit()
    return jsonify({'status': 1})


@app.route('/setftime', methods=['POST'])
def setftime():
    """
    用户打开survey表单的时间
    :return:
    """
    data = request.get_json(silent=True)
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    record.ftime = time.localtime(data['ftime'] / 1000)
    db.session.commit()
    return jsonify({'status': 1})


@app.route('/setltime', methods=['POST'])
def setltime():
    """
    用户开始ucla测试的时间
    :return:
    """
    data = request.get_json(silent=True)
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    record.ltime = time.localtime(data['ltime'] / 1000)
    db.session.commit()
    return jsonify({'status': 1})


@app.route('/setotime', methods=['POST'])
def setotime():
    """
    用户开始opened question的时间
    :return:
    """
    data = request.get_json(silent=True)
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    record.otime = time.localtime(data['otime'] / 1000)
    db.session.commit()
    return jsonify({'status': 1})


@app.route('/moodn', methods=['GET', 'POST'])
def moodn():
    """
    结束心情选择
    :return:
    """
    data = request.get_json(silent=True)
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    record.moodn = data['mood']
    record.mntime = time.localtime(data['mtime'] / 1000)
    db.session.commit()
    return jsonify({'status': 'success'})


@app.route('/surveyscore', methods=['GET', 'POST'])
def surveyscore():
    record = Records.query.filter(Records.id == session.get('id'), Records.sid == session.get('sid')).first()
    if record.category == 0:
        qnum = 0
    elif record.category == 1 or record.category == 2:
        qnum = 3
    elif record.category == 3 or record.category == 4:
        qnum = 10
    else:
        qnum = 20
    category = record.category % 2
    return jsonify({'score': record.cscore, 'qnum': qnum, 'category': category})


if __name__ == '__main__':
    app.run(debug=True)
