-- 1.编写一.存储过程，该存储过程只接受一个部门编号作为参数，可以求出该部门的员工总数。
USE tmp;
CREATE PROCEDURE get_count_dept(IN _deptno INT, OUT _count_dept INT)
BEGIN
	SELECT COUNT(*) FROM emp WHERE deptno = _deptno;
END;

CALL get_count_dept(10, @emptotal);
SELECT @emptotal;

-- 2.利用sql复制一份emp表，生成一个名叫emp1的表
USE tmp;
CREATE TABLE IF NOT EXISTS emp1 AS (SELECT * FROM emp);


-- 3.在emp1上建立一个触发器，要求在更新emp1数据时，如果该记录的comm为null，则更新后自动变成0，如果该记录的comm小于sal，则更新后comm等于sal。
CREATE TRIGGER emp1_trigger BEFORE UPDATE ON emp1 FOR EACH ROW
BEGIN
	IF old.comm IS NULL THEN
			SET new.comm = 0;
	ELSEIF old.comm < old.sal THEN
			SET new.comm = new.sal;
	END IF;
END


SHOW CREATE TABLE emp1;