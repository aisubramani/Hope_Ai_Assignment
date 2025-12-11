GRANT SELECT, INSERT ON students TO 'subramani'@'localhost';
REVOKE SELECT, INSERT ON students FROM 'subramani'@'localhost';
GRANT ALL PRIVILEGES ON students TO 'subramani'@'localhost';
REVOKE ALL PRIVILEGES ON students FROM 'subramani'@'localhost';
FLUSH PRIVILEGES;