-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 05, 2021 at 07:29 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `schoolregform`
--

-- --------------------------------------------------------

--
-- Table structure for table `resultsv2`
--

CREATE TABLE `resultsv2` (
  `Name` varchar(20) NOT NULL,
  `LastName` varchar(20) NOT NULL,
  `BirthDate` varchar(10) NOT NULL,
  `Gender` varchar(4) NOT NULL,
  `Ethnicity` varchar(20) NOT NULL,
  `EntryYear` varchar(4) NOT NULL,
  `Grade` varchar(2) NOT NULL,
  `Semester` varchar(2) NOT NULL,
  `appliedOrNot` int(1) NOT NULL,
  `StreetAddress` varchar(20) NOT NULL,
  `StreetAddressLine2` varchar(20) NOT NULL,
  `City` varchar(20) NOT NULL,
  `State` varchar(20) NOT NULL,
  `PostalNum` varchar(8) NOT NULL,
  `HomePhoneNum` varchar(20) NOT NULL,
  `CellPhoneNum` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `resultsv2`
--

INSERT INTO `resultsv2` (`Name`, `LastName`, `BirthDate`, `Gender`, `Ethnicity`, `EntryYear`, `Grade`, `Semester`, `appliedOrNot`, `StreetAddress`, `StreetAddressLine2`, `City`, `State`, `PostalNum`, `HomePhoneNum`, `CellPhoneNum`) VALUES
('Iliya', 'Yadegari', '22122008', 'male', 'Middle Eastern', '2008', '7', '5', 2, '9 Price House', 'britannia row', 'london', 'england', 'n7 yut', '07436635326', '07524435364'),
('Tom', 'Smith', '06041991', 'male', 'Asian', '4', '7', '5', 2, 'Grove street', '9 pric estate', 'London', 'England', 'n8 ytj', '0789433424', '0764235459');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
