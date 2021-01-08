-- MySQL dump 10.13  Distrib 8.0.22, for osx10.16 (x86_64)
--
-- Host: localhost    Database: we_ro
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
-- Table structure for table `album_charts`
--

DROP TABLE IF EXISTS `album_charts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album_charts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `album_id` int NOT NULL,
  `chart_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `album_charts_album_id_56556f6f_fk_albums_id` (`album_id`),
  KEY `album_charts_chart_id_79d040ec_fk_charts_id` (`chart_id`),
  CONSTRAINT `album_charts_album_id_56556f6f_fk_albums_id` FOREIGN KEY (`album_id`) REFERENCES `albums` (`id`),
  CONSTRAINT `album_charts_chart_id_79d040ec_fk_charts_id` FOREIGN KEY (`chart_id`) REFERENCES `charts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album_charts`
--

LOCK TABLES `album_charts` WRITE;
/*!40000 ALTER TABLE `album_charts` DISABLE KEYS */;
/*!40000 ALTER TABLE `album_charts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `album_emotions`
--

DROP TABLE IF EXISTS `album_emotions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album_emotions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `album_id` int NOT NULL,
  `emotion_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `album_emotions_album_id_fb8e4568_fk_albums_id` (`album_id`),
  KEY `album_emotions_emotion_id_b2a9d50c_fk_emotions_id` (`emotion_id`),
  CONSTRAINT `album_emotions_album_id_fb8e4568_fk_albums_id` FOREIGN KEY (`album_id`) REFERENCES `albums` (`id`),
  CONSTRAINT `album_emotions_emotion_id_b2a9d50c_fk_emotions_id` FOREIGN KEY (`emotion_id`) REFERENCES `emotions` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album_emotions`
--

LOCK TABLES `album_emotions` WRITE;
/*!40000 ALTER TABLE `album_emotions` DISABLE KEYS */;
/*!40000 ALTER TABLE `album_emotions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `album_genres`
--

DROP TABLE IF EXISTS `album_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album_genres` (
  `id` int NOT NULL AUTO_INCREMENT,
  `album_id` int NOT NULL,
  `genre_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `album_genres_album_id_68922487_fk_albums_id` (`album_id`),
  KEY `album_genres_genre_id_1a42e176_fk_genres_id` (`genre_id`),
  CONSTRAINT `album_genres_album_id_68922487_fk_albums_id` FOREIGN KEY (`album_id`) REFERENCES `albums` (`id`),
  CONSTRAINT `album_genres_genre_id_1a42e176_fk_genres_id` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album_genres`
--

LOCK TABLES `album_genres` WRITE;
/*!40000 ALTER TABLE `album_genres` DISABLE KEYS */;
INSERT INTO `album_genres` VALUES (1,1,1),(2,2,1),(3,3,2),(4,4,2),(5,5,3),(6,6,2),(7,7,3),(8,8,4),(9,9,2),(10,10,2),(11,11,2),(12,12,2),(13,12,4),(14,13,1),(15,14,3),(16,15,2),(17,16,1),(18,17,5),(19,18,1),(20,19,5),(21,20,2),(22,21,1),(23,22,1),(24,23,1),(25,24,2),(26,25,2),(27,26,4),(28,27,3),(29,28,2),(30,29,3),(31,30,2),(32,31,3),(33,32,4),(34,33,1),(35,34,2),(36,35,2),(37,36,5),(38,37,2),(39,38,2),(40,39,4),(41,40,2),(42,41,3),(43,42,4),(44,43,1),(45,44,2),(46,45,2),(47,46,2),(48,47,1),(49,48,2),(50,49,2),(51,50,2);
/*!40000 ALTER TABLE `album_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `album_moods`
--

DROP TABLE IF EXISTS `album_moods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album_moods` (
  `id` int NOT NULL AUTO_INCREMENT,
  `album_id` int NOT NULL,
  `mood_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `album_moods_album_id_ee62e34e_fk_albums_id` (`album_id`),
  KEY `album_moods_mood_id_053bfb4d_fk_moods_id` (`mood_id`),
  CONSTRAINT `album_moods_album_id_ee62e34e_fk_albums_id` FOREIGN KEY (`album_id`) REFERENCES `albums` (`id`),
  CONSTRAINT `album_moods_mood_id_053bfb4d_fk_moods_id` FOREIGN KEY (`mood_id`) REFERENCES `moods` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album_moods`
--

LOCK TABLES `album_moods` WRITE;
/*!40000 ALTER TABLE `album_moods` DISABLE KEYS */;
/*!40000 ALTER TABLE `album_moods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `album_types`
--

DROP TABLE IF EXISTS `album_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album_types` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album_types`
--

LOCK TABLES `album_types` WRITE;
/*!40000 ALTER TABLE `album_types` DISABLE KEYS */;
INSERT INTO `album_types` VALUES (1,'정규'),(2,'싱글');
/*!40000 ALTER TABLE `album_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `albums`
--

DROP TABLE IF EXISTS `albums`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `albums` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `release_date` date NOT NULL,
  `image_url` varchar(2000) NOT NULL,
  `album_type_id` int NOT NULL,
  `artist_id` int NOT NULL,
  `country_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `albums_album_type_id_81ec9746_fk_album_types_id` (`album_type_id`),
  KEY `albums_artist_id_8a9e6bb4_fk_artists_id` (`artist_id`),
  KEY `albums_country_id_2a83ed9e_fk_countries_id` (`country_id`),
  CONSTRAINT `albums_album_type_id_81ec9746_fk_album_types_id` FOREIGN KEY (`album_type_id`) REFERENCES `album_types` (`id`),
  CONSTRAINT `albums_artist_id_8a9e6bb4_fk_artists_id` FOREIGN KEY (`artist_id`) REFERENCES `artists` (`id`),
  CONSTRAINT `albums_country_id_2a83ed9e_fk_countries_id` FOREIGN KEY (`country_id`) REFERENCES `countries` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `albums`
--

LOCK TABLES `albums` WRITE;
/*!40000 ALTER TABLE `albums` DISABLE KEYS */;
INSERT INTO `albums` VALUES (1,'Kiss Me','2009-12-20','https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?ixid=MXwxMjA3fDB8MHxwaG90[…]ufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80',1,1,1),(2,'Like That','2020-12-25','https://images.unsplash.com/photo-1566417713940-fe7c737a9ef2?ixid=MXwxMjA3fDB8MHxwaG90[…]ufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1315&q=80',1,2,1),(3,'Text Me','2020-12-25','https://images.unsplash.com/photo-1505740420928-5e560c06d30e?ixid=MXwxMjA3fDB8MHxwaG90[…]ufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80',1,1,1),(4,'Say So','2020-02-06','https://images.unsplash.com/photo-1510832198440-a52376950479?ixid=MXwxMjA3fDB8MHxwaG90[…]ufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1348&q=80',1,4,1),(5,'애럼 괜찮아요?','1990-02-06','https://images.unsplash.com/photo-1514649045639-b9ae6faad201?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=3400&q=80',1,5,1),(6,'애럼은 존잘러','1990-02-06','https://images.unsplash.com/photo-1517028652656-71b45315812f?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,6,1),(7,'애럼의 크리스마스 캐롤','1990-02-06','https://images.unsplash.com/photo-1607262807149-dfd4c39320a6?ixid=MXwxMjA3fDB8MHxzZWFyY2h8OHx8c2hpbmV8ZW58MHwyfDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',1,7,1),(8,'애럼의 사랑','1990-02-06','https://images.unsplash.com/photo-1512311992738-d75a673c40ec?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1642&q=80',1,8,1),(9,'애럼에게 사랑이란?','1990-02-06','https://images.unsplash.com/photo-1519954235535-ba95cf82a5a1?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,9,1),(10,'애럼 탄신일','1990-02-06','https://images.unsplash.com/photo-1570049475416-7f3067eae58c?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1369&q=80',1,10,1),(11,'','1990-02-06','https://images.unsplash.com/photo-1525018881838-08eca358cc58?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,11,1),(12,'애럼만이 내세상','1990-02-06','https://images.unsplash.com/photo-1564063456422-cf24c3a44133?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1411&q=80',1,12,1),(13,'애럼과 같이','1990-02-06','https://images.unsplash.com/photo-1585716662901-ccda14ddb722?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,13,1),(14,'애럼 더 오클라호만','1990-02-06','https://images.unsplash.com/photo-1578317906878-e64c7a4772ee?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1976&q=80',1,14,1),(15,'애럼더 비트','1990-02-06','https://images.unsplash.com/photo-1523380556360-95dee7d9ca6f?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fG9rY3xlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',1,15,1),(16,'애럼쓰쓰','1990-02-06','https://images.unsplash.com/photo-1590228232524-6776f2d6f84b?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1408&q=80',1,7,1),(17,'애럼쓰고이','1990-02-06','https://images.unsplash.com/photo-1578458303432-3aae09a4a99f?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,7,1),(18,'애럼쏴뢍','1990-02-06','https://images.unsplash.com/photo-1607420112334-a0a99c0408cd?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1864&q=80',1,7,1),(19,'애럼the게임중독','1990-02-06','https://images.unsplash.com/photo-1585851381675-6fdb0e88d827?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1365&q=80',1,1,1),(20,'애럼 유후','1990-02-06','https://images.unsplash.com/photo-1577138043155-7934dd897541?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,2,1),(21,'애럼 더 이모티콘','1990-02-06','https://images.unsplash.com/photo-1523688471150-efdd09f0f312?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,2,1),(22,'애럼 그만','1990-02-06','https://images.unsplash.com/photo-1483135349295-9e3c48106ee6?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,2,1),(23,'애럼 탄신일','1990-02-06','https://images.unsplash.com/photo-1534939618208-e604c88fcffb?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,3,1),(24,'애럼 탄신일','1990-02-06','https://images.unsplash.com/photo-1516651029879-bcd191e7d33b?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,4,1),(25,'애럼 탄신일','1990-02-06','https://images.unsplash.com/photo-1601063458289-77247ba485ec?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,5,1),(26,'애럼 탄신일','1990-02-06','https://images.unsplash.com/photo-1600070347822-6d6d0c3543f0?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,2,2),(27,'애럼 탄신일','1990-02-06','https://images.unsplash.com/photo-1496293455970-f8581aae0e3b?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1001&q=80',1,7,2),(28,'애럼 탄신일','1990-02-06','https://images.unsplash.com/photo-1597067280918-62d08d8afd52?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1369&q=80',1,8,2),(29,'애럼 질러','1990-02-06','https://images.unsplash.com/photo-1587132164684-cfd0b8214d8e?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,9,2),(30,'애럼 인 더 하우스','2020-02-06','https://images.unsplash.com/photo-1591470916941-dcc7b59d0841?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1686&q=80',1,1,2),(31,'애럼쓰','1999-02-06','https://images.unsplash.com/photo-1519084278803-b94f11e1c63b?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fHNoaW5lfGVufDB8MnwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',1,15,2),(32,'애럼인가?','1990-02-06','https://images.unsplash.com/photo-1511638186783-963fde36ce1a?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,2,2),(33,'애럼 인건가','1990-02-06','https://images.unsplash.com/photo-1579466651003-bf074ff488d3?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MjQxfHxkYXJrfGVufDB8MnwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',1,3,2),(34,'애럼 인가요','1990-02-06','https://images.unsplash.com/photo-1593314749968-5e83f303effd?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,14,2),(35,'애럼 우리의 왕','1990-02-06','https://images.unsplash.com/photo-1592920704646-99d0d6792133?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MzQzfHxkYXJrfGVufDB8MnwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',1,5,2),(36,'애럼과 같이','1990-02-06','https://images.unsplash.com/photo-1593160926155-cad551003e3f?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,3,2),(37,'애럼 한분만으로','1990-02-06','https://images.unsplash.com/photo-1545769441-65bd3c7128d8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1411&q=80',1,7,2),(38,'애럼 탄신일','2002-02-06','https://images.unsplash.com/photo-1605926637512-c8b131444a4b?ixid=MXwxMjA3fDB8MHxzZWFyY2h8ODB8fGNocmlzdG1hc3xlbnwwfDJ8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',1,8,2),(39,'애럼 탄신일','2002-02-06','https://images.unsplash.com/photo-1575914550597-50c184334c46?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1351&q=80',1,9,2),(40,'애럼은 할 수 있다!','1990-02-06','https://images.unsplash.com/photo-1521136486846-47c70cd4a591?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,10,2),(41,'애럼이 할수이쪄!!','1990-02-06','https://images.unsplash.com/photo-1566073283089-38a47111c835?ixid=MXwxMjA3fDB8MHxzZWFyY2h8N3x8ZnJlZWRvbXxlbnwwfDJ8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',1,13,2),(42,'애럼의 두번째 사랑','2002-02-06','https://images.unsplash.com/photo-1557331467-f17b71e12ac8?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NjR8fGxvdmV8ZW58MHwyfDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',1,12,2),(43,'애럼의 끝사랑','1990-02-06','https://images.unsplash.com/photo-1587735079480-35d3326e4041?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1393&q=80',1,3,2),(44,'애럼만으로','1999-02-06','https://images.unsplash.com/photo-1501978811118-e2abb948bb81?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,4,2),(45,'애럼 탄신일','1990-02-06','https://images.unsplash.com/photo-1597827390892-87dde0993f53?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,5,2),(46,'15기 감사합니다','1999-02-06','https://images.unsplash.com/photo-1551596210-4da509bd1e99?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MzQ0fHxkYXJrfGVufDB8MnwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',1,6,2),(47,'라인 아미고스','1990-02-06','https://images.unsplash.com/photo-1562544075-dc363e663e59?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1352&q=80',1,4,2),(48,'홀로 위로 할로','1999-02-06','https://images.unsplash.com/photo-1518732836484-bd257665c9d1?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,8,2),(49,'애럼 괜찬하요?','1990-02-06','https://images.unsplash.com/photo-1606208879338-cc46068dfccc?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1401&q=80',1,9,2),(50,'애럼과 아이들','1999-02-06','https://images.unsplash.com/photo-1607442430766-ad4f1e806a41?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1670&q=80',1,5,2);
/*!40000 ALTER TABLE `albums` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artist_types`
--

DROP TABLE IF EXISTS `artist_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist_types` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist_types`
--

LOCK TABLES `artist_types` WRITE;
/*!40000 ALTER TABLE `artist_types` DISABLE KEYS */;
INSERT INTO `artist_types` VALUES (1,'싱글'),(2,'듀오'),(3,'그룹');
/*!40000 ALTER TABLE `artist_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artists`
--

DROP TABLE IF EXISTS `artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artists` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `profile_image_url` varchar(2000) DEFAULT NULL,
  `artist_type_id` int NOT NULL,
  `gender_id` int NOT NULL,
  `genre_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `artists_artist_type_id_359dd778_fk_artist_types_id` (`artist_type_id`),
  KEY `artists_gender_id_66d7798c_fk_genders_id` (`gender_id`),
  KEY `artists_genre_id_3bd0e9fb_fk_genres_id` (`genre_id`),
  CONSTRAINT `artists_artist_type_id_359dd778_fk_artist_types_id` FOREIGN KEY (`artist_type_id`) REFERENCES `artist_types` (`id`),
  CONSTRAINT `artists_gender_id_66d7798c_fk_genders_id` FOREIGN KEY (`gender_id`) REFERENCES `genders` (`id`),
  CONSTRAINT `artists_genre_id_3bd0e9fb_fk_genres_id` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artists`
--

LOCK TABLES `artists` WRITE;
/*!40000 ALTER TABLE `artists` DISABLE KEYS */;
INSERT INTO `artists` VALUES (1,'DPR Live','https://images.unsplash.com/photo-1600975607954-e1f9b9863c1b?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,2,1),(2,'Doja Cat','https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?ixid=MXwxMjA3fDB8MHxwaG90[…]ufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80',1,2,1),(3,'애럼 the Beat','https://images.unsplash.com/photo-1566417713940-fe7c737a9ef2?ixid=MXwxMjA3fDB8MHxwaG90[…]ufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1315&q=80',1,1,1),(4,'다된 밥에 애럼 투척','https://images.unsplash.com/photo-1485528562718-2ae1c8419ae2?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1381&q=80',1,1,1),(5,'애럼_drop_the_beat','https://images.unsplash.com/photo-1484186139897-d5fc6b908812?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,1,4),(6,'함께가요 위고두','https://images.unsplash.com/photo-1534126416832-a88fdf2911c2?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,1,1),(7,'Mug-RAM','https://images.unsplash.com/photo-1534954553104-88cb75be7648?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,2,1),(8,'우리민족끼리','https://images.unsplash.com/photo-1521510186458-bbbda7aef46b?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1401&q=80',3,2,1),(9,'Drop_that','https://images.unsplash.com/photo-1509112756314-34a0badb29d4?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1444&q=80',1,1,1),(10,'LALA-Land','https://images.unsplash.com/photo-1509335035496-c47fc836517f?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1404&q=80',1,2,1),(11,'Adel','https://images.unsplash.com/photo-1528817164944-2cf16aefdc8d?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1397&q=80',1,1,1),(12,'hAWaii','https://images.unsplash.com/photo-1579923272605-85def6c777a3?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1379&q=80',1,1,1),(13,'Idol','https://images.unsplash.com/photo-1514960919797-5ff58c52e5ba?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1355&q=80 ',1,1,1),(14,'너네민족끼리','https://images.unsplash.com/photo-1523617423-4ee97cdd27f4?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,1,1),(15,'OvertheRainbow','https://images.unsplash.com/photo-1530519486016-6ebc8a343be5?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',1,1,1);
/*!40000 ALTER TABLE `artists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_taste_artists`
--

DROP TABLE IF EXISTS `character_taste_artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `character_taste_artists` (
  `id` int NOT NULL AUTO_INCREMENT,
  `artist_id` int NOT NULL,
  `character_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `character_taste_artists_artist_id_abad8e0d_fk_artists_id` (`artist_id`),
  KEY `character_taste_artists_character_id_4f4fc1d8_fk_characters_id` (`character_id`),
  CONSTRAINT `character_taste_artists_artist_id_abad8e0d_fk_artists_id` FOREIGN KEY (`artist_id`) REFERENCES `artists` (`id`),
  CONSTRAINT `character_taste_artists_character_id_4f4fc1d8_fk_characters_id` FOREIGN KEY (`character_id`) REFERENCES `characters` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_taste_artists`
--

LOCK TABLES `character_taste_artists` WRITE;
/*!40000 ALTER TABLE `character_taste_artists` DISABLE KEYS */;
/*!40000 ALTER TABLE `character_taste_artists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_taste_charts`
--

DROP TABLE IF EXISTS `character_taste_charts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `character_taste_charts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `character_id` int NOT NULL,
  `chart_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `character_taste_charts_character_id_3e207bfe_fk_characters_id` (`character_id`),
  KEY `character_taste_charts_chart_id_170183a5_fk_charts_id` (`chart_id`),
  CONSTRAINT `character_taste_charts_character_id_3e207bfe_fk_characters_id` FOREIGN KEY (`character_id`) REFERENCES `characters` (`id`),
  CONSTRAINT `character_taste_charts_chart_id_170183a5_fk_charts_id` FOREIGN KEY (`chart_id`) REFERENCES `charts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_taste_charts`
--

LOCK TABLES `character_taste_charts` WRITE;
/*!40000 ALTER TABLE `character_taste_charts` DISABLE KEYS */;
/*!40000 ALTER TABLE `character_taste_charts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_taste_genres`
--

DROP TABLE IF EXISTS `character_taste_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `character_taste_genres` (
  `id` int NOT NULL AUTO_INCREMENT,
  `character_id` int NOT NULL,
  `genre_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `character_taste_genres_character_id_a501cc24_fk_characters_id` (`character_id`),
  KEY `character_taste_genres_genre_id_8bccd7ba_fk_genres_id` (`genre_id`),
  CONSTRAINT `character_taste_genres_character_id_a501cc24_fk_characters_id` FOREIGN KEY (`character_id`) REFERENCES `characters` (`id`),
  CONSTRAINT `character_taste_genres_genre_id_8bccd7ba_fk_genres_id` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_taste_genres`
--

LOCK TABLES `character_taste_genres` WRITE;
/*!40000 ALTER TABLE `character_taste_genres` DISABLE KEYS */;
/*!40000 ALTER TABLE `character_taste_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `characters`
--

DROP TABLE IF EXISTS `characters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `characters` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `profile_image_url` varchar(2000) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `characters_user_id_26cc4c0c_fk_users_id` (`user_id`),
  CONSTRAINT `characters_user_id_26cc4c0c_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `characters`
--

LOCK TABLES `characters` WRITE;
/*!40000 ALTER TABLE `characters` DISABLE KEYS */;
/*!40000 ALTER TABLE `characters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `charts`
--

DROP TABLE IF EXISTS `charts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `charts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `charts`
--

LOCK TABLES `charts` WRITE;
/*!40000 ALTER TABLE `charts` DISABLE KEYS */;
INSERT INTO `charts` VALUES (1,'FLO 차트');
/*!40000 ALTER TABLE `charts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (1,'KOREA'),(2,'USA');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'contenttypes','contenttype'),(8,'music','album'),(23,'music','albumchart'),(22,'music','albumemotion'),(21,'music','albumgenre'),(20,'music','albummood'),(9,'music','albumtype'),(10,'music','artist'),(11,'music','artisttype'),(12,'music','chart'),(13,'music','country'),(14,'music','emotion'),(15,'music','gender'),(16,'music','genre'),(17,'music','mood'),(18,'music','music'),(19,'music','musicdetail'),(2,'sessions','session'),(24,'storage','mylist'),(28,'storage','mylistmusic'),(27,'storage','storagealbum'),(26,'storage','storageartist'),(25,'storage','storagemusic'),(3,'user','character'),(7,'user','charactertasteartist'),(6,'user','charactertastechart'),(5,'user','charactertastegenre'),(4,'user','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-01-08 09:47:02.787503'),(2,'contenttypes','0002_remove_content_type_name','2021-01-08 09:47:02.819693'),(3,'music','0001_initial','2021-01-08 09:47:03.281488'),(4,'sessions','0001_initial','2021-01-08 09:47:03.438569'),(5,'user','0001_initial','2021-01-08 09:47:03.565410'),(6,'storage','0001_initial','2021-01-08 09:47:03.743513'),(7,'storage','0002_auto_20210108_1037','2021-01-08 10:37:16.820718');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emotions`
--

DROP TABLE IF EXISTS `emotions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emotions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emotions`
--

LOCK TABLES `emotions` WRITE;
/*!40000 ALTER TABLE `emotions` DISABLE KEYS */;
INSERT INTO `emotions` VALUES (1,'상쾌함');
/*!40000 ALTER TABLE `emotions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genders`
--

DROP TABLE IF EXISTS `genders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genders`
--

LOCK TABLES `genders` WRITE;
/*!40000 ALTER TABLE `genders` DISABLE KEYS */;
INSERT INTO `genders` VALUES (1,'Male'),(2,'Female'),(3,'Unknown');
/*!40000 ALTER TABLE `genders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genres` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genres`
--

LOCK TABLES `genres` WRITE;
/*!40000 ALTER TABLE `genres` DISABLE KEYS */;
INSERT INTO `genres` VALUES (1,'발라드'),(2,'힙합'),(3,'클래식'),(4,'해외소셜차트'),(5,'국내힙합'),(6,'어린이 동요'),(7,'EDM'),(8,'트로트');
/*!40000 ALTER TABLE `genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `moods`
--

DROP TABLE IF EXISTS `moods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `moods` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moods`
--

LOCK TABLES `moods` WRITE;
/*!40000 ALTER TABLE `moods` DISABLE KEYS */;
INSERT INTO `moods` VALUES (1,'드라이브 가자');
/*!40000 ALTER TABLE `moods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `music_details`
--

DROP TABLE IF EXISTS `music_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `music_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `lyric` longtext NOT NULL,
  `composer` varchar(10) DEFAULT NULL,
  `lyricist` varchar(10) DEFAULT NULL,
  `arrangement` varchar(10) DEFAULT NULL,
  `is_rated_r` tinyint(1) NOT NULL,
  `play_count` int NOT NULL,
  `music_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `music_id` (`music_id`),
  CONSTRAINT `music_details_music_id_0353afe6_fk_musics_id` FOREIGN KEY (`music_id`) REFERENCES `musics` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `music_details`
--

LOCK TABLES `music_details` WRITE;
/*!40000 ALTER TABLE `music_details` DISABLE KEYS */;
INSERT INTO `music_details` VALUES (1,'lyric',NULL,NULL,NULL,1,13323,1),(2,'lyric',NULL,NULL,NULL,1,192133,2),(3,'lyric',NULL,NULL,NULL,1,2123,3),(4,'lyric',NULL,NULL,NULL,1,1210,4),(5,'lyric',NULL,NULL,NULL,1,10432,5),(6,'lyric',NULL,NULL,NULL,1,42343,6),(7,'lyric',NULL,NULL,NULL,1,32324,7),(8,'lyric',NULL,NULL,NULL,1,534634,8),(9,'lyric',NULL,NULL,NULL,1,576571,9),(10,'lyric',NULL,NULL,NULL,1,57567,10),(11,'lyric',NULL,NULL,NULL,1,2313,11),(12,'lyric',NULL,NULL,NULL,1,34125,12),(13,'lyric',NULL,NULL,NULL,0,1343,13),(14,'lyric',NULL,NULL,NULL,0,32142,14),(15,'lyric',NULL,NULL,NULL,1,13512,15),(16,'lyric',NULL,NULL,NULL,0,42124,16),(17,'lyric',NULL,NULL,NULL,1,12421,17),(18,'lyric',NULL,NULL,NULL,0,21343,18),(19,'lyric',NULL,NULL,NULL,1,3525,19),(20,'lyric',NULL,NULL,NULL,1,32452,20),(21,'lyric',NULL,NULL,NULL,0,32143,21),(22,'lyric',NULL,NULL,NULL,1,10000,22),(23,'lyric',NULL,NULL,NULL,0,4535,23),(24,'lyric',NULL,NULL,NULL,1,45304,24),(25,'lyric',NULL,NULL,NULL,1,13323,25),(26,'lyric',NULL,NULL,NULL,1,19233,26),(27,'lyric',NULL,NULL,NULL,1,2123,27),(28,'lyric',NULL,NULL,NULL,1,1210,28),(29,'lyric',NULL,NULL,NULL,1,10232,29),(30,'lyric',NULL,NULL,NULL,1,42343,30),(31,'lyric',NULL,NULL,NULL,1,32324,31),(32,'lyric',NULL,NULL,NULL,1,5334,32),(33,'lyric',NULL,NULL,NULL,1,576571,33),(34,'lyric',NULL,NULL,NULL,1,57567,34),(35,'lyric',NULL,NULL,NULL,1,234113,35),(36,'lyric',NULL,NULL,NULL,1,34125,36),(37,'lyric',NULL,NULL,NULL,0,1343,37),(38,'lyric',NULL,NULL,NULL,0,32142,38),(39,'lyric',NULL,NULL,NULL,1,13512,39),(40,'lyric',NULL,NULL,NULL,0,42124,40),(41,'lyric',NULL,NULL,NULL,1,12421,41),(42,'lyric',NULL,NULL,NULL,0,21343,42),(43,'lyric',NULL,NULL,NULL,1,3535,43),(44,'lyric',NULL,NULL,NULL,1,32452,44),(45,'lyric',NULL,NULL,NULL,0,32143,45),(46,'lyric',NULL,NULL,NULL,1,34005,46),(47,'lyric',NULL,NULL,NULL,0,45355,47),(48,'lyric',NULL,NULL,NULL,1,45543,48),(49,'lyric',NULL,NULL,NULL,1,3245,49),(50,'lyric',NULL,NULL,NULL,0,32143,50),(51,'lyric',NULL,NULL,NULL,1,34505,51),(52,'lyric',NULL,NULL,NULL,0,45345,52),(53,'lyric',NULL,NULL,NULL,1,450054,53),(54,'lyric',NULL,NULL,NULL,1,13323,54),(55,'lyric',NULL,NULL,NULL,1,19233,55),(56,'lyric',NULL,NULL,NULL,1,2123,56),(57,'lyric',NULL,NULL,NULL,1,1210,57),(58,'lyric',NULL,NULL,NULL,1,10232,58),(59,'lyric',NULL,NULL,NULL,1,42343,59),(60,'lyric',NULL,NULL,NULL,1,32324,60),(61,'lyric',NULL,NULL,NULL,1,534634,61),(62,'lyric',NULL,NULL,NULL,1,576571,62),(63,'lyric',NULL,NULL,NULL,1,57567,63),(64,'lyric',NULL,NULL,NULL,1,234113,64),(65,'lyric',NULL,NULL,NULL,1,34125,65),(66,'lyric',NULL,NULL,NULL,0,1343,66),(67,'lyric',NULL,NULL,NULL,0,32142,67),(68,'lyric',NULL,NULL,NULL,1,13512,68),(69,'lyric',NULL,NULL,NULL,0,42124,69),(70,'lyric',NULL,NULL,NULL,1,12421,70);
/*!40000 ALTER TABLE `music_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `musics`
--

DROP TABLE IF EXISTS `musics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `musics` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `streaming_url` varchar(2000) NOT NULL,
  `album_id` int NOT NULL,
  `artist_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `musics_album_id_a18e3945_fk_albums_id` (`album_id`),
  KEY `musics_artist_id_347944ba_fk_artists_id` (`artist_id`),
  CONSTRAINT `musics_album_id_a18e3945_fk_albums_id` FOREIGN KEY (`album_id`) REFERENCES `albums` (`id`),
  CONSTRAINT `musics_artist_id_347944ba_fk_artists_id` FOREIGN KEY (`artist_id`) REFERENCES `artists` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `musics`
--

LOCK TABLES `musics` WRITE;
/*!40000 ALTER TABLE `musics` DISABLE KEYS */;
INSERT INTO `musics` VALUES (1,'Kiss Me','https://developer.apple.com/streaming/examples/',1,1),(2,'Like That','https://developer.apple.com/streaming/examples/',2,2),(3,'Text Me','https://developer.apple.com/streaming/examples/',3,1),(4,'Say So','https://developer.apple.com/streaming/examples/',4,3),(5,'배고프다니까요?!','https://developer.apple.com/streaming/examples/',46,4),(6,'웃어? 웃음이 나와?!','https://developer.apple.com/streaming/examples/',45,5),(7,'애럼의 때늦은 캐롤','https://developer.apple.com/streaming/examples/',44,5),(8,'배가고파','https://developer.apple.com/streaming/examples/',43,6),(9,'야식먹자','https://developer.apple.com/streaming/examples/',42,7),(10,'홀로그램','https://developer.apple.com/streaming/examples/',41,8),(11,'홀로 we_ro?!','https://developer.apple.com/streaming/examples/',40,9),(12,'웃어? 웃자? 나와?!','https://developer.apple.com/streaming/examples/',12,10),(13,'그리운 위코드(feat.A-Ram)','https://developer.apple.com/streaming/examples/',13,2),(14,'그립냐? 나도 그립다!','https://developer.apple.com/streaming/examples/',14,2),(15,'사랑해요 15기','https://developer.apple.com/streaming/examples/',15,2),(16,'고마워요 15기','https://developer.apple.com/streaming/examples/',16,2),(17,'함께해서 위고두?!','https://developer.apple.com/streaming/examples/',17,4),(18,'가치가자 위고두?!','https://developer.apple.com/streaming/examples/',18,5),(19,'함께해서 위고두?!','https://developer.apple.com/streaming/examples/',19,9),(20,'가치가자 위고두?!','https://developer.apple.com/streaming/examples/',20,10),(21,'Kiss Me','https://developer.apple.com/streaming/examples/',21,1),(22,'Like That','https://developer.apple.com/streaming/examples/',22,10),(23,'Text Me','https://developer.apple.com/streaming/examples/',23,11),(24,'Say So','https://developer.apple.com/streaming/examples/',24,12),(25,'배고프다니까요?!','https://developer.apple.com/streaming/examples/',25,14),(26,'웃어? 웃음이 나와?!','https://developer.apple.com/streaming/examples/',26,11),(27,'애럼의 때늦은 캐롤','https://developer.apple.com/streaming/examples/',27,8),(28,'배가고파','https://developer.apple.com/streaming/examples/',28,6),(29,'야식먹자','https://developer.apple.com/streaming/examples/',29,7),(30,'홀로그램','https://developer.apple.com/streaming/examples/',30,10),(31,'위로홀로?!','https://developer.apple.com/streaming/examples/',31,9),(32,'웃어? 웃자? 나와?!','https://developer.apple.com/streaming/examples/',32,8),(33,'그리운 위코드(feat.A-Ram)','https://developer.apple.com/streaming/examples/',33,7),(34,'그립냐? 나도 그립다!','https://developer.apple.com/streaming/examples/',34,5),(35,'사랑해요 15기','https://developer.apple.com/streaming/examples/',35,3),(36,'고마워요 15기','https://developer.apple.com/streaming/examples/',36,2),(37,'함께해서 위고두?!','https://developer.apple.com/streaming/examples/',37,4),(38,'가치가자 위고두?!','https://developer.apple.com/streaming/examples/',38,2),(39,'함께해서 위고두?!','https://developer.apple.com/streaming/examples/',39,4),(40,'가치가자 위고두?!','https://developer.apple.com/streaming/examples/',40,5),(41,'Kiss Me','https://developer.apple.com/streaming/examples/',10,6),(42,'Like That','https://developer.apple.com/streaming/examples/',9,7),(43,'Text Me','https://developer.apple.com/streaming/examples/',8,8),(44,'Say So','https://developer.apple.com/streaming/examples/',7,9),(45,'배고프다니까요?!','https://developer.apple.com/streaming/examples/',6,10),(46,'웃어? 웃음이 나와?!','https://developer.apple.com/streaming/examples/',5,11),(47,'애럼의 때늦은 캐롤','https://developer.apple.com/streaming/examples/',4,12),(48,'배가고파','https://developer.apple.com/streaming/examples/',3,13),(49,'야식먹자','https://developer.apple.com/streaming/examples/',2,14),(50,'홀로그램','https://developer.apple.com/streaming/examples/',1,15),(51,'위로홀로?!','https://developer.apple.com/streaming/examples/',3,2),(52,'웃어? 웃자? 나와?!','https://developer.apple.com/streaming/examples/',3,2),(53,'그리운 위코드(feat.A-Ram)','https://developer.apple.com/streaming/examples/',3,2),(54,'그립냐? 나도 그립다!','https://developer.apple.com/streaming/examples/',3,2),(55,'사랑해요 15기','https://developer.apple.com/streaming/examples/',3,2),(56,'고마워요 15기','https://developer.apple.com/streaming/examples/',3,2),(57,'함께해서 위고두?!','https://developer.apple.com/streaming/examples/',3,2),(58,'가치가자 위고두?!','https://developer.apple.com/streaming/examples/',11,2),(59,'함께해서 위고두?!','https://developer.apple.com/streaming/examples/',11,2),(60,'가치가자 위고두?!','https://developer.apple.com/streaming/examples/',11,2),(61,'수고했다 위고두?!','https://developer.apple.com/streaming/examples/',11,2),(62,'함께해서 위고두?!','https://developer.apple.com/streaming/examples/',11,2),(63,'보고싶다 위고두?!','https://developer.apple.com/streaming/examples/',11,2),(64,'2차 프로젝트!','https://developer.apple.com/streaming/examples/',15,11),(65,'수고 많았어요!','https://developer.apple.com/streaming/examples/',15,11),(66,'여러분의 성장이 뿌듯합니다!','https://developer.apple.com/streaming/examples/',15,11),(67,'애럼! 지금이라도 캐롤!','https://developer.apple.com/streaming/examples/',15,11),(68,'감사합니다 멘토님들','https://developer.apple.com/streaming/examples/',15,11),(69,'남기고 싶은 한 마디','https://developer.apple.com/streaming/examples/',15,11),(70,'사랑합니다','https://developer.apple.com/streaming/examples/',15,11);
/*!40000 ALTER TABLE `musics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mylist_musics`
--

DROP TABLE IF EXISTS `mylist_musics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mylist_musics` (
  `id` int NOT NULL AUTO_INCREMENT,
  `music_id` int NOT NULL,
  `mylist_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mylist_musics_music_id_b398f1d0_fk_musics_id` (`music_id`),
  KEY `mylist_musics_mylist_id_07f2e63f_fk_mylists_id` (`mylist_id`),
  CONSTRAINT `mylist_musics_music_id_b398f1d0_fk_musics_id` FOREIGN KEY (`music_id`) REFERENCES `musics` (`id`),
  CONSTRAINT `mylist_musics_mylist_id_07f2e63f_fk_mylists_id` FOREIGN KEY (`mylist_id`) REFERENCES `mylists` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mylist_musics`
--

LOCK TABLES `mylist_musics` WRITE;
/*!40000 ALTER TABLE `mylist_musics` DISABLE KEYS */;
/*!40000 ALTER TABLE `mylist_musics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mylists`
--

DROP TABLE IF EXISTS `mylists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mylists` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `character_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mylists_character_id_5840fbf1_fk_characters_id` (`character_id`),
  CONSTRAINT `mylists_character_id_5840fbf1_fk_characters_id` FOREIGN KEY (`character_id`) REFERENCES `characters` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mylists`
--

LOCK TABLES `mylists` WRITE;
/*!40000 ALTER TABLE `mylists` DISABLE KEYS */;
/*!40000 ALTER TABLE `mylists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storage_albums`
--

DROP TABLE IF EXISTS `storage_albums`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storage_albums` (
  `id` int NOT NULL AUTO_INCREMENT,
  `album_id` int NOT NULL,
  `character_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `storage_albums_album_id_f121686f_fk_albums_id` (`album_id`),
  KEY `storage_albums_character_id_251daf4f_fk_characters_id` (`character_id`),
  CONSTRAINT `storage_albums_album_id_f121686f_fk_albums_id` FOREIGN KEY (`album_id`) REFERENCES `albums` (`id`),
  CONSTRAINT `storage_albums_character_id_251daf4f_fk_characters_id` FOREIGN KEY (`character_id`) REFERENCES `characters` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storage_albums`
--

LOCK TABLES `storage_albums` WRITE;
/*!40000 ALTER TABLE `storage_albums` DISABLE KEYS */;
/*!40000 ALTER TABLE `storage_albums` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storage_artists`
--

DROP TABLE IF EXISTS `storage_artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storage_artists` (
  `id` int NOT NULL AUTO_INCREMENT,
  `artist_id` int NOT NULL,
  `character_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `storage_artists_artist_id_6aa903b8_fk_artists_id` (`artist_id`),
  KEY `storage_artists_character_id_6852db0c_fk_characters_id` (`character_id`),
  CONSTRAINT `storage_artists_artist_id_6aa903b8_fk_artists_id` FOREIGN KEY (`artist_id`) REFERENCES `artists` (`id`),
  CONSTRAINT `storage_artists_character_id_6852db0c_fk_characters_id` FOREIGN KEY (`character_id`) REFERENCES `characters` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storage_artists`
--

LOCK TABLES `storage_artists` WRITE;
/*!40000 ALTER TABLE `storage_artists` DISABLE KEYS */;
/*!40000 ALTER TABLE `storage_artists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storage_musics`
--

DROP TABLE IF EXISTS `storage_musics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storage_musics` (
  `id` int NOT NULL AUTO_INCREMENT,
  `character_id` int NOT NULL,
  `music_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `storage_musics_character_id_9f88549e_fk_characters_id` (`character_id`),
  KEY `storage_musics_music_id_f85cad1c_fk_musics_id` (`music_id`),
  CONSTRAINT `storage_musics_character_id_9f88549e_fk_characters_id` FOREIGN KEY (`character_id`) REFERENCES `characters` (`id`),
  CONSTRAINT `storage_musics_music_id_f85cad1c_fk_musics_id` FOREIGN KEY (`music_id`) REFERENCES `musics` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storage_musics`
--

LOCK TABLES `storage_musics` WRITE;
/*!40000 ALTER TABLE `storage_musics` DISABLE KEYS */;
/*!40000 ALTER TABLE `storage_musics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `password` varchar(250) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `kakao_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'we_ro'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-08 10:38:59
