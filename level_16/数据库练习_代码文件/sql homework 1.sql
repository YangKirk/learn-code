-- 练习题1 编写一条CREATE TABLE 语句，用来创建一个包含下表中所列各项的表Addressbook(地址簿)，并为regist_no（注册编号）列设置主键约束。
-- 列的含义		|		列的名称		|		数据类型									|		约束				 |
-- 注册编号		|		regist_no		|		整数型										|不能为NULL、主键|
-- 姓名				|		name				|	可变长字符串类型(长度为128) |不能为NULL			 |
-- 住址				| 	address			| 可变长字符串类型(长度为256)	|不能为NULL			 |
-- 电话号码		| 	tel_no			| 定长字符串类型(长度为10)		| 							 |
-- 邮箱地址		|		mail_address| 定长字符串类型(长度为20)		| 							 |

USE demo;
CREATE TABLE IF NOT EXISTS Addressbook(
	regist_no INT NOT NULL PRIMARY KEY,
	name VARCHAR(128) NOT NULL,
	address VARCHAR(256) NOT NULL,
	tel_no CHAR(10),
	mail_address char(20)) ENGINE=INNODB DEFAULT CHARACTER SET utf8;

-- 练习题2:假设在创建练习题1中的Addressbook表时忘记添加如下一列postal_code(邮政编码)了，请把此列添加到表中。 
-- 列名：postal_code \ 数据类型： 定长字符串类型(长度为8) \ 约束：不能为NULL
ALTER TABLE Addressbook ADD COLUMN postal_code CHAR(8) NOT NULL;


-- 练习题3：编写SQL语句删除Addressbook表
DROP TABLE Addressbook;