import psycopg2
from config import config
from functions import create_tables, add_new_user, add_new_user_score, get_user_id, update_user_score



def main():
    """main function with all the logic"""
    
    # creating tables
    #create_tables()
    #add_new_user('aset')
    #print(get_user_id('aset'))
    #add_new_user_score(get_user_id('aset'), 1, 20)
    update_user_score(get_user_id('player'), 1, 1)

if __name__ == "__main__":
    main()