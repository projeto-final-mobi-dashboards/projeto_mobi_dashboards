create database if not exists projeto;
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
-- Table structure for table `enderecos`
--

DROP TABLE IF EXISTS `enderecos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enderecos` (
  `usuario_id` bigint NOT NULL,
  `bairro` varchar(50) NOT NULL,
  `cep` varchar(50) NOT NULL,
  `cidade` varchar(100) NOT NULL,
  `numero` varchar(100) NOT NULL,
  `rua` varchar(100) NOT NULL,
  PRIMARY KEY (`usuario_id`),
  CONSTRAINT `FKbmhtlb81pj58hm1itutsrs1as` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enderecos`
--

LOCK TABLES `enderecos` WRITE;
/*!40000 ALTER TABLE `enderecos` DISABLE KEYS */;
INSERT INTO `enderecos` VALUES (1,'Da Luz','26260-030','Nova Iguaçu','192','Rua Ana Costa'),(2,'Autódromo','26042-180','Nova Iguaçu','1305','Rua Coronel Tinoco'),(5,'Recantus','26157-336','Belford Roxo','13','Rua Maria Luísa'),(6,'Nova Piam','26165-000','Belford Roxo','82','Rua Umbelina Barcelos'),(7,'Parque Flora','26041-080','Nova Iguaçu','0','Rua Dona Leopoldina'),(8,'Irajá','21231-050','Rio de Janeiro','289','Rua Criciúma'),(9,'Moquetá','26285-350','Nova Iguaçu','91','Rua Eliza Lessa de Alvarenga'),(10,'Engenho Pequeno','26011-352','Nova Iguaçu','213','Rua Primeiro de Maio'),(11,'Nova Piam','26115-190','Belford Roxo','266','Rua Amarau'),(12,'Triangulo','26052-130','Nova Iguaçu','120','Rua Carlos'),(13,'Cidade Jardim Parque Estoril','26063-190','Nova Iguaçu','795','Rua Vasco da Gama'),(14,'Centro','26112-230','Belford Roxo','108','Rua Joana Angélica'),(15,'Oswaldo Cruz','21341-130','Rio de Janeiro','230','Rua Paulo Prado'),(16,'Santo Antônio da Prata','26130-740','Belford Roxo','05','Rua Ângel'),(17,'Vilar dos Teles','25565-150','São João de Meriti','01','Rua Doutor César Nascimento Monteiro'),(18,'Itaipu','26140-075','Belford Roxo','20','Rua Sociedade'),(19,'Da Luz','26256-142','Nova Iguaçu','745','Rua Professor Joaquim Cardoso de Matos'),(20,'Da Luz','26255-291','Nova Iguaçu','355','Rua Juiz Alberto Nader'),(21,'Jardim Monte Castelo','26041-630','Nova Iguaçu','115','Rua Eliana Cotrim'),(22,'Fanchem','26383-450','Queimados','284','Rua Peter Shutzwence'),(23,'Iguaçu Velho','26062-025','Nova Iguaçu','84','Rua Barão de Tinguá'),(24,'Chaperó','23831-190','Itaguaí','436','Rua Professor Amauri Lima Benedicto'),(25,'Magalhães Bastos','21750-340','Rio de Janeiro','90','Rua Crispim de Macedo'),(26,'Éden','25545-180','São João de Meriti','S/n Lt 07','Rua Santa Margarida'),(27,'Vila de Cava','26051-720','Nova Iguaçu','544','Rua Sacadura Cabral'),(28,'Jardim Pernambuco','26275-390','Nova Iguaçu','650','Rua Buenos Aires');
/*!40000 ALTER TABLE `enderecos` ENABLE KEYS */;
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
