import sqlite3
import datetime

con = sqlite3.connect("allowance.db")
creation_sql = """CREATE TABLE IF NOT EXISTS transactions(
                                                        id INTEGER PRIMARY KEY,
                                                        subject TEXT,
                                                        amount REAL,
                                                        ts
                                                        );"""
con.execute(creation_sql)
con.commit()

ALLOWED_CMDS = ["new", "list", "allowance", "update", "bulk"]

def is_valid(cmd):
    return len(cmd) > 0 and cmd[0] in ALLOWED_CMDS

def run_update(update_args):
    id = update_args[0]
    subject = None
    amount = None
    if "-subject" in update_args:
        subject = update_args[update_args.index("-subject") + 1]
    if "-amount" in update_args:
        amount = update_args[update_args.index("-amount") + 1]
    original_row = con.execute("SELECT * FROM transactions WHERE id = ?", (id)).fetchone()
    if subject and amount:
        con.execute("UPDATE transactions SET subject = ?, amount = ? WHERE id = ?", (subject, amount, id))
    elif subject:
        con.execute("UPDATE transactions SET subject = ? WHERE id = ?", (subject, id))
    elif amount:
        con.execute("UPDATE transactions SET amount = ? WHERE id = ?", (amount, id))
    else:
        print("No values given to update")
    new_row = con.execute("SELECT * FROM transactions WHERE id = ?", (id)).fetchone()
    print("{} --> {}".format(original_row, new_row))


def run_command(cmd):
    if cmd[0] == "new":
        con.execute("INSERT INTO transactions VALUES (?, ?, ?, ?)", (None, cmd[1], cmd[2], datetime.datetime.now()))
    elif cmd[0] == "list":
        for row in con.execute("SELECT * FROM transactions"):
            print(row)
    elif cmd[0] == "allowance": 
        allowance = con.execute("SELECT SUM(amount) FROM transactions").fetchone()[0]
        if allowance:
            print(allowance)
        else:
            print(0)
    elif cmd[0] == "update":
        run_update(cmd[1:])
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
    except Exception:
        con.rollback()
        con.close()
        raise Exception

 







