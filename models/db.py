# import os

# import psycopg2
# from dotenv import load_dotenv
# from flask import Blueprint, flash, redirect, render_template, request

# admin = Blueprint("admin", __name__)

# DATABASE_URL = os.getenv("DATABASE_URL")

# ALLOWED_TABLES = {
#     "os_files": "Operating Systems",
#     "dbms_files": "DBMS",
#     "cn_files": "Computer Networks",
# }


# def get_db():
#     return psycopg2.connect(DATABASE_URL)


# @admin.route("/admin/upload", methods=["GET", "POST"])
# def upload_file():
#     if request.method == "POST":
#         table = request.form.get("table")
#         file = request.files.get("file")

#         if table not in ALLOWED_TABLES:
#             return "Invalid table selected", 400

#         if not file:
#             return "No file selected", 400

#         conn = get_db()
#         cur = conn.cursor()

#         sql = f"""
#             INSERT INTO {table} (filename, content_type, file_data)
#             VALUES (%s, %s, %s)
#         """

#         cur.execute(
#             sql, (file.filename, file.content_type, psycopg2.Binary(file.read()))
#         )

#         conn.commit()
#         cur.close()
#         conn.close()
#         return redirect("/admin/upload")

#     return render_template("upload.html", tables=ALLOWED_TABLES)
