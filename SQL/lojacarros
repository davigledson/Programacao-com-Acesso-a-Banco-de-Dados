CREATE DATABASE lojacarros;

USE lojacarros;

CREATE TABLE carros(
codigo INT PRIMARY KEY AUTO_INCREMENT,
fabricante VARCHAR(100),
modelo VARCHAR(100),
preco FLOAT
);

INSERT INTO carros
VALUES (1, "Fiat", "Mobi", 68990);

INSERT INTO carros
VALUES(NULL, "Fiat", "Pulse", 98990);

INSERT INTO carros
VALUES(5, "Fiat", "Strada", 103990);

INSERT INTO carros
VALUES(NULL, "Fiat", "Toro", 146990);

INSERT INTO carros
VALUES (3, "VW", "Gol", 55760),
(4, "VW", "Polo", 80580),
(7,"VW", "Nivus", 125890);

## CONSULTA SIMPLES ###################
SELECT * FROM carros;

## CONSULTA COLUNAS ESCOLHIDAS ########
SELECT modelo, preco FROM carros;

## ORDENANDO OS REGISTROS ############
SELECT * FROM carros
ORDER BY preco;

SELECT * FROM carros
ORDER BY modelo;

## ORDENAÇÃO POR VÁRIAS COLUNAS #####
SELECT * FROM carros
ORDER BY fabricante, modelo;

## ORDENAÇÃO DECRESCENTE #########
SELECT modelo, preco FROM carros
ORDER BY preco DESC;

## CONSULTA COM CONDIÇÃO (FILTRA LINHAS) ##
SELECT * FROM carros
WHERE fabricante = "vw";

SELECT * FROM carros
WHERE preco < 100000;

# <  menor que,       > maior que
# <= menor ou igual,  >= maior ou igual
# =  igual,           <> != diferente

## CONDIÇÃO MÚLTIPLA (E/AND) ############
# Carros da Fiat abaixo de 100 mil
SELECT * FROM carros
WHERE fabricante = "fiat"
AND   preco < 100000;

## CONDIÇÃO MÚLTIPLA (OU/OR) ##########
SELECT * FROM carros
WHERE modelo = "gol" OR modelo = "mobi";


## ATUALIZAR INFORMAÇÕES EXISTENTES ######
UPDATE carros              #qual tabela
SET preco = 62490          #qual coluna
WHERE codigo = 1;          #qual linha

UPDATE carros
SET modelo = "Gol Last"
WHERE codigo = 3;

## Atualizar várias COLUNAS #############
UPDATE carros
SET modelo = "Nivus 2024", preco = 132990
WHERE codigo = 7;

## Atualizar várias LINHAS (CUIDAAAAAADOOO)
UPDATE carros
SET preco = preco * 1.05
WHERE fabricante = "VW";

## Atualizar vários CÓDIGOS de uma vez ###
UPDATE carros
SET preco = preco * 0.95
WHERE codigo IN (1, 6);

## EXCLUSÃO DE REGISTROS #################

INSERT INTO carros
VALUES (NULL,"Hyundai","HB20", 89990);

DELETE FROM carros
WHERE codigo = 8;

DELETE FROM carros
WHERE fabricante = "Hyundai";

DELETE FROM carros
WHERE codigo IN (11, 13, 14);
