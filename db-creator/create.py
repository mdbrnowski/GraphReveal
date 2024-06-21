#!/usr/bin/env python3

import sqlite3

con = sqlite3.connect("graphs.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS graphs")

cur.execute(""" CREATE TABLE graphs (
                    id VARCHAR(20) PRIMARY KEY,
                    vertices INT NOT NULL,
                    edges INT NOT NULL,
                    connected BOOLEAN NOT NULL,
                    acyclic BOOLEAN NOT NULL
                )
            """)

con.close()
