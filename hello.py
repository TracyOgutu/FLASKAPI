from flask import Flask,jsonify,request,abort
app = Flask(__name__)

entry=[{'record':'Got a job'},
{'record':'My birthday'},
{'record':'Won an award'}]

@app.route('/',methods=['GET'])
def index():
    return jsonify({'message':'It works'})

@app.route('/entry',methods=['GET'])
def all_entries():
    return jsonify({'entry':entry})

@app.route('/entry/<string:record>',methods=['GET'])
def searchentry(record):
    '''
    Returns the entry that matches the record 
    '''
    ents=[ent for ent in entry if ent['record']==record]
    return jsonify ({'ent':ents[0]})

@app.route('/entry',methods=['POST'])
def addentry():
    if 'record' in request.json and type(request.json['record'])!=str:
        abort(404,'please input a string')
    
    entrypost=request.get_json(['record'])
    entry.append(entrypost)
    return jsonify({'entry':entry})

@app.route('/entry/<string:record>',methods=['PUT'])
def updatentry(record):
    ents=[ent for ent in entry if ent['record']==record]
    ents[0]['record']=request.get_json(['record'])
    return jsonify({'ent':ents[0]})

if __name__ == '__main__':
    app.run(debug = True)

