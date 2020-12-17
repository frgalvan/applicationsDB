#!/usr/bin/env python3

# Simple python program powered by sqlite3
# to document which organizations I've applied to
# and other relevant information.
# .schema
# CREATE TABLE applications(
# company_name VARCHAR(30),
# is_denied BOOLEAN,
# role VARCHAR(20),
# date_applied VARCHAR(8),
# resume_name VARCHAR(20));

import sqlite3
import time  # for sleep() to pause execution
import sys

connection = sqlite3.connect("applied.db")
cursor = connection.cursor()


def main():
    print("  ************** Welcome **************")
    print("  This is your local Applied DB where you can search for")
    print("  and/or add organizations to which you've applied.\n")
    print("    1. Search by company name")
    print("    2. Enter new entry")
    print("    X. Save and exit\n")

    user_input = input("Your selection: ")

    while user_input != 'X' and user_input != 'x':
        if (user_input == '1'):
            coName = input(" What's the company's name? ")
            selectCmd = """SELECT * FROM applications WHERE company_name IS "%s" ;""" % coName
            try:
                cursor.execute(selectCmd)
                print(cursor.fetchall()[0])  # returns a tuple embedded in a list, both index-able
            except:
                print(" Company not in DB, yet")
                time.sleep(2)

        elif (user_input == '2'):
            insertCmd = newEntry()
            try:
                cursor.execute(insertCmd)
            except:
                print(" There was a problem with your input.")
                print(" Please try again")
                user_input = '2'
                continue

        print("\n  1. Search by company name")
        print("  2. Enter new entry")
        print("  X. Save and exit\n")
        user_input = input("Select: ")


    print(" Saving and closing")

# helper fn newEntry() collects the values to populate the insertion query.
def newEntry():
    coName = input("Please enter the name of the company: ")
    role = input("For what position: ")
    date = input("today's date (xx/xx/xx): ")
    resume = input("which resume did you use?: ")

    queryBuilder = """INSERT INTO applications VALUES( "%s", "false", "%s", "%s", "%s");""" % (coName, role, date, resume)
    return queryBuilder

main()
connection.commit()  # won't save without this call, DB changes would be lost.
connection.close()
sys.exit(0)
