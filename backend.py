from flask import Flask,jsonify,request
from contact import Contact,ContactBook

cb=ContactBook()
app=Flask(__name__)


@app.route('/contacts',methods=['GET'])
def get_all_contacts():
    contacts=cb.get_all_contacts()
    return jsonify(contacts)


@app.route('/contact/<name>',methods=['GET'])
def get_contact_by_name(name):
    contact=cb.get_contact_by_name(name)
    if contact:
        return jsonify(contact.to_dict())
    
    else:
        return jsonify({"error":f"no contact with name {name} found"}),404

@app.route('/contact',methods=['POST'])
def add_contact():
    data=request.json
    name=data['name']
    no=data['number']
    email=data['email']
    
    contact=Contact(name,no,email)
    success,message=cb.add_contact(contact)
    
    if success:
        return jsonify({"message":message}),201
    else:
        return jsonify({"message":message}),400

@app.route('/contact/<name>',methods=['PUT'])
def update_contact(name):
    data=request.json
    no=data.get('number')
    email=data.get('email')
    
    success,message=cb.update_contact(name,no,email)
    if success:
            return jsonify({"message":message}),201
    else:
        return jsonify({"message":message}),404
    

@app.route('/contact/<name>',methods=['DELETE'])
def delete_contact(name):
    success,message=cb.delete_contact(name)
    if success:
        return jsonify({"message":message}),201
    else:
        return jsonify({"message":message}),404
    
    
if __name__ == '__main__':
    app.run(debug=True)