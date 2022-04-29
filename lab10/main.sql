create database phonebook
create table PhoneBook_from_csv(
	USERNAME varchar(255),
	NUMBER int not null
)

COPY PhoneBook_from_csv from '\Users\STARLINECOMP.KZ\Documents\example.csv' delimiter ',' csv header;
create table PhoneBookK(
	name varchar,
	number numeric
)
