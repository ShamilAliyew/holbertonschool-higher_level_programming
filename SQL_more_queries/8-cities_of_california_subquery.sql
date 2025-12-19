-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa
USE hbtn_0d_usa;
SELECT *
FROM hbtn_0d_usa.cities c
    WHERE c.state_id = (SELECT s.id
                        FROM hbtn_0d_usa.states s WHERE s.name = "California");