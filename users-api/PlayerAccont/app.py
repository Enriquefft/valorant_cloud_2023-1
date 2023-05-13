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

      

class UsuarioCompetitivo(Resource):
    def get(self,id):

        try: 

            conexion = mysql.connect()
            consulta = conexion.cursor()

            consulta.execute("SELECT id FROM AppUser WHERE id = %s",(id))

            if len(consulta.fetchall()) == 0:
                return jsonify({"status" : 404 , "msg" : "El usuario no existe"})

            consulta.execute("SELECT idUsuario FROM PlayerAccount WHERE idUsuario = %s",(id))

            if len(consulta.fetchall()) == 0:
                return jsonify({"status" : 404 , "msg" : "El usuario valorant no existe"})



            c1 = """SELECT idUsuario,rango,nivel,totalMuertes,totalPartidos,totalAsesinatos 
                    FROM PlayerAccount WHERE idUsuario = %s"""       
            
            consulta.execute(c1,(id))            

            playerAccont = {}

            for filas in consulta.fetchall():
                playerAccont["idUsuario"] = filas[0]
                playerAccont["rango"] = filas[1]
                playerAccont["nivel"] = filas[2]
                playerAccont["totalMuertes"] = filas[3]
                playerAccont["totalPartidos"] = filas[4]
                playerAccont["totalAsesinatos"] = filas[5]

            
            return jsonify(playerAccont)  

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
                return jsonify({"status" : 404 , "msg" : "El usuario valorant no existe"})
            
            consulta.execute("SELECT idUsuario FROM PlayerAccount WHERE idUsuario = %s",(id))


            
            if len(consulta.fetchall()) >0:
                return jsonify({"status" : 404 , "msg" : "El usuario valorant ya existe"})
                                            
            rango = request.form["rango"]
            nivel = request.form["nivel"]

            list_rangos = ["IRON 1","IRON 2","IRON 3","BRONZE 1","BRONZE 2","BRONZE 3","SILVER 1","SILVER 2","SILVER 3","GOLD 1","GOLD 2","GOLD 3","PLATINUM 1","PLATINUM 2","PLATINUM 3","DIAMOND 1","DIAMOND 2","DIAMOND 3","IMMORTAL 1","IMMORTAL 2","IMMORTAL 3","RADIANT"]

            if rango.upper() not in list_rangos:
                return jsonify({"status" : 404 , "msg" : "El rango no existe o no esta bien escrito"})
            
            
            c1 = """SELECT SUM(muertes),SUM(asesinatos),SUM(idUsuario) FROM Matches 
                    WHERE idUsuario = %s"""

            consulta.execute(c1,(id))            

            

            for filas in consulta.fetchall():
                totalMuertes = filas[2] if filas[2] != None else 0
                totalPartidos = filas[1] if filas[1] != None else 0
                totalAsesinatos = filas[0] if filas[0] != None else 0
            
            c2 = """INSERT INTO PlayerAccount(idUsuario,rango,nivel,totalMuertes,totalPartidos,totalAsesinatos)
                    VALUES (%s, %s, %s, %s, %s, %s)"""

            consulta.execute(c2,(id,rango.upper(),nivel,totalMuertes,totalPartidos,totalAsesinatos))

            conexion.commit()

            return jsonify({"status" : 200 , "msg" : "El usuario valorant se ha registado"})
        
        except Exception as e:
            print(e)
        
        finally:
            consulta.close()
            conexion.close()
            


    def put(self,id):
        conexion = mysql.connect()
        consulta = conexion.cursor()

        consulta.execute("SELECT id FROM AppUser WHERE id = %s",(id))

        if len(consulta.fetchall()) == 0:
            return jsonify({"status" : 404 , "msg" : "El usuario valorant no existe"})
        

        rango = request.form["rango"]
        nivel = request.form["nivel"]

        list_rangos = ["IRON 1","IRON 2","IRON 3","BRONZE 1","BRONZE 2","BRONZE 3","SILVER 1","SILVER 2","SILVER 3","GOLD 1","GOLD 2","GOLD 3","PLATINUM 1","PLATINUM 2","PLATINUM 3","DIAMOND 1","DIAMOND 2","DIAMOND 3","IMMORTAL 1","IMMORTAL 2","IMMORTAL 3","RADIANT"]

        if rango.upper() not in list_rangos:
            return jsonify({"status" : 404 , "msg" : "El rango no existe o no esta bien escrito"})

        consulta.execute("UPDATE PlayerAccount SET rango = %s, nivel = %s",(rango.upper(),nivel))

        conexion.commit()

        return jsonify({"status" : 200, "msg" : "El usuario valorant se ha actualizado"})


    def delete(self,id):
        conexion = mysql.connect()
        consulta = conexion.cursor()

        consulta.execute("SELECT id FROM AppUser WHERE id = %s",(id))

        if len(consulta.fetchall()) == 0:
            return jsonify({"status" : 404 , "msg" : "El usuario valorant no existe"})
        

        consulta.execute("DELETE FROM PlayerAccount WHERE idUsuario = %s",(id))

        conexion.commit()

        return jsonify({"status" : 200 , "msg" : "El usuario valorant se ha eliminado"})



            
            

            
   

        

api.add_resource(UsuarioCompetitivo, '/competitivo/<int:id>', endpoint='competitivo')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)