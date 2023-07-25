-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 25/07/2023 às 06:21
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `lojaroupa`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `roupas`
--

CREATE TABLE `roupas` (
  `codigo` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `tipoVestimenta` varchar(255) DEFAULT NULL,
  `quantidade` int(11) NOT NULL,
  `preco` float NOT NULL,
  `detalhes` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `roupas`
--

INSERT INTO `roupas` (`codigo`, `nome`, `tipoVestimenta`, `quantidade`, `preco`, `detalhes`) VALUES
(1, 'camisa', 'masculinha', 30, 12, 'camisa oficial do manoel gomes'),
(2, 'calcas', NULL, 0, 90, NULL),
(3, 'sapato', 'Unisex', 30, 80, 'sapato normal'),
(4, 'moleton', 'Unisex', 3000, 900, 'moleton haaaaaaaaaaaaaaaaaaaaa'),
(5, 'cueca', 'Masculino', 90, 30, 'cueca box');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `codigo` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `tipoFuncionario` varchar(255) DEFAULT NULL,
  `turno` varchar(255) DEFAULT NULL,
  `estagiario` varchar(255) DEFAULT NULL,
  `remunerado` varchar(255) DEFAULT NULL,
  `obs` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuarios`
--

INSERT INTO `usuarios` (`codigo`, `nome`, `senha`, `tipoFuncionario`, `turno`, `estagiario`, `remunerado`, `obs`) VALUES
(1, 'davi', '1234', NULL, NULL, NULL, NULL, NULL),
(2, 'davi2', '321', 'Logístico', 'Tarde', 'Sim', 'não', 'asdfgsgsg'),
(3, 'maldades', '1234', 'Vendedor', 'Tarde', 'Sim', 'não', 'pode escravisar'),
(4, 'allison', '1234', 'Vendedor', 'Noite', 'Sim', 'sim', 'aaaaaaaaaaaaaaaaaaaaaaaa'),
(5, 'aaaa', '1234', 'Entregador', 'Tarde', 'Sim', 'sim', 'dfdfdfdf');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `roupas`
--
ALTER TABLE `roupas`
  ADD PRIMARY KEY (`codigo`);

--
-- Índices de tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`codigo`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `roupas`
--
ALTER TABLE `roupas`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
