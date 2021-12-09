import datetime
import edgedb

def main():
    # Establish a connection to an existing database
    # named "test" as an "edgedb" user.
    conn = edgedb.connect(user='edgedb')

    # Create a User object type
    set = conn.query('''
        select Movie {title, director: {first_name, last_name}}
    ''')
    
    for item in set:
        print(item.title)
        print(f'{item.director.first_name} {item.director.last_name}')

    conn.close()

if __name__ == "__main__":
    main()