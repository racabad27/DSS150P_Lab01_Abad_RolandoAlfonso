import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "dss150p_lab",
    "user": "dss150p",
    "password": "dss150p_lab",
}

def main():
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:

            print("=== Tables in database ===")
            cur.execute("""
                SELECT table_schema, table_name
                FROM information_schema.tables
                WHERE table_schema NOT IN ('pg_catalog', 'information_schema');
            """)
            for row in cur.fetchall():
                print(row)

            print("\n=== Columns in support_tickets ===")
            cur.execute("""
                SELECT column_name, data_type, is_nullable
                FROM information_schema.columns
                WHERE table_name = 'support_tickets'
                ORDER BY ordinal_position;
            """)
            for row in cur.fetchall():
                print(row)

            print("\n=== Row count (support_tickets) ===")
            cur.execute("SELECT COUNT(*) FROM support_tickets;")
            print(cur.fetchone())

            print("\n=== Sample rows (support_tickets) ===")
            cur.execute("SELECT * FROM support_tickets LIMIT 5;")
            for row in cur.fetchall():
                print(row)

            print("\n=== Columns in lab.customers ===")
            cur.execute("""
                SELECT column_name, data_type, is_nullable
                FROM information_schema.columns
                WHERE table_schema = 'lab' AND table_name = 'customers'
                ORDER BY ordinal_position;
            """)
            for row in cur.fetchall():
                print(row)

if __name__ == "__main__":
    main()