-- 定义变量
SET @nametest=666;
SELECT @nametest;

USE tmp;
SELECT @maxsal:=MAX(sal) FROM emp;
SELECT MAX(sal) INTO @maxsal FROM emp;

-- 查询变量
SELECT @maxsal;
SELECT ename, sal FROM emp WHERE sal=@maxsal;

-- 存储过程
USE tmp;
DROP PROCEDURE IF EXISTS get_maxsal;

DELIMITER //
	CREATE PROCEDURE get_maxsal()
		BEGIN
			SELECT MAX(sal) FROM emp;
		END //
DELIMITER;

CALL get_maxsal();

-- 在存储过程中声明使用变量
DROP PROCEDURE IF EXISTS get_sal;
DELIMITER //
CREATE PROCEDURE get_sal()
	BEGIN
		DECLARE avgsal INT;
		SELECT AVG(sal) INTO avgsal FROM emp;
		SELECT ename, sal FROM emp WHERE sal > avgsal;
	END //

DELIMITER ;

CALL get_sal();

-- 带参数的存储过程
DROP PROCEDURE IF EXISTS get_sal_1;
DELIMITER //
CREATE PROCEDURE get_sal_1(IN empname VARCHAR(5), OUT empsal INT)
	BEGIN
		SELECT sal INTO empsal FROM emp WHERE ename=empname;
	END //

CALL get_sal_1('BLAKE', @_empsal);
SELECT @_empsal;

-- IF
DROP PROCEDURE IF EXISTS get_sal_level;
DELIMITER //
CREATE PROCEDURE get_sal_level(IN empname VARCHAR(5), OUT sallevel VARCHAR(10))
	BEGIN
		DECLARE empsal INT;
		SELECT sal INTO empsal FROM emp WHERE ename=empname;
		IF empsal > 3000 THEN
			SET sallevel = 'high';
		ELSEIF empsal <= 3000 AND empsal >2000 THEN
			SET sallevel = 'middle';
		ELSE
			SET sallevel = 'low';
		END IF;
	END //

CALL get_sal_level('BLAKE', @_sallevel);
SELECT @_sallevel;

-- CASE
CREATE PROCEDURE p()
	BEGIN
		DECLARE v INT DEFAULT 1;
		CASE v
			WHEN 2 THEN SELECT v;
			WHEN 3 THEN SELECT 0;
		ELSE
			SELECT 'hello';
		END CASE;
	END;



-- REPEAT
DROP PROCEDURE IF EXISTS dorepeat;
CREATE PROCEDURE dorepeat(IN b INT, IN e INT)
	BEGIN
		DECLARE total INT DEFAULT 0;
		DECLARE temp INT DEFAULT b;
		REPEAT
			SET total = total + temp;
			SET temp = temp + 1;
		UNTIL temp > e
		END REPEAT;
		SELECT total;
	END;

CALL dorepeat(1,10);

-- while
DROP PROCEDURE IF EXISTS dowhile;
CREATE PROCEDURE dowhile()
BEGIN
	DECLARE v1 INT DEFAULT 5;
	WHILE v1 > 0 DO
		SELECT v1;
		SET v1=v1-1;
	END WHILE;
END;

CALL dowhile();

-- 跳出循环和继续循环 LEAVE & ITERATE
DROP PROCEDURE IF EXISTS test_iterate;
DELIMITER //
CREATE PROCEDURE test_iterate(IN p INT)
BEGIN
	outw: WHILE TRUE DO
		SET p=p+1;
		IF p <=5 THEN
			ITERATE outw;
		ELSEIF p>=10 THEN
			LEAVE outw;
		END IF;
	END WHILE outw;
	SELECT p;
END //

SET @a=2;
CALL test_iterate(@a);

DROP PROCEDURE IF EXISTS proc_repeattest;
DELIMITER //
CREATE PROCEDURE proc_repeattest()
BEGIN
	DECLARE num INT DEFAULT 6;
	outtest: REPEAT
		SET num=num-1;
		IF num = 4 THEN
			ITERATE outtest;
		ELSEIF num=2 THEN
			LEAVE outtest;
		END IF;
		SELECT num;
	UNTIL num < 1
	END REPEAT outtest;
END //

CALL proc_repeattest();


-- 删除触发器
DROP TRIGGER IF EXISTS trigger_name;

-- 查看触发器
SHOW TRIGGERS;

-- 创建触发器
CREATE TRIGGER tri_comm BEFORE INSERT ON emp1 FOR EACH ROW	-- 当向emp1表中插入数据时触发
BEGIN
	IF new.comm > new.sal THEN	-- 如果新的comm > 新的sal
		SET new.comm = new.sal;	-- 让新的comm = 新的sal
	END IF;
END;

CREATE TRIGGER tri_comm1 BEFORE DELETE ON dept FOR EACH ROW
BEGIN
	IF old.deptno <> 40 THEN
		SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = '不能删除还有员工的部门信息'; -- 必须写在同一行上
	END IF;
END;

DELETE FROM dept WHERE deptno=30;

-- 事务
-- START TRANSACTION;	-- 开始事务
BEGIN;
INSERT INTO dept VALUES(50, 'TEST', 'CHINA');
INSERT INTO dept VALUES(60, 'JAVA', 'CHENGDU');
ROLLBACK;		-- 回滚事务
-- COMMIT;	-- 提交事务