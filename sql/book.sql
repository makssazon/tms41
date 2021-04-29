--coment
/*
	Создать файл book.sql. Создать таблицу Book. Атрибуты: 
	id(integer primary key autoincrement), 
	title(varchar), pages(int), 
	author(varchar), price(float)
*/

CREATE TABLE Book (
	id integer primary key autoincrement, 
	title varchar,
	pages int,
	author varchar,
	price float
	
);

ALTER TABLE book ADD COLUMN release_year int;