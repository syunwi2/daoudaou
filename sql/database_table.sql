USE DAOUDAOU;

CREATE TABLE USER(
	EMAIL VARCHAR(100),
	NAME VARCHAR(10),
    PASSWORD VARCHAR(20)
);
alter table USER modify EMAIL VARCHAR(100) primary key;
alter table USER modify EMAIL VARCHAR(100) FIRST;

CREATE TABLE EVENT(
    EMAIL VARCHAR(100),
    DATETIME DATETIME,
    TITLE VARCHAR(50),
    CONTENT VARCHAR(300)
);
alter table EVENT add EVENT_KEY INT primary key;
alter table EVENT modify EVENT_KEY INT FIRST;
alter table EVENT modify EVENT_KEY int not null auto_increment;

CREATE TABLE ROUTINE(
    EMAIL VARCHAR(100),
    DAY INT,
    TITLE VARCHAR(50),
    CONTENT VARCHAR(300),
    TIME TIME
);
alter table routine add ROUTINE_KEY INT primary key;
alter table routine modify ROUTINE_KEY INT FIRST;
alter table routine modify ROUTINE_KEY int not null auto_increment;

INSERT INTO USER VALUES("syunwi2@gmail.com", "root", "root");
INSERT INTO EVENT VALUES(1, "syunwi2@gmail.com", '2023-01-28 21:00:00', "TEST", "TEST EVENT CONTENT");
INSERT INTO ROUTINE VALUES(1, "syunwi2@gmail.com", 1, "TEST", "TEST ROUTINE CONTENT", "21:00:00");