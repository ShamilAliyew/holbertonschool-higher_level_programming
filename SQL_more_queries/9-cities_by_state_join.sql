-- a script that lists all cities contained in the database hbtn_0d_usa
-- a script that lists all cities contained in the database hbtn_0d_usa
SELECT
    C.ID,
    C.NAME,
    S.NAME
FROM cities C
JOIN states S ON C.state_id = S.id;