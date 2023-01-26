-- @block
SELECT * from predmety
ORDER BY id ASC;

-- @block
SELECT predmety.nazov AS predmet,poznamky.nazov AS nazov,poznamky.poznamky FROM predmety
INNER JOIN poznamky
ON poznamky.predmet = predmety.id
ORDER BY id ASC

-- @block
CREATE TABLE ulohy(
    predmet INT,
    zadanie VARCHAR(255),
    deadline DATE,
    FOREIGN KEY (predmet) REFERENCES predmety(id)
)
-- @block
INSERT INTO ulohy(predmet,zadanie,deadline)
VALUES 
    (6,'12/19','2024-01-20')
;
-- @block
SELECT predmety.nazov,ulohy.zadanie,ulohy.deadline FROM predmety
INNER JOIN ulohy
ON ulohy.predmet = predmety.id
ORDER BY deadline ASC
;
-- @block
CREATE TABLE users(
    username VARCHAR(30),
    passwrd VARCHAR(30)
);
-- @block
INSERT INTO users(username,passwrd)
VALUES 
    ('saminko','123')
;

-- @block
SELECT * FROM users;

-- @block
DELETE FROM poznamky WHERE predmet = 1 OR predmet = 2;