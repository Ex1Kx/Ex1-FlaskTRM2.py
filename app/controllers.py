
from flask.views import MethodView
from flask import jsonify, request



class RegisterUserControllers(MethodView):
    """
        Example register
    """
    def post(self):
        content = request.get_json()
        nombres = content.get("nombre")
        password = content.get("password")
        ciudad = content.get("ciudad")

        return jsonify({"Status": "Registro ok ",
                        "nombres": nombres, "password": password,
                        "ciudad": ciudad}), 200


    def get(self):
        return jsonify({"Status": "Respondiendo por metodo get"}), 200




class LoginUserControllers(MethodView):
    """
        Example Login
    """
    def post(self):
        nombre = request.form.get("nombre")
        password = request.form.get("password")
        return jsonify({"Status": "Login correcto",
                        "nombre": nombre, "password": password}), 200


class LineControllers(MethodView):
    """
        Example register
    """

    def post(self):
        return jsonify({"Status": "la linea se ha creado exitosamente"}), 200

    def get(self):
        string_query = request.args.get("id")
        if string_query:
            return jsonify({"linea solicitada de id": string_query}), 200

        return jsonify({"info de todas las lineas": "aca va toda la info de todas las lineas"}), 200



class JsonControllers(MethodView):
    """
        Example Json
    """
    def post(self):
        content = request.get_json()
        nombres = content.get("nombres")
        ciudad = content.get("ciudad")
        return jsonify({"Status": "JSON recibido y procesado correctamente",
                        "nombre": nombres, "ciudad": ciudad}), 200
