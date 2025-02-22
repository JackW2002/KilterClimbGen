import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('db/kilterklimbs.db')
cursor = conn.cursor()

# Define the SQL query to join placements and holes where layout_id = 1
query = """
SELECT p.id, h.x, h.y
FROM placements p
JOIN holes h ON p.hole_id = h.id
WHERE p.layout_id = 1;
"""

# Execute the query
cursor.execute(query)

# Fetch all results from the query
results = cursor.fetchall()

# Process or print the results
for placement_id, x, y in results:
    print(f"Placement ID: {placement_id}, x: {x}, y: {y}")

# Optionally, if you want to save the results to a new table called 'placements_positions'
create_table_query = """
CREATE TABLE IF NOT EXISTS placements_positions AS
SELECT p.id AS placement_id, h.x, h.y
FROM placements p
JOIN holes h ON p.hole_id = h.id
WHERE p.layout_id = 1;
"""
cursor.execute(create_table_query)
conn.commit()

# Clean up by closing the connection
cursor.close()
conn.close()
