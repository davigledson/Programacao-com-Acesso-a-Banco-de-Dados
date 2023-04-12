CREATE DATABASE lanchonete;

CREATE TABLE Cardapio
(
codigo INT PRIMARY KEY AUTO_INCREMENT,
prato VARCHAR(100),
preco FLOAT
);

INSERT INTO Cardapio
VALUES (NULL,"Suco de laranja",1),
(NULL,"Coxinha",3.80),
(NULL,"Pastel",2.90),
(NULL,"Vitamina de banana",6.30),
(NULL,"Hamburguer",8.70),
(NULL,"Torrada",5.50),
(NULL,"Pudim",7.65),
(NULL,"Refrigerante em Lata",4.25);

SELECT * FROM Cardapio;

SELECT prato,preco FROM Cardapio ORDER BY preco ASC;

SELECT * FROM Cardapio ORDER BY preco DESC;

UPDATE Cardapio SET preco = 5.30 WHERE prato ="Vitamina de banana";

UPDATE Cardapio SET preco = 5.30, prato ="Pudim de leite" WHERE codigo = 7;

INSERT INTO Cardapio
VALUES (NULL,"Pastel",4);

DELETE FROM Cardapio WHERE prato = "pastel";

DELETE FROM Cardapio WHERE codigo IN(2,5);