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
    CONTENT VARCHAR(300)
);
alter table routine add ROUTINE_KEY INT primary key;
alter table routine modify ROUTINE_KEY INT FIRST;
alter table routine modify ROUTINE_KEY int not null auto_increment;
INSERT INTO USER VALUES("ROOT", "ROOT", "ROOOT");