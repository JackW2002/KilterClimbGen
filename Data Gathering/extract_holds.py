import sqlite3

conn = sqlite3.connect('db/kilterklimbs')
cursor = conn.cursor()

query = """
SELECT p.id, h.x, h.y
FROM placements p
JOIN holes h ON p.hole_id = h.id
WHERE p.layout_id = 1;
"""

cursor.execute(query)

results = cursor.fetchall()

for placement_id, x, y in results:
    print(f"Placement ID: {placement_id}, x: {x}, y: {y}")

create_table_query = """
CREATE TABLE IF NOT EXISTS placements_positions_filtered AS
SELECT p.id AS placement_id, h.x, h.y
FROM placements p
JOIN holes h ON p.hole_id = h.id
WHERE p.layout_id = 1
  AND h.x > 3
  AND h.x < 141;
"""
cursor.execute(create_table_query)
conn.commit()

cursor.close()
conn.close()
