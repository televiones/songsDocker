create database if not exists songs;

CREATE USER if not exists 'televiones'@'localhost' IDENTIFIED BY 'televiones';
GRANT ALL PRIVILEGES ON * . * TO 'televiones'@'localhost';
FLUSH PRIVILEGES;

use songs;

CREATE TABLE artist(
	id int not null auto_increment, #por defecto empieza en 1
	name VARCHAR(100) not null,
    primary key(id)
);

CREATE TABLE song (
	id int NOT NULL auto_increment,
    name VARCHAR(50) not null,
    artist_id int not null,
    released_in year,
    primary key(id),
    foreign key(artist_id) references artist(id) on delete cascade
);

insert into artist (name) values ('Ed Sheeran'), ('Harry Styles'), ('Beyoncé');

insert into song values (0, 'Late Night Talking', 2, 2022),  (0, 'As It Was', 2, 2022), (0, 'ALIEN SUPERSTAR', 3, 2022), (0, 'Dont', 1, 2014), (0, 'Castle on the Hill', 1, 2017);
