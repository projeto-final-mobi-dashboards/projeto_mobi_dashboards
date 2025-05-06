use projeto;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: api_itinerarios
-- ------------------------------------------------------
-- Server version	8.4.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `trecho`
--

/*DROP TABLE IF EXISTS `trecho`;*/
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trecho` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `bairro` varchar(200) NOT NULL,
  `cidade` varchar(200) NOT NULL,
  `complemento` varchar(200) DEFAULT NULL,
  `hora` varchar(200) NOT NULL,
  `latitude` double NOT NULL,
  `local` varchar(200) NOT NULL,
  `longitude` double NOT NULL,
  `meio_transporte` varchar(200) NOT NULL,
  `numero` varchar(200) NOT NULL,
  `rua` varchar(200) NOT NULL,
  `tipo_trajeto` varchar(255) NOT NULL,
  `itinerario_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKtjmqkk0k74cu93pp6e6gfhjyu` (`itinerario_id`),
  CONSTRAINT `FKtjmqkk0k74cu93pp6e6gfhjyu` FOREIGN KEY (`itinerario_id`) REFERENCES `itinerario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trecho`
--

LOCK TABLES `trecho` WRITE;
/*!40000 ALTER TABLE `trecho` DISABLE KEYS */;
INSERT INTO `trecho` VALUES (1,'Santa Rita','Nova Iguaçu','Estr. de Adrianópolis, 1317 - Vila Nossa Sra. da Conceicao, Nova Iguaçu - RJ, 26041-271','22:07',-22.704589,'CEFET RJ - NI',-43.4617004,'Carro','1317','Estrada de Adrianópolis','Ida',1),(2,'Gerard Danon','Nova Iguaçu','Casa','06:12',-22.7075604,'Ponto',-43.47372379999999,'A pé','1305','Rua Coronel Tinoco','Ida',1),(3,'sao bernardo','belford roxo','','11:23',-22.7358222,'casa',-43.3894353,'Ônibus','82','umbelina barcelos','Ida',2),(4,'Iraja','Rio de janeiro','','14:22',-22.8301565,'Saca',-43.3217573,'Ônibus','289','Rua criciuma','Ida',3),(5,'Santa Rita','Nova Iguaçu','Estr. de Adrianópolis, 1317 - Vila Nossa Sra. da Conceicao, Nova Iguaçu - RJ, 26041-271','15:31',-22.704589,'CEFET RJ - NI',-43.4617004,'Ônibus','1317','Estrada de Adrianópolis','Ida',5),(6,'Engenho Pequeno','Nova Iguaçu ','','15:31',-22.7462844,'Casa',-43.4260442,'Ônibus','213','Rua primeiro de maio','Volta',5),(7,'Andrade Araujo','Nova Iguaçu ','Mercado','15:34',-22.7580274,'Mercado Vianense',-43.4212496,'A pé','010','Dona Clara de Araujo','Ida',5),(8,'Engenho Pequeno ','Nova Iguaçu ','','15:50',-22.7462844,'Casa',-43.4260442,'A pé','213','Primeiro de Maio ','Volta',5),(9,'Nova Piam','Belfod Roxo','','15:55',-22.7358222,'casa para a rodoviaria',-43.3894353,'Ônibus','82','umbelina barcelos','Ida',2),(10,'centro','nova Iguaçu','top shopping','15:55',-22.7532679,'shopping  pra escola',-43.45420960000001,'Ônibus','540','av. gov. roberto silveira','Ida',2),(11,'centro','Nova iguaçu','rodoviaria Nova Iguaçu','15:55',-22.7580676,'rodoviaria',-43.455862,'Ônibus','2509','av. mal. floriano peixoto','Volta',2),(12,'Nova Piam','belford Roxo','','15:55',-22.7358222,'casa',-43.3894353,'Ônibus','82','umbelina barcelos','Volta',2),(13,'Santa Amélia','Belford roxo ','Casa','07:16',-22.7373907,'Casa',-43.38931059999999,'Ônibus','266','Rua Amarau','Ida',7),(14,'Triangulo','Nova Iguaçu','','07:35',-22.6869343,'Casa',-43.4512728,'Ônibus','120','Rua Carlos','Ida',8),(15,'Montevidéu','Nova Iguaçu','','07:42',-22.6407344,'Meu ponto',-43.4077608,'Ônibus','6454','Estr. Zumbi dos Palmares','Ida',9),(16,'Santa Rita','Nova Iguaçu','Estr. de Adrianópolis, 1317 - Vila Nossa Sra. da Conceicao, Nova Iguaçu - RJ, 26041-271','07:42',-22.704589,'CEFET RJ - NI',-43.4617004,'Ônibus','1317','Estrada de Adrianópolis','Ida',9),(17,'Santa Rita','Nova Iguaçu','Estr. de Adrianópolis, 1317 - Vila Nossa Sra. da Conceicao, Nova Iguaçu - RJ, 26041-271','07:47',-22.704589,'CEFET RJ - NI',-43.4617004,'Ônibus','1317','Estrada de Adrianópolis','Volta',9),(18,'Montevidéu','Nova Iguaçu','','07:47',-22.6407344,'Meu ponto',-43.4077608,'Ônibus','6454','Estr. Zumbi dos Palmares','Volta',9),(19,'Centro','Rj','','08:56',-22.9840315,'Casa',-43.2048298,'Ônibus','108','Rua joana angelica','Ida',10),(20,'Santa Rita','Nova Iguaçu','Estr. de Adrianópolis, 1317 - Vila Nossa Sra. da Conceicao, Nova Iguaçu - RJ, 26041-271','08:57',-22.704589,'CEFET RJ - NI',-43.4617004,'Ônibus','1317','Estrada de Adrianópolis','Ida',10),(21,'Santa Rita','Nova Iguaçu','Estr. de Adrianópolis, 1317 - Vila Nossa Sra. da Conceicao, Nova Iguaçu - RJ, 26041-271','14:06',-22.704589,'CEFET RJ - NI',-43.4617004,'Ônibus','1317','Estrada de Adrianópolis','Ida',11),(22,'Vilar dos Teles ','São João de Meriti ','','14:07',-22.7826924,'Casa',-43.3621695,'Ônibus','1','Rua Doutor César do Nascimento Monteiro ','Volta',11),(23,'Iguaçu velho','Nova iguaçu ','','16:20',-22.6587491,'Casa',-43.4189952,'Ônibus','84','Barão de tingua ','Ida',13),(24,'Santa Rita','Nova Iguaçu','Estr. de Adrianópolis, 1317 - Vila Nossa Sra. da Conceicao, Nova Iguaçu - RJ, 26041-271','17:11',-22.704589,'CEFET RJ - NI',-43.4617004,'Ônibus','1317','Estrada de Adrianópolis','Ida',13);
/*!40000 ALTER TABLE `trecho` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-22 14:58:12
