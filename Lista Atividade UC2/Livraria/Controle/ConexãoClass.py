import psycopg2
class Conexão:
    def __init__(self, dbname, host, port, user, password):
        self._dbname = dbname
        self._dbname = dbname
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        
    def consultarBanco(self, sql):
        conn = psycopg2.connect(dbname = self._dbname, host = self._host, port = self._port, user = self._user, password = self._password)

        cursor = conn.cursor()
        try:
            cursor.execute(sql)
        except:
            return False
        resultado = cursor.fetchall()

        cursor.close()
        conn.close()

        return resultado
    
    def manipularBanco(self,sql):
        conn = psycopg2.connect(dbname = self._dbname, host = self._host, port = self._port, user = self._user, password = self._password)
        cursor = conn.cursor()
        try:    
            cursor.execute(sql)

            conn.commit()

            cursor.close()

            conn.close()
            return True
        except:
            return False

