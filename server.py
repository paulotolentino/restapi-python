# imports das libs que iremos utlizar
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from sqlalchemy import text

db_connect = create_engine("sqlite:///exemplo.db")
app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):
        conn = db_connect.connect()
        sql = text("select * from user")
        query = conn.execute(sql)
        conn.commit()
        conn.close()
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        name = request.json["name"]
        email = request.json["email"]

        sql1 = text("insert into user values(null, '{0}','{1}')".format(name, email))
        conn.execute(sql1)

        sql2 = text("select * from user order by id desc limit 1")
        query = conn.execute(sql2)
        conn.commit()
        conn.close()
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def put(self):
        conn = db_connect.connect()
        id = request.json["id"]
        name = request.json["name"]
        email = request.json["email"]

        sql1 = text(
            "update user set name ='"
            + str(name)
            + "', email ='"
            + str(email)
            + "'  where id =%d " % int(id)
        )
        conn.execute(sql1)

        sql2 = text("select * from user where id=%d " % int(id))
        query = conn.execute(sql2)
        conn.commit()
        conn.close()
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)


class UserById(Resource):
    def delete(self, id):
        conn = db_connect.connect()
        sql = text("delete from user where id=%d " % int(id))
        conn.execute(sql)
        conn.commit()
        conn.close()
        return {"status": "success"}

    def get(self, id):
        conn = db_connect.connect()
        sql = text("select * from user where id =%d " % int(id))
        query = conn.execute(sql)
        conn.commit()
        conn.close()
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)


api.add_resource(Users, "/users")
api.add_resource(UserById, "/users/<id>")

if __name__ == "__main__":
    app.run()
