-- MySQL dump 10.13  Distrib 5.5.49, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: garak_db
-- ------------------------------------------------------
-- Server version	5.5.49-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add store',1,'add_store'),(2,'Can change store',1,'change_store'),(3,'Can delete store',1,'delete_store'),(4,'Can add unit',2,'add_unit'),(5,'Can change unit',2,'change_unit'),(6,'Can delete unit',2,'delete_unit'),(7,'Can add grade',3,'add_grade'),(8,'Can change grade',3,'change_grade'),(9,'Can delete grade',3,'delete_grade'),(10,'Can add item',4,'add_item'),(11,'Can change item',4,'change_item'),(12,'Can delete item',4,'delete_item'),(13,'Can add order',5,'add_order'),(14,'Can change order',5,'change_order'),(15,'Can delete order',5,'delete_order'),(16,'Can add ordered_item',6,'add_ordered_item'),(17,'Can change ordered_item',6,'change_ordered_item'),(18,'Can delete ordered_item',6,'delete_ordered_item'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add permission',8,'add_permission'),(23,'Can change permission',8,'change_permission'),(24,'Can delete permission',8,'delete_permission'),(25,'Can add group',9,'add_group'),(26,'Can change group',9,'change_group'),(27,'Can delete group',9,'delete_group'),(28,'Can add user',10,'add_user'),(29,'Can change user',10,'change_user'),(30,'Can delete user',10,'delete_user'),(31,'Can add content type',11,'add_contenttype'),(32,'Can change content type',11,'change_contenttype'),(33,'Can delete content type',11,'delete_contenttype'),(34,'Can add session',12,'add_session'),(35,'Can change session',12,'change_session'),(36,'Can delete session',12,'delete_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$24000$7nPeERGjPghG$nohKZNBkerF/FExE7V+2rc6WfPTdGb/0X6mxdKM1r8s=','2016-07-06 15:45:10',1,'admin','','','',1,1,'2016-07-06 15:44:45');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-07-06 15:45:20','1','grade: 1등급',1,'Added.',3,1),(2,'2016-07-06 15:47:15','1','Store: 봉수상회',1,'Added.',1,1),(3,'2016-07-06 15:47:35','1','Order: 가라데이터1',1,'Added.',5,1),(4,'2016-07-06 15:47:57','1','unit: box',1,'Added.',2,1),(5,'2016-07-06 15:48:04','2','unit: ton',1,'Added.',2,1),(6,'2016-07-06 15:48:55','1','item: 배추',1,'Added.',4,1),(7,'2016-07-06 15:49:23','1','Ordered_item: 30만원어치 경매 구매',1,'Added.',6,1),(8,'2016-07-06 15:49:25','1','Ordered_item: 30만원어치 경매 구매',2,'No fields changed.',6,1),(9,'2016-07-06 15:49:39','2','item: 젓갈',1,'Added.',4,1),(10,'2016-07-06 15:50:03','2','Ordered_item: 5톤 구매',1,'Added.',6,1),(11,'2016-07-06 15:50:45','2','Store: 서울청과',1,'Added.',1,1),(12,'2016-07-06 15:51:19','2','Order: 제품은 별로이나 관계를 만들기 위해 구매함',1,'Added.',5,1),(13,'2016-07-06 15:51:41','3','item: 사과',1,'Added.',4,1),(14,'2016-07-06 15:52:04','3','Ordered_item: 사과 100box구매',1,'Added.',6,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (7,'admin','logentry'),(9,'auth','group'),(8,'auth','permission'),(10,'auth','user'),(11,'contenttypes','contenttype'),(12,'sessions','session'),(3,'testapp','grade'),(4,'testapp','item'),(5,'testapp','order'),(6,'testapp','ordered_item'),(1,'testapp','store'),(2,'testapp','unit');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-07-06 15:44:28'),(2,'auth','0001_initial','2016-07-06 15:44:28'),(3,'admin','0001_initial','2016-07-06 15:44:28'),(4,'admin','0002_logentry_remove_auto_add','2016-07-06 15:44:28'),(5,'contenttypes','0002_remove_content_type_name','2016-07-06 15:44:28'),(6,'auth','0002_alter_permission_name_max_length','2016-07-06 15:44:28'),(7,'auth','0003_alter_user_email_max_length','2016-07-06 15:44:28'),(8,'auth','0004_alter_user_username_opts','2016-07-06 15:44:28'),(9,'auth','0005_alter_user_last_login_null','2016-07-06 15:44:28'),(10,'auth','0006_require_contenttypes_0002','2016-07-06 15:44:28'),(11,'auth','0007_alter_validators_add_error_messages','2016-07-06 15:44:28'),(12,'sessions','0001_initial','2016-07-06 15:44:28'),(13,'testapp','0001_initial','2016-07-06 15:44:28');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ow1tzq9o2yzvvowu0l1klx0dj5ads3ve','MDNhYmJiMmFmZDY5YmNlNmE0YjllODE4NzIzOTBiM2ZiZTFmMTAyYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjczNzllZTJhMGNmN2IzZjBlZmY4ZjIyM2VkOWY2ZDQ2NTgzOWZkMmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-07-20 15:45:10');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_grade`
--

DROP TABLE IF EXISTS `testapp_grade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_grade` (
  `grade_id` int(11) NOT NULL AUTO_INCREMENT,
  `grade_name` varchar(100) NOT NULL,
  `grade_description` varchar(200) NOT NULL,
  PRIMARY KEY (`grade_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_grade`
--

LOCK TABLES `testapp_grade` WRITE;
/*!40000 ALTER TABLE `testapp_grade` DISABLE KEYS */;
INSERT INTO `testapp_grade` VALUES (1,'1등급','좋은것');
/*!40000 ALTER TABLE `testapp_grade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_item`
--

DROP TABLE IF EXISTS `testapp_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_item` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(100) NOT NULL,
  `item_description` varchar(200) NOT NULL,
  `item_unit_id` int(11) NOT NULL,
  PRIMARY KEY (`item_id`),
  KEY `testapp_item_7d8c7d6d` (`item_unit_id`),
  CONSTRAINT `testapp_item_item_unit_id_692f9423_fk_testapp_unit_unit_id` FOREIGN KEY (`item_unit_id`) REFERENCES `testapp_unit` (`unit_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_item`
--

LOCK TABLES `testapp_item` WRITE;
/*!40000 ALTER TABLE `testapp_item` DISABLE KEYS */;
INSERT INTO `testapp_item` VALUES (1,'배추','1box 단위로 거래되는 배추',1),(2,'젓갈','새우젓',2),(3,'사과','빨간사과',1);
/*!40000 ALTER TABLE `testapp_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_order`
--

DROP TABLE IF EXISTS `testapp_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_date` datetime NOT NULL,
  `order_total_amount` int(11) NOT NULL,
  `order_paid_amount` int(11) NOT NULL,
  `order_discounted_amount` int(11) NOT NULL,
  `order_outstanding_amount` int(11) NOT NULL,
  `order_notes` varchar(200) NOT NULL,
  `order_store_id` int(11) NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `testapp_order_a5c8672c` (`order_store_id`),
  CONSTRAINT `testapp_order_order_store_id_81f43887_fk_testapp_store_store_id` FOREIGN KEY (`order_store_id`) REFERENCES `testapp_store` (`store_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_order`
--

LOCK TABLES `testapp_order` WRITE;
/*!40000 ALTER TABLE `testapp_order` DISABLE KEYS */;
INSERT INTO `testapp_order` VALUES (1,'2016-07-06 15:47:02',1200000,100000,200000,300000,'가라데이터1',1),(2,'2016-07-01 21:00:00',5000000,1000000,200000,300000,'제품은 별로이나 관계를 만들기 위해 구매함',2);
/*!40000 ALTER TABLE `testapp_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_ordered_item`
--

DROP TABLE IF EXISTS `testapp_ordered_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_ordered_item` (
  `ordered_item_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordered_item_unit_price` int(11) NOT NULL,
  `ordered_item_qty` int(11) NOT NULL,
  `ordered_item_description` varchar(200) NOT NULL,
  `ordered_item_grade_id` int(11) NOT NULL,
  `ordered_item_item_id` int(11) NOT NULL,
  `ordered_item_order_id` int(11) NOT NULL,
  `ordered_item_unit_id` int(11) NOT NULL,
  PRIMARY KEY (`ordered_item_id`),
  KEY `testapp_ordered_item_grade_id_ba2553eb_fk_testapp_grade_grade_id` (`ordered_item_grade_id`),
  KEY `testapp_or_ordered_item_item_id_66f8773b_fk_testapp_item_item_id` (`ordered_item_item_id`),
  KEY `testapp_ordered_item_order_id_20b7a051_fk_testapp_order_order_id` (`ordered_item_order_id`),
  KEY `testapp_ordered_item_e626116c` (`ordered_item_unit_id`),
  CONSTRAINT `testapp_ordered_item_grade_id_ba2553eb_fk_testapp_grade_grade_id` FOREIGN KEY (`ordered_item_grade_id`) REFERENCES `testapp_grade` (`grade_id`),
  CONSTRAINT `testapp_ordered_item_order_id_20b7a051_fk_testapp_order_order_id` FOREIGN KEY (`ordered_item_order_id`) REFERENCES `testapp_order` (`order_id`),
  CONSTRAINT `testapp_or_ordered_item_item_id_66f8773b_fk_testapp_item_item_id` FOREIGN KEY (`ordered_item_item_id`) REFERENCES `testapp_item` (`item_id`),
  CONSTRAINT `testapp_or_ordered_item_unit_id_5aaa4c8b_fk_testapp_unit_unit_id` FOREIGN KEY (`ordered_item_unit_id`) REFERENCES `testapp_unit` (`unit_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_ordered_item`
--

LOCK TABLES `testapp_ordered_item` WRITE;
/*!40000 ALTER TABLE `testapp_ordered_item` DISABLE KEYS */;
INSERT INTO `testapp_ordered_item` VALUES (1,3000,100,'30만원어치 경매 구매',1,1,1,1),(2,1500000,5,'5톤 구매',1,2,1,2),(3,30000,100,'사과 100box구매',1,3,2,1);
/*!40000 ALTER TABLE `testapp_ordered_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_store`
--

DROP TABLE IF EXISTS `testapp_store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_store` (
  `store_id` int(11) NOT NULL AUTO_INCREMENT,
  `store_name` varchar(100) NOT NULL,
  `store_call` varchar(100) NOT NULL,
  `store_address` varchar(200) NOT NULL,
  `store_pic_name` varchar(200) NOT NULL,
  `store_description` varchar(200) NOT NULL,
  PRIMARY KEY (`store_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_store`
--

LOCK TABLES `testapp_store` WRITE;
/*!40000 ALTER TABLE `testapp_store` DISABLE KEYS */;
INSERT INTO `testapp_store` VALUES (1,'봉수상회','02-333-444','서울 송파구 가락동 230-33','최봉수','마린'),(2,'서울청과','02-356-77881','가락동 가락시장 103호','김새롬','가락시장내에 있는 청과상');
/*!40000 ALTER TABLE `testapp_store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_unit`
--

DROP TABLE IF EXISTS `testapp_unit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_unit` (
  `unit_id` int(11) NOT NULL AUTO_INCREMENT,
  `unit_name` varchar(100) NOT NULL,
  `unit_description` varchar(200) NOT NULL,
  PRIMARY KEY (`unit_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_unit`
--

LOCK TABLES `testapp_unit` WRITE;
/*!40000 ALTER TABLE `testapp_unit` DISABLE KEYS */;
INSERT INTO `testapp_unit` VALUES (1,'box','box'),(2,'ton','ton');
/*!40000 ALTER TABLE `testapp_unit` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-10 14:59:43
