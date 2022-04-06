CREATE DATABASE IF NOT EXISTS demo;

USE demo;
CREATE TABLE IF NOT EXISTS Friend(
    Name VARCHAR(50),
    PhoneNumber VARCHAR(15)
);
CREATE TABLE IF NOT EXISTS demo(
    id INT PRIMARY KEY,
    name VARCHAR(10)
                 )ENGINE=INNODB DEFAULT CHARACTER SET utf8;
								 
SHOW DATABASES;

CREATE TABLE IF NOT EXISTS demo1(
	id INT auto_increment PRIMARY KEY,
	reg_datetime DATETIME,
	reg_time TIME,
	reg_date DATE,
	reg_year YEAR);

-- INSERT INTO demo1 VALUES (1, '2022-04-03 16:41:30', '16:41:30', '2022-04-03', '2022');

CREATE TABLE IF NOT EXISTS stu(
	id INT PRIMARY KEY,		-- 声明主键
	sname VARCHAR(5) NOT NULL,
	sex INT);
	

CREATE TABLE IF NOT EXISTS demo_new(
	cid INT PRIMARY KEY,
	id INT);


-- ALTER TABLE demo_new ADD CONSTRAINT fk_demo_new FOREIGN KEY(id) REFERENCES demo(id) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE IF NOT EXISTS demo2(
		-- 设定为自增长的列必须设置为主键，并且一张表里只能有一个自增列
		ID INT AUTO_INCREMENT PRIMARY KEY,
		Name VARCHAR(10));

-- INSERT INTO demo2 VALUES(0, 'vip', 'tester1');
-- INSERT INTO demo2(name, vip) VALUES('tester2','vip');	-- 没有指定主键的值会自动增长

CREATE TABLE IF NOT EXISTS demo2(
		-- 设定为自增长的列必须设置为主键，并且一张表里只能有一个自增列
		ID INT AUTO_INCREMENT PRIMARY KEY,	-- 主键约束、自增长约束
		vip VARCHAR(50) UNIQUE NOT NULL,		-- 唯一约束
		Name VARCHAR(10) NOT NULL,					-- 非空约束
		sex SET('男','女'),									-- 检查约束
		payment ENUM('货到付款', '在线支付'));	-- 检查约束
		
-- INSERT INTO demo2 VALUES(0,'VIP1','tester1','男','货到付款');
-- INSERT INTO demo2(vip,name,sex,payment) VALUES ('VIP2','tester2','女','在线支付');
-- INSERT INTO demo2 VALUES (DEFAULT, 'VIP3','tester3','女','在线支付');
-- INSERT INTO demo2 VALUES (DEFAULT(ID), 'VIP4','tester4','女','货到付款');
-- INSERT INTO demo2 VALUES (DEFAULT(ID), 'VIP5','tester5','男','在线支付');

DROP TABLE IF EXISTS demo3;
CREATE TABLE IF NOT EXISTS demo3(
	-- 设定为自增的列必须设置为主键，且一张表里只有一个自增列
	ID INT,
	name VARCHAR(10),
	sex varchar(2));

ALTER TABLE demo3 ADD CONSTRAINT pk_demo3 PRIMARY KEY demo3(ID);
CREATE TABLE IF NOT EXISTS demo4 AS SELECT * FROM demo2;
CREATE TABLE IF NOT EXISTS demo5 LIKE demo4;
ALTER TABLE demo5 RENAME TO	demo6;
ALTER TABLE demo6 RENAME AS demo5;
ALTER TABLE demo5 ADD COLUMN product_name VARCHAR(100);
ALTER TABLE demo5 ADD COLUMN comment VARCHAR(10) NOT NULL; 
ALTER TABLE demo3 CHANGE name sname VARCHAR(20) NOT NULL;
ALTER TABLE demo3 MODIFY sname VARCHAR(10);
ALTER TABLE demo3 MODIFY COLUMN sname VARCHAR(10) DEFAULT 'zhangsan';
ALTER TABLE demo3 MODIFY COLUMN ID INT auto_increment;
ALTER TABLE demo3 MODIFY sex SET('男','女');
ALTER TABLE demo3 CHANGE sname ssname VARCHAR(10) NOT NULL;
ALTER TABLE demo5 DROP product_name;
ALTER TABLE demo5 DROP COLUMN comment;
