import psycopg2
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, filename="app.log",
                    format="%(asctime)s %(levelname)s %(message)s")
logger.addHandler(RotatingFileHandler('app.log', maxBytes=200000, backupCount=1))


user = 'postgres'
password = 'postgres'
host = '127.0.0.1'
port = '5432'
database = 'postgres'

def dbquery(usr_id):
        try:
            connection = psycopg2.connect(user=user,
                                        password=password,
                                        host=host, 
                                        port=port,
                                        database=database)
            cursor = connection.cursor()
            query_str = "select username from accounts where user_id = '{}'".format(usr_id)
            logging.info('query_str = ' + query_str)

            cursor.execute(query_str)
            result = cursor.fetchall()
            logging.info('Query result = ' + str(result))

            return result
        
        except (Exception, psycopg2.Error) as error:
            logging.error(error)

        finally:
            if connection: #type: ignore
                cursor.close() #type: ignore
                logging.info('Cursor closed')
                connection.close()
                logging.info('Connection closed')

if __name__ == '__main__': 
    print(dbquery(123))