from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector


app = Flask(__name__)
CORS(app)



# Créer une connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employees_db"
)

# Créer un curseur pour exécuter des requêtes
cursor = conn.cursor()
@ app.route('/', methods=['GET'])
def get_raouf():
     return 'hello Jean'

@app.route('/api/v1/employees', methods=['GET'])
def get_employees():
    # Exécuter une requête SELECT pour récupérer tous les employés
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    # Convertir le résultat en une liste de dictionnaires
    employees = []
    for row in result:
        employee = {"id": row[0], "firstName": row[1], "lastName": row[2], "emailId": row[3]}
        employees.append(employee)
    return jsonify(employees)

@app.route('/api/v1/employees', methods=['POST'])
def add_employee():
    employee = request.get_json()
    employee.append(employee)
    return jsonify({"message": "Employee added successfully."}), 201

@app.route('/api/v1/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    for employee in employee:
        if employee['id'] == employee_id:
            employee['firstName'] = request.json['firstName']
            employee['lastName'] = request.json['lastName']
            employee['emailId'] = request.json['emailId']
            return jsonify({"message": "Employee updated successfully."}), 200
    return jsonify({"message": "Employee not found."}), 404

@app.route('/api/v1/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    for employee in employee:
        if employee['id'] == employee_id:
            employee.remove(employee)
            return jsonify({"message": "Employee deleted successfully."}), 200
    return jsonify({"message": "Employee not found."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
