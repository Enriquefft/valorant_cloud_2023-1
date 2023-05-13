from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api

#Create an instance of Flask
app = Flask(__name__)

#Create an instance of MySQL
mysql = MySQL()

#Create an instance of Flask RESTful API
api = Api(app)

#Set database credentials in config.
app.config.from_object('../config')

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

            consulta.execute("SELECT * FROM usuarios") #Consulta de todos los usuarios

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
            conexion = mysql.connect()
            consulta = conexion.cursor()

            usuario = request.form["usuario"]
            contrasena = request.form["contrasena"]
            correo = request.form["correo"]
            edad = request.form["edad"]
            sexo = request.form["sexo"]

            consulta.execute("SELECT usuario,correo FROM usuarios") #consultar solo los usuariosy correos
        
            for fila in consulta.fetchall(): #extraemos todos los usuarios
                
                if fila[0] == usuario: # usuario repetido 
                    return jsonify({"status" : 404, "msg" : f"El usuario {usuario} ya esta registrado" })
                
                elif fila[1] == correo: # correo repetido
                    return jsonify({"status" : 404, "msg" : f"El correo {correo} ya esta registrado por el usuario {fila[0]}" })

        
        
            c1 = """INSERT INTO usuarios (usuario,contrasena,correo,edad,sexo) 
                    VALUES (%s,%s,%s,%s,%s)""" # insertar los datos con sql 
            
            consulta.execute(c1,(usuario,contrasena,correo,edad,sexo))# insertar los datos a la tabla         
            conexion.commit() #Enviar los datos a la tabla usuarios
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

            consulta.execute("SELECT * FROM usuarios WHERE usuario = %s",(usr)) # consultar el usuario

            for fila in consulta.fetchall():
                diccionario = {  #Diccionario de el usuario
                    "id" : fila[0],
                    "usuario" : fila[1],
                    "contraseña" : fila[2],
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

            consulta.execute("SELECT * FROM usuarios WHERE usuario = %s",(usr)) # consultar el usuario


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
                return f"El usuario {usr} no existe o no se ha escrito correctamente"
            
            else:

                

                
                usuario = request.form["usuario"]
                contrasena = request.form["contrasena"]
                correo = request.form["correo"]
                edad = request.form["edad"]
                sexo = request.form["sexo"]

                consulta.execute("SELECT usuario,correo FROM usuarios") #consultar solo los usuariosy correos
            
                for fila in consulta.fetchall(): #extraemos todos los usuarios

                    if fila[0] == usuario and usuarioPrincipal["usuario"] != usuario: # usuario repetido 
                        return jsonify({"status" : 404, "msg" : f"El usuario {usuario} ya esta registrado" })
                    
                    elif fila[1] == correo and usuarioPrincipal["correo"] != correo: # correo repetido
                        
                        return jsonify({"status" : 404, "msg" : f"El correo {correo} ya esta registrado por el usuario {fila[0]}" })


                c1 = """UPDATE usuarios SET usuario = %s, contrasena = %s, correo = %s, edad= %s, sexo= %s
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
            
            consulta.execute("SELECT * FROM usuarios WHERE usuario = %s",(usr)) # consultar el usuario

            for fila in consulta.fetchall():
                diccionario = {  #Diccionario de el usuario
                "id" : fila[0],
                "usuario" : fila[1],
                "contraseña" : fila[2],
                "correo" : fila[3],
                "edad" : fila[4],
                "sexo" : fila[5]
                }

                usuarioPrincipal = diccionario

                id = usuarioPrincipal["id"]
                consulta.execute("DELETE FROM usuarios WHERE id =%s",(id))
                conexion.commit()
                return jsonify({"status" : 200, "msg" : f"El usuario {usr} fue eliminado exitosamente" }) 
        
        except Exception as e:
            print(e)
        
        finally:
            consulta.close()
            conexion.close()
        
#API resource routes
api.add_resource(ListaUsuario, '/usuarios', endpoint='usuarios')
api.add_resource(Usuario, '/usuario/<usr>', endpoint='usuario')
