-- MariaDB dump 10.19  Distrib 10.5.18-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: sm2k4
-- ------------------------------------------------------
-- Server version	10.5.18-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `Book_ID` varchar(6) DEFAULT NULL,
  `Book_Name` varchar(20) DEFAULT NULL,
  `Author_Name` varchar(20) DEFAULT NULL,
  `Publishers` varchar(20) DEFAULT NULL,
  `Price` int(11) DEFAULT NULL,
  `Type` varchar(20) DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('C0001','Fast Cook','Lata Kapoor','EPB',355,'Cookery',5),('F0001','The Tears','William Hopkins','First Publ.',700,'Fiction',20),('T0001','My First C++','Brain & Brooke','EPB',350,'Text',10),('T0002','C++ Brainworks','A.W Rossaine','TDH',350,'Text',15),('F0002','Thunderbolts','Anna Roberts','First Publ.',800,'Fiction',50);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `club`
--

DROP TABLE IF EXISTS `club`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `club` (
  `CoachID` int(5) NOT NULL,
  `CoachName` varchar(20) DEFAULT NULL,
  `Sports` varchar(20) DEFAULT NULL,
  `DateOfAppl` date DEFAULT NULL,
  `Salary` int(10) DEFAULT NULL,
  `Gender` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`CoachID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `club`
--

LOCK TABLES `club` WRITE;
/*!40000 ALTER TABLE `club` DISABLE KEYS */;
INSERT INTO `club` VALUES (1001,'Rabindra','karate','1990-03-27',12000,'M'),(1002,'Ambika','karate','1998-01-20',30000,'F'),(1003,'Nitin','Squash','1998-02-19',15000,'M'),(1004,'Rohit','Basketball','1999-04-23',18000,'M'),(1005,'Mohan','Swimming','1998-02-24',30000,'M'),(1006,'Saumya','Swimming','2001-01-22',15000,'F'),(1007,'Garima','karate','2010-02-27',5600,'F'),(1008,'Shailja','Basketball','2010-05-29',8500,'F');
/*!40000 ALTER TABLE `club` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issued`
--

DROP TABLE IF EXISTS `issued`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `issued` (
  `Book_ID` varchar(6) DEFAULT NULL,
  `Quantity_Issued` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issued`
--

LOCK TABLES `issued` WRITE;
/*!40000 ALTER TABLE `issued` DISABLE KEYS */;
INSERT INTO `issued` VALUES ('T0001',4),('C0001',5),('F0001',2),('F0002',4);
/*!40000 ALTER TABLE `issued` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `item` (
  `Code` int(4) NOT NULL,
  `ItemName` varchar(20) DEFAULT NULL,
  `Company` varchar(20) DEFAULT NULL,
  `Qty` int(4) DEFAULT NULL,
  `Price` int(6) DEFAULT NULL,
  `ExpiryDate` date DEFAULT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1001,'Jelly','Nestle',23,155,'2012-11-21'),(1002,'Cake','Britannia',45,205,'2013-01-12'),(1003,'Maggi','Nestle',80,105,'2013-02-10'),(1004,'Chocolate','Cadbury',100,205,'2012-12-27'),(1005,'Biscuit','Britannia',90,105,'2012-12-12'),(1006,'Jam','Kissan',34,165,'2013-01-23'),(1007,'Sauce','Kissan',120,265,'2013-02-15');
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patient` (
  `Pcode` varchar(3) DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Dept` varchar(20) DEFAULT NULL,
  `DOA` date DEFAULT NULL,
  `Charge` int(11) DEFAULT NULL,
  `Gender` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES ('P1','Karan',24,'Surgery','2010-07-07',5000,'M'),('P2','Varun',45,'Orthopedic','2010-12-19',8000,'M'),('P3','Ravina',12,'Orthopedic','2010-01-15',8000,'F'),('P4','Ankita',36,'Surgery','2009-04-16',12000,'F'),('P5','Ketan',16,'ENT','2009-07-31',25000,'M'),('P6','Arvind',29,'ENT','2010-07-07',15000,'M'),('P7','Zugal',45,'Cardiology','2010-10-20',14000,'M');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-16 11:55:40
