import mysql.connector
import dotenv

# get configurations
config = dotenv.dotenv_values()


# database helpers
class Database:

    # function to write sql queries to database
    def to_database(sql):

        # try to query the database
        try:

            # connect to database
            database = mysql.connector.connect(host=config["DATABASE_HOST"],
                                               user=config["DATABASE_USER"],
                                               passwd=config["DATABASE_PASSWORD"],
                                               database=config["DATABASE_NAME"],
                                               auth_plugin="mysql_native_password")

            # initiate cursor
            my_cursor = database.cursor()

            # execute cursor
            my_cursor.execute(sql)

            # make changes in database
            database.commit()

            # close cursor and database connection
            my_cursor.close()
            database.close()

        # unknown exception occurred
        except Exception as e:

            # print the error
            print(e)

    # function to get data with sql queries from database
    def from_database(sql):

        # try to query the database
        try:

            # connect to database
            database = mysql.connector.connect(host=config["DATABASE_HOST"],
                                               user=config["DATABASE_USER"],
                                               passwd=config["DATABASE_PASSWORD"],
                                               database=config["DATABASE_NAME"],
                                               auth_plugin="mysql_native_password")

            # initiate cursor
            my_cursor = database.cursor()

            # execute cursor
            my_cursor.execute(sql)

            # get results from database
            results = my_cursor.fetchall()

            # parse results
            columns = [desc[0] for desc in my_cursor.description]
            parsed_results = []
            for row in results:
                row = dict(zip(columns, row))
                parsed_results.append(row)

            # close cursor and database connection
            my_cursor.close()
            database.close()

        # unknown exception occurred
        except Exception as e:

            # print the error
            print(e)

            # fallback to none
            parsed_results = None

        return parsed_results
