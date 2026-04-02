create database db_loja;
use db_loja;
create table produtos(
	codigo int primary key auto_increment,
    produto varchar(40) not null unique, 
    descricao varchar(100) not null,
    preco DECIMAL(10,2) not null,
    destaque bool not null, 
    foto varchar(500) not null,
    disponibilidade int not null
);

insert into produtos(produto, descricao, preco, destaque, foto, disponibilidade) 
values("Lanche Python", "Muito bom e cheio de codigos", 49.90, 1, "https://blog.zanottirefrigeracao.com.br/wp-content/uploads/2017/09/lanche-na-chapa-1024x768.jpg", 100);