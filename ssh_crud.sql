-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ssh_crud
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `housing_estate`
--

DROP TABLE IF EXISTS `housing_estate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `housing_estate` (
  `id` varchar(20) NOT NULL,
  `h_e_adress` varchar(20) NOT NULL,
  `h_e_developer` varchar(20) NOT NULL,
  `h_e_area` int DEFAULT '0',
  `h_e_pet` int DEFAULT '0',
  `h_e_family` int DEFAULT '0',
  `h_e_car` int DEFAULT '0',
  `h_e_staff` int DEFAULT '0',
  `h_e_building` int DEFAULT '0',
  `h_e_parking` int DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `housing_estate`
--

LOCK TABLES `housing_estate` WRITE;
/*!40000 ALTER TABLE `housing_estate` DISABLE KEYS */;
/*!40000 ALTER TABLE `housing_estate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `id` varchar(20) NOT NULL,
  `h_e_id` varchar(20) DEFAULT NULL,
  `s_name` varchar(20) NOT NULL,
  `s_sex` varchar(20) NOT NULL,
  `s_age` int DEFAULT '0',
  `s_telephone` int DEFAULT NULL,
  `s_idcard` int DEFAULT NULL,
  `s_work_position` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `h_e_id` (`h_e_id`),
  CONSTRAINT `staff_ibfk_1` FOREIGN KEY (`h_e_id`) REFERENCES `housing_estate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_account_number`
--

DROP TABLE IF EXISTS `staff_account_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_account_number` (
  `id` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `staff_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `staff_id` (`staff_id`),
  CONSTRAINT `staff_account_number_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_account_number`
--

LOCK TABLES `staff_account_number` WRITE;
/*!40000 ALTER TABLE `staff_account_number` DISABLE KEYS */;
/*!40000 ALTER TABLE `staff_account_number` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-06 23:46:00
