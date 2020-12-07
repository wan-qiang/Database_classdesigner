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
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `c_id` varchar(20) NOT NULL,
  `f_id` varchar(20) NOT NULL,
  `date` datetime NOT NULL,
  `money` float DEFAULT '0',
  PRIMARY KEY (`c_id`,`f_id`),
  KEY `f_id` (`f_id`),
  CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `cost` (`id`),
  CONSTRAINT `bill_ibfk_2` FOREIGN KEY (`f_id`) REFERENCES `family` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `building`
--

DROP TABLE IF EXISTS `building`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `building` (
  `id` varchar(20) NOT NULL,
  `h_e_id` varchar(20) NOT NULL,
  `b_adress` varchar(20) NOT NULL,
  `b_family` int DEFAULT '0',
  `floor` int DEFAULT '0',
  `unit` int DEFAULT '0',
  `room` int DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `h_e_id` (`h_e_id`),
  CONSTRAINT `building_ibfk_1` FOREIGN KEY (`h_e_id`) REFERENCES `housing_estate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `building`
--

LOCK TABLES `building` WRITE;
/*!40000 ALTER TABLE `building` DISABLE KEYS */;
/*!40000 ALTER TABLE `building` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car` (
  `id` varchar(20) NOT NULL,
  `f_id` varchar(20) NOT NULL,
  `color` varchar(20) NOT NULL,
  `brand` varchar(20) NOT NULL,
  `model` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `f_id` (`f_id`),
  CONSTRAINT `car_ibfk_1` FOREIGN KEY (`f_id`) REFERENCES `family` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cost`
--

DROP TABLE IF EXISTS `cost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cost` (
  `id` varchar(20) NOT NULL,
  `f_id` varchar(20) NOT NULL,
  `s_date` datetime DEFAULT '2000-01-01 00:00:00',
  `e_date` datetime DEFAULT NULL,
  `money` float DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `f_id` (`f_id`),
  CONSTRAINT `cost_ibfk_1` FOREIGN KEY (`f_id`) REFERENCES `family` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cost`
--

LOCK TABLES `cost` WRITE;
/*!40000 ALTER TABLE `cost` DISABLE KEYS */;
/*!40000 ALTER TABLE `cost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `family`
--

DROP TABLE IF EXISTS `family`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `family` (
  `id` varchar(20) NOT NULL,
  `h_e_id` varchar(20) NOT NULL,
  `family_number` varchar(20) NOT NULL,
  `parking` int DEFAULT '0',
  `pet` int DEFAULT '0',
  `people` int DEFAULT '0',
  `car` int DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `h_e_id` (`h_e_id`),
  CONSTRAINT `family_ibfk_1` FOREIGN KEY (`h_e_id`) REFERENCES `housing_estate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `family`
--

LOCK TABLES `family` WRITE;
/*!40000 ALTER TABLE `family` DISABLE KEYS */;
/*!40000 ALTER TABLE `family` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `family_account_number`
--

DROP TABLE IF EXISTS `family_account_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `family_account_number` (
  `id` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `f_id` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `f_id` (`f_id`),
  CONSTRAINT `family_account_number_ibfk_1` FOREIGN KEY (`f_id`) REFERENCES `family` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `family_account_number`
--

LOCK TABLES `family_account_number` WRITE;
/*!40000 ALTER TABLE `family_account_number` DISABLE KEYS */;
/*!40000 ALTER TABLE `family_account_number` ENABLE KEYS */;
UNLOCK TABLES;

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
  `h_e_name` varchar(20) NOT NULL,
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
-- Table structure for table `parking`
--

DROP TABLE IF EXISTS `parking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `parking` (
  `h_e_id` varchar(20) NOT NULL,
  `f_id` varchar(20) NOT NULL,
  `adress` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`h_e_id`,`f_id`),
  KEY `f_id` (`f_id`),
  CONSTRAINT `parking_ibfk_1` FOREIGN KEY (`h_e_id`) REFERENCES `housing_estate` (`id`),
  CONSTRAINT `parking_ibfk_2` FOREIGN KEY (`f_id`) REFERENCES `family` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking`
--

LOCK TABLES `parking` WRITE;
/*!40000 ALTER TABLE `parking` DISABLE KEYS */;
/*!40000 ALTER TABLE `parking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `people`
--

DROP TABLE IF EXISTS `people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `people` (
  `id` varchar(20) NOT NULL,
  `f_id` varchar(20) NOT NULL,
  `pname` varchar(20) NOT NULL,
  `psex` varchar(10) NOT NULL,
  `page` int DEFAULT '0',
  `pphone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `f_id` (`f_id`),
  CONSTRAINT `people_ibfk_1` FOREIGN KEY (`f_id`) REFERENCES `family` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people`
--

LOCK TABLES `people` WRITE;
/*!40000 ALTER TABLE `people` DISABLE KEYS */;
/*!40000 ALTER TABLE `people` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pet`
--

DROP TABLE IF EXISTS `pet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pet` (
  `id` varchar(20) NOT NULL,
  `f_id` varchar(20) NOT NULL,
  `variety` varchar(20) NOT NULL,
  `sex` varchar(20) NOT NULL,
  `age` int DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `f_id` (`f_id`),
  CONSTRAINT `pet_ibfk_1` FOREIGN KEY (`f_id`) REFERENCES `family` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pet`
--

LOCK TABLES `pet` WRITE;
/*!40000 ALTER TABLE `pet` DISABLE KEYS */;
/*!40000 ALTER TABLE `pet` ENABLE KEYS */;
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

-- Dump completed on 2020-12-07 12:16:33
