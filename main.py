#!/usr/bin/env python3

# Simple python program powered by sqlite3
# to document which organizations I've applied to
# and other relevant information.
# NOTE: the user must first instantiate DB & table:
# the .db should be placed in this directory.
# .schema:
# CREATE TABLE applications(
# company_name VARCHAR(30),
# is_denied BOOLEAN,
# role VARCHAR(20),
# date_applied VARCHAR(8),
# resume_name VARCHAR(20));

import sqlite3
import time  # for sleep() to pause execution
import sys
from datetime import date

connection = sqlite3.connect("applied.db")
cursor = connection.cursor()


def main():
    print("\n\n  ******************************************************")
    print("  ********************** Welcome ***********************")
    print("  This is your local Applied DB where you can search for")
    print("  and/or add organizations to which you've applied.")
    print("  (Don't forget to save your changes!)")
    print("\n    1. Search by company name")
    print("    2. New submission")
    print("    3. Application denied")
    print("    4. Show all pending applications")
    print("    5. Show today's submissions")
    print("    6. Number of applications so far")
    print("    X. Save and exit\n")

    user_input = input("\nYour selection: ")

    while user_input != 'X' and user_input != 'x':
        if user_input == '1':
            co_name = input(" What's the company's name? ")
            selectCmd = """SELECT * FROM applications WHERE company_name IS "%s" ;""" % co_name
            try:
                cursor.execute(selectCmd)
                print(cursor.fetchall()[0])  # returns a tuple in a list
            except:
                print(co_name + " not in database, yet.")

        elif user_input == '2':
            insertCmd = newEntry()
            cursor.execute(insertCmd)

        elif user_input == '3':
            deniedCmd = denied()
            cursor.execute(deniedCmd)

        elif user_input == '4':
            showCmd = queryAll()
            if showCmd is not None:
                cursor.execute(showCmd)
                print('\n{:12s}     {:30s}       {}'.format("Company Name", "Position", "Date submitted\n"))
                for count, row in enumerate(cursor):
                    print(str(count + 1) + '.  {:12s} --- {:30s} ----- {}'.format(row[0], row[2], row[3]))
        elif user_input == '5':
            today = date.today().strftime('%m/%d/%y')
            query = """SELECT * FROM applications WHERE is_denied = "false" AND date_applied = '%s' ;""" % today
            cursor.execute(query)
            for count, row in enumerate(cursor):
                print(str(count + 1) + '.  {:12s} --- {:30s} ----- {}'.format(row[0], row[2], row[3]))

        elif user_input == '6':
            query = """SELECT * FROM applications;"""
            results = cursor.execute(query)
            print("   You've submitted " + str(len(results.fetchall())) + " applications in total!")

        print('\n  ..Going back to the main menu..')
        time.sleep(2)
        print("\n  1. Search by company name")
        print("  2. New submission")
        print("  3. Application denied")
        print("  4. Show all pending applications")
        print("  5. Show today's submissions")
        print("  6. Number of applications so far")
        print("  X. Save and exit\n")
        user_input = input("\nSelection: ")
    print(" Saving and closing")


def newEntry():
    co_name = input("Please enter the name of the company: ")
    role = input("For what position?: ")
    date = input("today's date (xx/xx/xx): ")
    resume = input("which resume did you use?: ")

    queryBuilder = """INSERT INTO applications VALUES( "%s", "false", "%s", "%s", "%s");""" % (
        co_name, role, date, resume)
    return queryBuilder


def denied():
    co_name = input("Enter the name of the company: ")
    queryBuilder = """UPDATE applications SET is_denied = "true" WHERE company_name = "%s"; """ % (
        co_name)
    return queryBuilder


def queryAll():
    print("\n 1. Order by company name")
    print(" 2. Order by date")
    print(" R  Return")

    user_input = input("Select: ")
    while user_input != 'R' and user_input != 'r':
        if user_input == '1':
            queryBuilder = """SELECT * FROM applications WHERE is_denied IS "false" ORDER BY company_name;"""
            return queryBuilder

        elif user_input == '2':
            queryBuilder = """SELECT * FROM applications WHERE is_denied IS "false" ORDER BY date_applied;"""
            return queryBuilder

        print("\n 1. Order by company name")
        print(" 2. Order by date")
        print(" R  Return")
        user_input = input("Select: ")

    print("\n Aight then..")
    time.sleep(1)
    return


main()
connection.commit()  # won't save without this call, DB changes would be lost.
connection.close()
sys.exit(0)
