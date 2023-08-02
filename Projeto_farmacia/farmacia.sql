/*
SQLyog Trial v13.1.8 (64 bit)
MySQL - 10.4.28-MariaDB : Database - farmacia
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`farmacia` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `farmacia`;

/*Table structure for table `produtos` */

DROP TABLE IF EXISTS `produtos`;

CREATE TABLE `produtos` (
  `codigo` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `fabrica` varchar(255) DEFAULT NULL,
  `estoque` varchar(255) DEFAULT NULL,
  `validade` varchar(255) DEFAULT NULL,
  `valor_compra` varchar(255) DEFAULT NULL,
  `valor_venda` varchar(255) DEFAULT NULL,
  `controlada` varchar(255) DEFAULT NULL,
  `medida` varchar(255) DEFAULT NULL,
  `decricao` varchar(255) DEFAULT NULL,
  `categoria` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=2147483648 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `produtos` */

insert  into `produtos`(`codigo`,`nome`,`fabrica`,`estoque`,`validade`,`valor_compra`,`valor_venda`,`controlada`,`medida`,`decricao`,`categoria`) values 
(13123,'a','aaaaaaaaa','11','2020-1-31','15,00','0,00','0','Micrograma (mcg)','aaaa','Higiene'),
(2147483647,'sonrisal','IFRN','99','2020-2-14','0,00','51,00','1','Litro (L)','faz o usuario ter nota 100 no projeto de professor Abrahao, pelo amor de deus','Saúde');

/*Table structure for table `usuarios` */

DROP TABLE IF EXISTS `usuarios`;

CREATE TABLE `usuarios` (
  `codigo` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `senha` varchar(225) DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `usuarios` */

insert  into `usuarios`(`codigo`,`nome`,`senha`) values 
(1,'livia','123'),
(2,'eduarda','123'),
(3,'mari','123'),
(4,'sonaly','123');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
