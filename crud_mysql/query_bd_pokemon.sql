#create database bd_pokedex;

#use bd_pokedex;

/*
create table pokemons(
	id int auto_increment,
    nome_pokemon varchar(30) not null,
	id_pokemon int(4) not null,
    tipo_pokemon varchar(20) not null,
    altura_pokemon float,
    peso_pokemon float,
	primary key(id)
);
*/
select * from pokemons;

#update pokemons set id_pokemon = 0041 where id = 7
