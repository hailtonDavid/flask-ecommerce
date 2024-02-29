drop table if exists marcas;

create table marcas (
  id          int(11)     not null auto_increment,
  nome        varchar(80) default '' UNIQUE,
  apelido     varchar(30) default '' UNIQUE,
  primary key  (id)
)engine=innodb;