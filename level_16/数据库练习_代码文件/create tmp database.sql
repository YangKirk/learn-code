-- tmp数据库建立
CREATE DATABASE tmp;
USE tmp;

-- dept表建立
CREATE TABLE dept (
	deptno INT ( 2 ) NOT NULL,
	dname VARCHAR ( 14 ),
	loc VARCHAR ( 13 ),
	CONSTRAINT pk_dept PRIMARY KEY ( deptno ) 
) ENGINE = INNODB DEFAULT CHARACTER 
SET utf8;
INSERT INTO dept
VALUES
	( 10, 'ACCOUNTING', 'NEW YORK' );
INSERT INTO dept
VALUES
	( 20, 'RESEARCH', 'DALLAS' );
INSERT INTO dept
VALUES
	( 30, 'SALES', 'CHICAGO' );
INSERT INTO dept
VALUES
	( 40, 'OPERATIONS', 'BOSTON' );

-- emp表建立
CREATE TABLE emp (
	empno INT ( 4 ) NOT NULL PRIMARY KEY,
	ename VARCHAR ( 10 ),
	job VARCHAR ( 9 ),
	mgr INT ( 4 ),
	hiredate DATE,
	sal FLOAT ( 7, 2 ),
	comm FLOAT ( 7, 2 ),
	deptno INT ( 2 ),
	CONSTRAINT fk_deptno FOREIGN KEY ( deptno ) REFERENCES dept ( deptno ) 
) ENGINE = INNODB DEFAULT CHARACTER 
SET utf8;
INSERT INTO emp
VALUES
	( 7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800, NULL, 20 );
INSERT INTO emp
VALUES
	( 7499, 'ALLEN', 'SALLSMAN', 7698, '1981-02-20', 1600, 300, 30 );
INSERT INTO emp
VALUES
	( 7521, 'WARD', 'SALESMAN', 7698, '1981-02-22', 1250, 500, 30 );
INSERT INTO emp
VALUES
	( 7566, 'JONES', 'MANAGER', 7839, '1981-04-02', 2975, NULL, 20 );
INSERT INTO emp
VALUES
	( 7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28', 1250, 1400, 30 );
INSERT INTO emp
VALUES
	( 7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01', 2850, NULL, 30 );
INSERT INTO emp
VALUES
	( 7782, 'CLARK', 'MANAGER', 7839, '1981-06-09', 2450, NULL, 10 );
INSERT INTO emp
VALUES
	( 7788, 'SCOTT', 'ANALYST', 7566, '1987-07-13', 3000, NULL, 20 );
INSERT INTO emp
VALUES
	( 7839, 'KING', 'PRESIDENT', NULL, '1981-11-07', 5000, NULL, 10 );
INSERT INTO emp
VALUES
	( 7844, 'TURMER', 'SALESMAN', 7698, '1981-09-08', 1500, 0, 30 );
INSERT INTO emp
VALUES
	( 7876, 'ADAMS', 'CLERK', 7788, '1987-07-13', 1100, NULL, 20 );
INSERT INTO emp
VALUES
	( 7900, 'JAMES', 'CLERK', 7698, '1981-12-03', 950, NULL, 30 );
INSERT INTO emp
VALUES
	( 7902, 'FORD', 'ANALYST', 7566, '1981-12-03', 3000, NULL, 20 );
INSERT INTO emp
VALUES
	( 7934, 'MILLER', 'CLERK', 7782, '1982-01-23', 1300, NULL, 10 );

-- bonus表建立
CREATE TABLE bonus ( ename VARCHAR ( 10 ), job VARCHAR ( 9 ), sal INT, comm INT ) ENGINE = INNODB DEFAULT CHARACTER 
SET utf8;

-- salgrade表建立
CREATE TABLE salgrade ( grade INT, losal INT, hisal INT ) ENGINE = INNODB DEFAULT CHARACTER 
SET utf8;
INSERT INTO salgrade
VALUES
	( 1, 700, 1200 );
INSERT INTO salgrade
VALUES
	( 2, 1201, 1400 );
INSERT INTO salgrade
VALUES
	( 3, 1401, 2000 );
INSERT INTO salgrade
VALUES
	( 4, 2001, 3000 );
INSERT INTO salgrade
VALUES
	( 5, 3001, 9999 );

-- DROP DATABASE tmp;