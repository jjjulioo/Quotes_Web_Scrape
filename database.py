import mysql.connector


def insert_authors(authors_list):
    mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'root', database='quotes_db')

    mycursor = mydb.cursor()
    
    try: 

        query = "INSERT INTO authors (namee, birth_date, birth_loc, descriptionn) VALUES (%s, %s, %s, %s)"
        mycursor.executemany(query, authors_list)
        mydb.commit()

        mycursor.close()
        mydb.close()
        return('Authors inserted succesfully.')

    except mysql.connector.Error as err:
        return f"Error: {err}"
    
    finally:
        # Ensure the cursor and database connection are closed
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

def get_author_ids():
    # Connect to the database
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='quotes_db'
    )

    mycursor = mydb.cursor()

    # Dictionary to store author names and ids
    author_ids = {}

    # Query to retrieve author names and ids
    query = "SELECT author_id, namee FROM authors"
    mycursor.execute(query)

    # Fetch all results and store in dictionary
    for (id, name) in mycursor.fetchall():
        author_ids[name] = id

    # Close the cursor and connection
    mycursor.close()
    mydb.close()
    return author_ids



def insert_quotes(quotes_list):


    mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'root', database='quotes_db')

    mycursor = mydb.cursor()

    # Retrieve author ids
    author_ids = get_author_ids()

    # author_ids has the form ('name': id, ...)
    print(author_ids['Albert Einstein'])

    quotes_withIDs = []

    for i in range(len(quotes_list)):
        try:
            quote = quotes_list[i]
            quote = quote + (author_ids[quote[1]],)
            quotes_withIDs.append(quote)
            print(quote)
        except: 
            pass

    try: 

        # Prepare the insert query for quotes
        query = "INSERT INTO quotes (quote, author, favorite, author_id) VALUES (%s, %s, %s, %s)"
        mycursor.executemany(query, quotes_withIDs)
        mydb.commit()

        mycursor.close()
        mydb.close()
        return('Quotes inserted succesfully.')

    except mysql.connector.Error as err:
        return f"Error: {err}"
    
    finally:
        # Ensure the cursor and database connection are closed
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

def prueba_Insert(): 
    mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'root', database='quotes_db')

    mycursor = mydb.cursor()

    author_ids = get_author_ids()

    print(author_ids)
    
    try:
        query = "INSERT INTO quotes (quote, author, favorite, author_id) VALUES ('Prueba 3', 'Albert Einstein', 0, 1);"
        mycursor.execute(query)

        mydb.commit()

        mycursor.close()
        mydb.close()
        return('Quote einstein inserted correctly inserted succesfully.')
    except mysql.connector.Error as err:
        return f"Error: {err}"

    finally:
        # Ensure the cursor and database connection are closed
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()


def insert_data(authors_list, quotes_list):
    #response_authors = insert_authors(authors_list)
    response_quotes = insert_quotes(quotes_list)
    return response_quotes



