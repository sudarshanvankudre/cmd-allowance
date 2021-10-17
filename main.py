import sqlite3
import datetime

con = sqlite3.connect("allowance.db")
creation_sql = """CREATE TABLE IF NOT EXISTS transactions(
                                                        id INTEGER PRIMARY KEY,
                                                        subject TEXT,
                                                        value REAL,
                                                        ts
                                                        );"""
con.execute(creation_sql)
con.commit()

ALLOWED_CMDS = ["new", "list", "allowance", "update", "bulk"]

def is_valid(cmd):
    return len(cmd) > 0 and cmd[0] in ALLOWED_CMDS

def run_command(cmd):
    if cmd[0] == "new":
        con.execute("INSERT INTO transactions VALUES (?, ?, ?, ?)", (None, cmd[1], cmd[2], datetime.datetime.now()))
    elif cmd[0] == "list":
        for row in con.execute("SELECT * FROM transactions"):
            print(row)
    elif cmd[0] == "allowance": 
        print(con.execute("SELECT SUM(value) FROM transactions").fetchone()[2])
    elif cmd[0] == "update":
        print("Update not implemented yet")
    elif cmd[0] == "bulk":
        print("Bulk insert not implemented yet")
    con.commit()

        
def main():
    while True:
        command = input('--> ').split()
        if is_valid(command):
            run_command(command)
        else:
            print("Invalid command")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        con.rollback()
        con.close()
        raise KeyboardInterrupt
 







