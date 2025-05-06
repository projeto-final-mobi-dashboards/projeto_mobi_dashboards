-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: api_itinerarios
-- ------------------------------------------------------
-- Server version	8.4.3
use projeto;
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
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cargo` varchar(50) NOT NULL,
  `cpf` varchar(50) NOT NULL,
  `email_institucional` varchar(100) NOT NULL,
  `matricula` varchar(20) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `senha` varchar(256) NOT NULL,
  `termos` bit(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_6toabl59ulnhirs3gqn22cux4` (`email_institucional`),
  UNIQUE KEY `UK_lss4x3vmrjtsxddl7k7dfgrqd` (`matricula`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'estudante','171.707.407-37','17170740737@cefet-rj.br','2312146ECAN','Guilherme Araujo de Almeida ','$2a$10$wZ0grlSyvEynDdyv39NB5.7FWjNS9Mx5xSfhNSs2B8IQiB9RzeiIG',_binary ''),(2,'estudante','230.003.977-01','23000397701@cefet-rj.br','2300666INFINI','Miguel da Silva Gomes','$2a$10$M79lZUeJIeQyZBMEs6cw5uPwJb744qm377UgUnQcgkVcbSjhOLT2a',_binary ''),(5,'estudante','160.503.077-51','16050307751@cefet-rj.br','2013063EPROD','Teste Victor','$2a$10$v/tyMuLOLfNEKaXGCAA/QenWhxnjRjY3ywd6Oj2PEYr47Lhl6Y1ku',_binary ''),(6,'estudante','166.124.867-59','16612486759@cefet-rj.br','2202241INFINI','kézia da silva dos santos','$2a$10$N6mXt9ahC8MoaGIDBNFkruFhL5xIhwRoWxZv5Opp8CoOGSteHQKxK',_binary ''),(7,'estudante','209.580.907-69','20958090769@cefet-rj.br','2312504INFINI','Kezia Luiza do Bomfim Oliveira ','$2a$10$dPblirOnMgEKjf54oWUPnufAXR76e9YGkc3XPVsVIJqGkjc3QteJW',_binary ''),(8,'estudante','184.819.427-74','18481942774@cefet-rj.br','2300125INFINI','Matheus Santos Fonseca','$2a$10$Q6KzK/.0s81JPQCdKh3KCOeW/qF6yx2A65KBh4WXweBZK4OB2wIca',_binary ''),(9,'estudante','155.636.707-40','15563670740@cefet-rj.br','2300632INFINI','Juan Canle Marinho','$2a$10$uJ2lHoz6jFMWbzK3vnBJqOs/G9tcbuoqnCIAUzGKrJxDdw78N35kG',_binary ''),(10,'estudante','207.706.107-30','20770610730@cefet-rj.br','2300006INFINI','Gustavo Luiz da Silva Procópio ','$2a$10$TS3prEN6mu8Qq5Dd5poREu4YC4ZPoLmh5Yh80eKK5hKZMwKJqBOfC',_binary ''),(11,'estudante','187.828.057-09','18782805709@cefet-rj.br','2300684INFINI','João Pedro Araujo das Chagas ','$2a$10$ipWNSkl5LYjWNhsxGpwWleeFGHFWL6cz3wlJvgW.rjCko8cTKpZXe',_binary ''),(12,'estudante','170.948.897-20','17094889720@cefet-rj.br','2300430INFINI','Evander de Assis Silva Cabral','$2a$10$a37HRuXtdBXZYUBP58zlIeJGU7FNmOdBcpSrNxGUbPjUUqxepUsGC',_binary ''),(13,'estudante','066.212.987-30','06621298730@cefet-rj.br','2201920INFINI','Danilo Sudré do Nascimento Santos','$2a$10$gqRSAofCTQRKfM7p8GY/5.T8bobxf.Bpnf0WMmn./brBTn115V06i',_binary ''),(14,'estudante','194.140.207-05','19414020705@cefet-rj.br','2300135INFINI','Jorge henry de andrade moreira','$2a$10$ZAutfn081aQ7NALofaBaD.pKHCiYf2d.8eK42OiOjBlY5eCuNCMQW',_binary ''),(15,'estudante','180.638.937-19','18063893719@cefet-rj.br','2428856EMEC','Gabriel Keller Dutra Mendes da Silva','$2a$10$Ue9k9DgyDN96ki41RCAGpOuYJcdb6K38O.HEp0QmUx8I03ober94a',_binary ''),(16,'estudante','199.604.557-18','19960455718@cefet-rj.br','2511994EMEC','João Carlos Fernandes de Oliveira','$2a$10$H7Uwn9zsErWgXcqsnGs7LumcPrh2gQfB8J39HyOg8FzHthc/STxC6',_binary ''),(17,'estudante','208.116.347-01','208116347@cefet-rj.br','2512081EMEC','Sara da Silva Gonçalves Peixoto ','$2a$10$iPBmb8YRqnRmxsPgsD6c/uv5N4mGANMiKbi/wI5UvSPOLorFyYTHa',_binary ''),(18,'estudante','203.160.877-00','20316087700@cefet-rj.br','2500618INFINI','Samuel Pereira de Mello França','$2a$10$FEjKmS1eAeKlUwp1/UUQqO45m6w7ab5kv4XHZkKJp3l2JHYDk4C6e',_binary ''),(19,'estudante','193.487.257-18','19348725718@cefet-rj.br','2500008AUTNI','Felipe Werneck Macedo','$2a$10$ho1qoB04ahqyYt1aXuasOu/4XqkBaqnymBw.A7EFO8jJMKvFY8/iG',_binary ''),(20,'estudante','167.000.717-04','16700071704@cefet-rj.br','2300134INFINI','Davi Nogueira Souto','$2a$10$Dti/UqljMQhrLWZvOA/kY.OH5mXdWDg1Ym3133QHMkUFqAu.M9o6m',_binary ''),(21,'estudante','162.106.837-46','16210683746@cefet-rj.br','2500121ENFINI','Luanny Alonso Santos Fernandes ','$2a$10$B3.94k3g7Mw6QTVy44iD6OrzuBhUuJNRPY3/CP5cdLUMoO2CpPWJi',_binary ''),(22,'estudante','212.432.497-73','21243249773@cefet-rj.br','2301817ENFINI','Sophia da Silva Salutto ','$2a$10$vH6kElssiehbup8D21wB0uoL8EoorERVhRQ0u6Q0soWalRaE.kbQW',_binary ''),(23,'estudante','190.303.057-97','19030305797@cefet-rj.br','2301924INFINI','Artur Samuel Vieira do Nascimento ','$2a$10$Gp6cDUqpfG5VcwKXskHMYeACrLgIS54XEI5jyTLqsi9r3SEcBAlwq',_binary ''),(24,'estudante','211.352.527-50','21135252750@cefet-rj.br','2400663AUTNI','Clara Emanuele da Silva Mange Eutimio ','$2a$10$MgDE.pj4h/14HY9RHDtNX.WBlKCjGAwHmxj/D6BVNl9z8veBdyIzG',_binary ''),(25,'estudante','150.064.497-80','15006449780@cefet-rj.br','2202170TELINI','Iago Cassiano Barbosa Ferreira ','$2a$10$0ecuTVm/u8AOgBk9fKCPle4hhWP8rG3Dqj9CuTEwCtHdsl59/cpaG',_binary ''),(26,'estudante','163.302.637-01','16330263701@cefet-rj.br','2300123TELINI','Isabele da Costa Oliveira ','$2a$10$noMJlW1OzW/tZpoVGvVW5OCfw1aEl/nHbS1PQfczj8D4U.UYqRNYC',_binary ''),(27,'estudante','205.856.827-39','20585682739@cefet-rj.br','2300567AUTNI','Allana Milena Rozario Silva ','$2a$10$AxrQl6VSeTAoIO4MCMFY3ua/FPdSuVHxRbkpxlTQ4DiUkY.zZQDr6',_binary ''),(28,'estudante','183.682.427-03','18368242703@cefet-rj.br','2500112TELINI','Anthony gustavo de lima Pereira da costa ','$2a$10$JerlvNtsgFSQK7V.ZLfHa.4Zea6YSn80.66jzMmsIZC1vV5wyjfiy',_binary '');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
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
