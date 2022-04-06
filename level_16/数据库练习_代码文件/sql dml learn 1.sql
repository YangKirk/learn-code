USE demo;
CREATE TABLE IF NOT EXISTS Students(
	SCode INT auto_increment PRIMARY KEY,
	SName VARCHAR(10) NOT NULL,
	SAddress VARCHAR(10) NOT NULL,
	SGrade INT,
	SEmail VARCHAR(20),
	SSex INT);

INSERT INTO Students(SName, SAddress, SGrade, SEmail, SSex) VALUES ('张三', '上海松江',6,'ZS@Sohu.com', 0);



UPDATE Students SET SAddress = '重庆' WHERE SAddress = '上海松江';

UPDATE Students SET SGrade = SGrade + 5 WHERE SGrade <= 10;


DELETE FROM Students;
ROLLBACK;

TRUNCATE TABLE Students;

DROP TABLE Students;


