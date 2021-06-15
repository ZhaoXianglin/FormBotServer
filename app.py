from flask import Flask, jsonify, request
from config import *
import math
import time
import hashlib
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return '你在看什么？'


@app.route('/add', methods=['POST'])
def add():
    """
    新建一条记录，在首页点击
    :return:
    """
    data = request.get_json(silent=True)
    ts = int(round(time.time() * 1000))
    print(ts-5000)
    print(data['ts'])
    if ts-5000 < data['ts'] < ts:
        stime = time.strftime('%Y-%m-%d %H:%M:%S')
        m = hashlib.md5(stime.encode(encoding='utf8'))
        sid = m.hexdigest()
        sql = "INSERT INTO `fb_records` (`id`, `sid`, `stime`) VALUES (NULL ,'{0}','{1}');".format(sid, stime)
        db = SQLManager()
        id = db.create(sql)
        db.close()
        return jsonify({'id': id, 'sid': sid})
    else:
        return jsonify({'id': None, 'sid': None})


@app.route('/self', methods=['POST'])
def self():
    """
    自我介绍
    :return:
    """
    data = request.get_json(silent=True)
    sql = "UPDATE `fb_records` SET `intro` = '{0}', `itime`= '{1}' WHERE `id` = '{2}' and `sid`= '{3}';".format(data['intro'], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['itime']/1000)), data['id'], data['sid'])
    db = SQLManager()
    db.moddify(sql)
    db.close()
    return jsonify({'status': 'success'})


@app.route('/mood', methods=['GET', 'POST'])
def mood():
    """
    心情选择
    :return:
    """
    data = request.get_json(silent=True)
    sql = "UPDATE `fb_records` SET `mood` = '{0}', `mtime`= '{1}' WHERE `id` = '{2}' and `sid`= '{3}';".format(
        data['mood'], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['mtime'] / 1000)), data['id'],
        data['sid'])
    db = SQLManager()
    db.moddify(sql)
    db.close()
    return jsonify({'status': 'success'})


@app.route('/ucla', methods=['GET', 'POST'])
def ucla():
    """
    ucla测试单条更新
    :return:
    """
    data = request.get_json(silent=True)

    sql = "UPDATE `fb_records` SET `{0}` = '{1}', `{2}`= '{3}' WHERE `id` = '{4}' and `sid`= '{5}';".format(
        data['citem'], data['content'], data['citem']+'t',
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['ctime'] / 1000)), data['id'],
        data['sid'])
    print(sql)
    db = SQLManager()
    db.moddify(sql)
    db.close()
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
        if item is not '':
            cq.append(item)
    q3 = [1, 10, 13]
    q10 = [1, 5, 9, 10, 12, 13, 15, 17, 18, 19]
    itemscore = {'Never': 1, 'Rarely': 2, 'Sometimes': 3, 'Always': 4}
    itemrscore = {'Never': 4, 'Rarely': 3, 'Sometimes': 2, 'Always': 1}
    score = 0
    print(cq)
    subsql = []
    if len(cq) is 3:
        for num, i in enumerate(cq):
            score += itemscore[i]
            subsql.append("`c" + str(q3[num]+1) + "` = '" + i + "', `c" + str(q3[num]+1) + "t` = '" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['ctime'] / 1000)) + "'")
    elif len(cq) is 10:
        for num, i in enumerate(cq):
            rev = [1, 2, 6, 8, 9]
            if num in rev:
                score += itemrscore[i]
            else:
                score += itemscore[i]
            subsql.append("`c" + str(q10[num]+1) + "` = '" + i + "', `c" + str(q10[num]+1) + "t` = '" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['ctime'] / 1000)) + "'")
    elif len(cq) is 20:
        for num, i in enumerate(cq):
            rev20 = [0, 4, 5, 8, 9, 14, 15, 18, 19]
            if num in rev20:
                score += itemrscore[i]
            else:
                score += itemscore[i]
            subsql.append("`c" + str(num+1) + "` = '" + i + "', `c" + str(num+1) + "t` = '" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['ctime'] / 1000)) + "'")
    print(subsql)
    sql = "UPDATE `fb_records` SET {0} WHERE `id` = '{1}' and `sid`= '{2}';".format(','.join(subsql), data['id'],data['sid'])
    print(sql)
    db = SQLManager()
    db.moddify(sql)
    db.close()
    return jsonify({'status': 'success', 'score': score})


@app.route('/openq', methods=['GET', 'POST'])
def openq():
    """
    开放域的问题更新
    :return:
    """
    data = request.get_json(silent=True)

    sql = "UPDATE `fb_records` SET `{0}` = '{1}', `{2}`= '{3}' WHERE `id` = '{4}' and `sid`= '{5}';".format(
        data['oitem'], data['content'], data['oitem'] + 't',
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['otime'] / 1000)), data['id'],
        data['sid'])
    print(sql)
    db = SQLManager()
    db.moddify(sql)
    db.close()
    return jsonify({'status': 'success'})


@app.route('/person', methods=['GET', 'POST'])
def person():
    """
    个人信息的更新
    :return:
    """
    data = request.get_json(silent=True)
    str_personality = [str(i) for i in data['personality']]
    print(str_personality)
    sql = "UPDATE `fb_records` SET `age` = '{0}', `gender`= '{1}',`personality`='{2}',`etime`='{3}' WHERE `id` = '{4}' and `sid`= '{5}';".format(data['age'], data['gender'], ",".join(str_personality), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['etime'] / 1000)), data['id'], data['sid'])
    print(sql)
    db = SQLManager()
    db.moddify(sql)
    db.close()
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run()
