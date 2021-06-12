import sqlite3

conn = sqlite3.connect('myquotes.db')
curr = conn.cursor()

# curr.execute("""create table quotes_table(
#                 title text,
#                 author text,
#                 tag text)
#                 """)
curr.execute("""
                insert into quotes_table values(
                'Python is a great language',
                'Author-Python',
                'tab-python')""")
conn.commit()
conn.close()
