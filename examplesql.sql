create database postgres

create role user11 LOGIN;

grant all privileges on database postgres to user11;

-- Creating the table
create table players
(
    id    int,
    name  varchar(255) not null,
    score  numeric not null
);


-- Adding data to our table
insert into players (id, name, score)
values (1, 'student1', 0);

insert into players (id, name, score)
values (2, 'student2', 0),
       (3, 'student3',  0),
       (4, 'student4',  0),
	   (5, 'student5',  0),
       (6, 'student6',  0);
