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
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'utec'
app.config['MYSQL_DATABASE_DB'] = 'ValorantDB'
app.config['MYSQL_DATABASE_HOST'] = '3.227.149.124'
app.config['MYSQL_DATABASE_PORT'] = 8005

#Initialize the MySQL extension
mysql.init_app(app)

conexion = None
consulta = None

class Partidas(Resource):
    def get(self,id):
        try:
            conexion = mysql.connect()
            consulta = conexion.cursor()

            consulta.execute("SELECT id FROM AppUser WHERE id = %s",(id))

            if len(consulta.fetchall()) == 0:
                return jsonify({"status" : 404 , "msg" : "El usuario no existe"})

            consulta.execute("SELECT DISTINCT t1.id FROM AppUser t1 JOIN Matches t2 ON t1.id = t2.idUsuario")

            verificadorId = False

            

            for userid in consulta.fetchall():
                if userid[0] == id:
                    
                    verificadorId = True
                    break
            
            if verificadorId == False:
                return jsonify({"status" : 404 , "msg" : "El usuario no tiene partidas jugadas"})


            consulta.execute("SELECT * FROM Matches WHERE idUsuario = %s",(id))

            listaPartidas = []

            for filas in consulta.fetchall():
                diccionario = {
                    "codigo" : filas[0],
                    "idUsuario" : filas[1],
                    "agente" : filas[2],
                    "muertes": filas[3],
                    "asesinatos": filas[4]

                }

                listaPartidas.append(diccionario)

            if len(listaPartidas) > 0 :
                return jsonify(listaPartidas)
            else:
                return jsonify({"status":200 , "msg" : "El usuario no tiene partidas jugadas"} )
                

        except Exception as e:
            print(e)
        
        finally:
            consulta.close()
            conexion.close()


    def post(self,id):
        try:
            conexion = mysql.connect()
            consulta = conexion.cursor()

            consulta.execute("SELECT id FROM AppUser WHERE id = %s",(id))

            if len(consulta.fetchall()) == 0:
                return jsonify({"status" : 404 , "msg" : "El usuario no existe"})

                      
            agente = request.form["agente"]
            muertes = request.form["muertes"]
            asesinatos = request.form["asesinatos"]

            c1 = "INSERT INTO Matches(idUsuario,agente,muertes,asesinatos) VALUES (%s,%s,%s,%s)"

            consulta.execute(c1,(id,agente,muertes,asesinatos))
            conexion.commit()

            return jsonify({"status" : 200 , "msg" : "La partida ha sido registrada exitosamente"})
        
        except Exception as e:
            print(e)
            
        finally:
            consulta.close()
            conexion.close()


class Partida(Resource):
    def get(self, codigo):
        try:
            conexion = mysql.connect()
            consulta = conexion.cursor()

            consulta.execute("SELECT * FROM Matches WHERE codigo = %s",(codigo))

            partida = {}

            for filas in consulta.fetchall():
                partida["codigo"] = filas[0]
                partida["idUsuario"] = filas[1]
                partida["agente"] = filas[2]
                partida["muertes"] = filas[3]
                partida["asesinatos"] = filas[4]

            

            if partida == None:
                return jsonify({"status":404 , "msg" : "La partida no existe"})
            else:
                return jsonify(partida)
        
    
            
        
        except Exception as e:
            print(e)

        finally:
            consulta.close()
            conexion.close()
            
    def put(self,codigo):

        try:
            conexion = mysql.connect()
            consulta = conexion.cursor()

            partidaUsuario = None

            consulta.execute("SELECT * FROM Matches WHERE codigo = %s",(codigo))

            
            for fila in consulta.fetchall():

                if fila[0] == codigo:

                    diccionario = {

                        "codigo" : fila[0],
                        "idUsuario" : fila[1],
                        "agente" : fila[2],
                        "muertes" : fila[3],
                        "asesinatos" : fila[4]
                    }

                    partidaUsuario = diccionario
                    break;
            
            

            if partidaUsuario == None:
                return jsonify({"status" : 404 , "msg" : "El codigo de la partida invalida o no existente"})

           

            idUsuario = request.form["idUsuario"]
            agente = request.form["agente"]
            muertes = request.form["muertes"]
            asesinatos = request.form["asesinatos"]

            c1 = """UPDATE Matches SET idUsuario = %s, agente = %s, muertes = %s, asesinatos= %s
                    WHERE codigo = %s"""

            consulta.execute(c1,(idUsuario,agente,muertes,asesinatos,codigo))
            conexion.commit()

            return jsonify({"status" : 200 , "msg": "La partida fue actualizada exitosamente"})             
                

            
        except Exception as e:
            print(e)
        
        finally:
            consulta.close()
            conexion.close()

    def delete(self,codigo):
        try:
            conexion = mysql.connect()
            consulta = conexion.cursor()

            partidaUsuario = None

            consulta.execute("SELECT * FROM Matches WHERE codigo = %s",(codigo))

            for fila in consulta.fetchall():

                if fila[0] == codigo:

                    diccionario = {

                        "codigo" : fila[0],
                        "idUsuario" : fila[1],
                        "agente" : fila[2],
                        "muertes" : fila[3],
                        "asesinatos" : fila[4]
                    }

                    partidaUsuario = diccionario
                    break;
            
            if partidaUsuario == None:
                return jsonify({"status" : 404 , "msg" : "El codigo de la partida invalida o no existente"})

            else:

                c1 = "DELETE FROM Matches WHERE codigo = %s"

                consulta.execute(c1,(codigo))
                conexion.commit()

                return jsonify({"status" : 200 , "msg" : "La partida ha sido eliminada"})

        except Exception as e:
            print(e)
                

        finally:
            consulta.close()
            conexion.close()
            




api.add_resource(Partidas, '/partidas/<int:id>', endpoint='partidas')
api.add_resource(Partida, '/partida/<int:codigo>', endpoint='partida')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)