import duckdb

con = duckdb.connect(database='/data/intalgo.duckdb', read_only=False)

con.execute("CREATE OR REPLACE TABLE ORGS AS SELECT * FROM 'src/example/organizations-10000.csv'")

con.execute("CREATE OR REPLACE TABLE PEEPS AS SELECT * FROM 'src/example/people-10000.csv'")


