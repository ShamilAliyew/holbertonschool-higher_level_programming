-- a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
-- a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(
    id int not null auto_increment primary key,
    state_id int not null FOREIGN KEY (state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);