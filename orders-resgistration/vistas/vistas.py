from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from datetime import datetime

#
import socket


from modelos import \
    db, \
    Orden, OrdenSchema


orden_schema = OrdenSchema()


class VistaOrden(Resource):

    def post(self):
        # Creacion de orden
        nueva_orden = Orden(
            vendedor=request.json["vendedor"],
            descripcion=request.json["descripcion"],
            producto=request.json["producto"],
            cantidad=request.json["cantidad"],
            fecha=datetime.strptime(request.json["fecha"], '%Y-%m-%d').date()
        )
        db.session.add(nueva_orden)
        db.session.commit()
        #
        hostName = socket.gethostname()
        hostIp = socket.gethostbyname(hostName)
        requestAttended = {
            "hostName": hostName,
            "ipAddress": hostIp
        }

        return {"data": {"requestAttended": requestAttended, "orderProcessed": orden_schema.dump(nueva_orden)}}
