from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api

def create_app(config_file=None):

#Create an instance of Flask
    app = Flask(__name__)

#Create an instance of MySQL
    mysql = MySQL()

#Create an instance of Flask RESTful API
    api = Api(app)

#Set database credentials in config.
    app.config['MYSQL_DATABASE_HOST'] = 'valorant-db.clofpmbdqs3h.us-east-1.rds.amazonaws.com'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_USER'] = 'admin'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'QH013xPlbpPeS9H1KKLC'
    app.config['MYSQL_DATABASE_DB'] = 'ValorantDB'

#Initialize the MySQL extension
    mysql.init_app(app)

    conexion = None 
    consulta = None

#Get All Users, or Create a new user
    class ListaUsuario(Resource):
        
        def get(self):
            try:
                conexion = mysql.connect()
                consulta = conexion.cursor()

                consulta.execute("SELECT * FROM AppUser") #Consulta de todos los usuarios

                lista_usuarios = []
                
                for fila in consulta.fetchall():
                    diccionario = {  #Diccionario de el usuario
                        "id" : fila[0],
                        "usuario" : fila[1],
                        "contrasena" : fila[2],
                        "correo" : fila[3],
                        "edad" : fila[4],
                        "sexo" : fila[5]
                    }
                    lista_usuarios.append(diccionario)

                if lista_usuarios is not None: #Si la "lista_usuarios" no esta vacia retorno el archivo a json
                    return jsonify(lista_usuarios)
                
            except Exception as e:
                print(e)
            finally:
                consulta.close()
                conexion.close()
        
        def post(self):
            try:
                print("posting...")
                print(request.form)
                conexion = mysql.connect()
                consulta = conexion.cursor()

                print("here1")
                usuario = request.form["usuario"]
                print("herex")
                contrasena = request.form["contrasena"]
                print("herex")
                correo = request.form["correo"]
                print("herex")
                edad = request.form["edad"]
                print("herex")
                sexo = request.form["sexo"]
                print("here3")

                consulta.execute("SELECT usuario,correo FROM AppUser") #consultar solo los usuarios y correos
            
                for fila in consulta.fetchall(): #extraemos todos los usuarios
                    
                    if fila[0] == usuario: # usuario repetido 
                        return jsonify({"status" : 404, "msg" : f"El usuario {usuario} ya esta registrado" })
                    
                    elif fila[1] == correo: # correo repetido
                        return jsonify({"status" : 404, "msg" : f"El correo {correo} ya esta registrado por el usuario {fila[0]}" })

            
            
                c1 = """INSERT INTO AppUser (usuario,contrasena,correo,edad,sexo) 
                        VALUES (%s,%s,%s,%s,%s)""" # insertar los datos con sql 
                print(c1)
                
                consulta.execute(c1,(usuario,contrasena,correo,edad,sexo))# insertar los datos a la tabla         
                conexion.commit() #Actualizar la tabla AppUser
                return jsonify({"status" : 200, "msg" : f"El usuario fue creado exitosamente" })
            
            except Exception as e:
                print(e)
                response = jsonify('Failed to add user.')         
                response.status_code = 400 

            finally:
                
                consulta.close()
                conexion.close()                

    class Usuario(Resource):
        def get(self,usr):
            try:
                conexion = mysql.connect()
                consulta = conexion.cursor()
                usuarioPrincipal = None

                consulta.execute("SELECT * FROM AppUser WHERE usuario = %s",(usr)) # consultar el usuario

                for fila in consulta.fetchall():
                    diccionario = {  #Diccionario de el usuario
                        "id" : fila[0],
                        "usuario" : fila[1],
                        "contrasena" : fila[2],
                        "correo" : fila[3],
                        "edad" : fila[4],
                        "sexo" : fila[5]
                    }

                    usuarioPrincipal = diccionario

                if usuarioPrincipal is None:
                    
                    return jsonify({"status" : 404, "msg" : f"El usuario {usr} no existe o no se ha escrito correctamente" })
                else:
                    return jsonify(usuarioPrincipal)

            
            except Exception as e:
                print(e)
            
            finally:
                consulta.close()
                conexion.close()

        
        def put(self,usr):

            try:
                conexion = mysql.connect()
                consulta = conexion.cursor()
                usuarioPrincipal = None

                consulta.execute("SELECT * FROM AppUser WHERE usuario = %s",(usr)) # consultar el usuario


                for fila in consulta.fetchall():
                    diccionario = {  #Diccionario de el usuario
                        "id" : fila[0],
                        "usuario" : fila[1],
                        "contrasena" : fila[2],
                        "correo" : fila[3],
                        "edad" : fila[4],
                        "sexo" : fila[5]
                    }

                    usuarioPrincipal = diccionario 

                
                if usuarioPrincipal is None: # Condicion de existencia
                    return f"El usuario {usr} no existe o no se ha escrito correctamente"
                
                else:

                    

                    
                    usuario = request.form["usuario"]
                    contrasena = request.form["contrasena"]
                    correo = request.form["correo"]
                    edad = request.form["edad"]
                    sexo = request.form["sexo"]

                    consulta.execute("SELECT usuario,correo FROM AppUser") #consultar solo los usuariosy correos
                
                    for fila in consulta.fetchall(): #extraemos todos los usuarios

                        if fila[0] == usuario and usuarioPrincipal["usuario"] != usuario: # usuario repetido 
                            return jsonify({"status" : 404, "msg" : f"El usuario {usuario} ya esta registrado" })
                        
                        elif fila[1] == correo and usuarioPrincipal["correo"] != correo: # correo repetido
                            
                            return jsonify({"status" : 404, "msg" : f"El correo {correo} ya esta registrado por el usuario {fila[0]}" })


                    c1 = """UPDATE AppUser SET usuario = %s, contrasena = %s, correo = %s, edad= %s, sexo= %s
                            WHERE usuario = %s"""

                    usuarioPrincipal["usuario"] = usuario
                    usuarioPrincipal["contrasena"] = contrasena
                    usuarioPrincipal["correo"] = correo
                    usuarioPrincipal["edad"] = edad
                    usuarioPrincipal["sexo"] = sexo



                    consulta.execute(c1,(usuario,contrasena,correo,edad,sexo,usr))
                    conexion.commit()

                    
                    return jsonify({"status" : 200, "msg" : f"El usuario se ha modificado exitosamente" })

            
            except Exception as e:
                print(e)
            
            finally:
                consulta.close()
                conexion.close()

        def delete(self,usr):
            try:
                conexion = mysql.connect()
                consulta = conexion.cursor()
                
                consulta.execute("SELECT * FROM AppUser WHERE usuario = %s",(usr)) # consultar el usuario

                for fila in consulta.fetchall():
                    diccionario = {  #Diccionario de el usuario
                    "id" : fila[0],
                    "usuario" : fila[1],
                    "contrasena" : fila[2],
                    "correo" : fila[3],
                    "edad" : fila[4],
                    "sexo" : fila[5]
                    }

                    usuarioPrincipal = diccionario

                    id = usuarioPrincipal["id"]
                    consulta.execute("DELETE FROM AppUser WHERE id =%s",(id))
                    conexion.commit()
                    return jsonify({"status" : 200, "msg" : f"El usuario {usr} fue eliminado exitosamente" }) 
            
            except Exception as e:
                print(e)        
            finally:
                consulta.close()
                conexion.close()
            
#API resource routes
    api.add_resource(ListaUsuario, '/usuarios', endpoint='usuarios')
    api.add_resource(Usuario, '/usuario/<usr>', endpoint='usuario') #usr = nombre del Usuario Original

    return app
