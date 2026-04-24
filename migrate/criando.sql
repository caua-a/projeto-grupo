create database db_loja;
use db_loja;
create table produtos(
	codigo int primary key auto_increment,
    produto varchar(40) not null unique, 
    descricao varchar(100) not null,
    preco DECIMAL(10,2) not null,
    destaque bool not null default (1), 
    foto varchar(500) not null,
    disponibilidade bool default(1)
);

create table usuarios(
	usuario int primary key auto_increment,
	nome varchar (300) not null unique,
    senha varchar (300) not null
);

create table carrinhos(
	cod_carrinho int auto_increment primary key,
    usuario INT NOT NULL,
    data datetime default current_timestamp,
    finalizado bool default false,
    CONSTRAINT fk_carrinho_usuario FOREIGN KEY (usuario) REFERENCES usuarios(usuario)
);


CREATE TABLE itens_carrinho (
	cod_itens int auto_increment primary key,
    id_produto INT NOT NULL,
    cod_carrinho int,
    quantidade int default 1,
    constraint fk_carrinho_itens foreign key (cod_carrinho) references carrinhos(cod_carrinho),
    CONSTRAINT fk_produtos_carrinho FOREIGN KEY (id_produto) REFERENCES produtos(codigo)
);

    
    
    

insert into produtos(produto, descricao, preco, destaque, foto, disponibilidade) 
values("Lanche Python", "Muito bom e cheio de codigos", 49.90, 1, "https://blog.zanottirefrigeracao.com.br/wp-content/uploads/2017/09/lanche-na-chapa-1024x768.jpg", 1);