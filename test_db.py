import pymysql
from sqlalchemy import create_engine, text

def test_mysql_connection():
    # Conexión directa con pymysql
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='x1z*9j-WTrSrPauq',  # Cambia si MySQL tiene contraseña
            database='mydrugs_db'
        )
        print("✅ [PyMySQL] Conexión directa a MySQL exitosa!")
        conn.close()
    except pymysql.Error as e:
        print(f"❌ [PyMySQL] Error: {e}")

    # Conexión via SQLAlchemy
    try:
        engine = create_engine("mysql+pymysql://root:x1z*9j-WTrSrPauq@localhost/mydrugs_db")
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("✅ [SQLAlchemy] Conexión exitosa!")
    except Exception as e:
        print(f"❌ [SQLAlchemy] Error: {e}")

test_mysql_connection()