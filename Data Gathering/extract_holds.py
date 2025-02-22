import sqlite3
import pandas as pd
import os

current_dir = os.path.dirname(__file__)

db_path = os.path.join(current_dir, "..", "db/kilterklimbs")

conn = sqlite3.connect(os.path.abspath(db_path))

# Define the SQL query
query = """
SELECT c.*, cc.*
FROM climbs c
JOIN climb_cache_fields cc ON c.uuid = cc.climb_uuid
WHERE c.layout_id = 1;
"""

df = pd.read_sql_query(query, conn)

csv_path = os.path.join(current_dir, "..", "Data/climbs_export.csv")

df.to_csv(os.path.abspath(csv_path), index=False)

conn.close()

print("Data exported successfully to climbs_export.csv")
