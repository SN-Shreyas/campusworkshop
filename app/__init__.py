"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7knt269vf5qb8c7eg-a.oregon-postgres.render.com",
        database="to_do_qr93",
        user="root",
        password="fGNfaNCC5T0Yq0sQpzHNIi7XUHpkHkRg")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
