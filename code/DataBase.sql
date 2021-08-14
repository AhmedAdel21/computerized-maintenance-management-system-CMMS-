-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 25, 2020 at 01:49 AM
-- Server version: 8.0.18
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `login`
--

-- --------------------------------------------------------

--
-- Table structure for table `conclusion`
--

CREATE TABLE `conclusion` (
  `inspectoinOrNot` int(11) NOT NULL,
  `acceptanceOrNot` int(11) NOT NULL,
  `acceptedWithReservation` int(1) NOT NULL,
  `remark` varchar(255) NOT NULL,
  `supplierName` varchar(255) NOT NULL,
  `supplierDesignation` varchar(255) NOT NULL,
  `supplierDate` date NOT NULL,
  `hospitalRepresentativeName` varchar(255) NOT NULL,
  `hospitalRepresentativeDesignation` varchar(255) NOT NULL,
  `hospitalRepresentativeDate` date NOT NULL,
  `EqSN` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `conclusion`
--

INSERT INTO `conclusion` (`inspectoinOrNot`, `acceptanceOrNot`, `acceptedWithReservation`, `remark`, `supplierName`, `supplierDesignation`, `supplierDate`, `hospitalRepresentativeName`, `hospitalRepresentativeDesignation`, `hospitalRepresentativeDate`, `EqSN`) VALUES
(0, 0, 1, 'Good', 'Ahmed Mohammed', 'Sales man', '2016-02-08', 'Ahmed Alnouby', 'Clinical Engineer', '2016-02-08', 1),
(0, 0, 1, 'Good', 'Ahmed Abdulla', 'Sales man', '2016-02-08', 'Ahmed Alnouby', 'Clinical Engineer', '2016-02-08', 3),
(0, 0, 1, 'Good', 'Ahmed Hossam', 'Sales man', '2016-02-08', 'Ahmed Alnouby', 'Clinical Engineer', '2016-02-08', 4),
(0, 0, 1, 'Good', 'Ahmed Hamada', 'Sales man', '2016-02-08', 'Ahmed Adel', 'Clinical Engineer', '2016-02-08', 5),
(0, 0, 1, 'Good', 'Ahmed Mohammed', 'Sales man', '2016-02-08', 'Ahmed Adel', 'Clinical Engineer', '2016-02-08', 6),
(0, 0, 0, 'Good', 'Hossam Mohammed', 'Sales man', '2016-02-08', 'Ahmed Adel', 'Clinical Engineer', '2016-02-08', 8),
(0, 0, 1, 'Good', 'Ahmad Adel', 'Sales man', '2016-02-08', 'Ahmed Elnouby', 'Clinical Engineer', '2016-02-08', 9),
(0, 0, 1, 'Good', 'Ahmad Adel', 'Sales man', '2016-02-08', 'Ahmed Elnouby', 'Clinical Engineer', '2016-02-08', 10),
(0, 0, 1, 'Good', 'Hossam Mohammed', 'Sales man', '2016-02-08', 'Ahmed Elnouby', 'Clinical Engineer', '2016-02-08', 11),
(0, 0, 1, 'Good', 'Malek Ezzat', 'Sales man', '2016-02-08', 'Ahmed Elnouby', 'Clinical Engineer', '2016-02-08', 12),
(0, 0, 0, 'Good', 'Ahmed Hossam', 'Sales man', '2016-02-08', 'Ahmed Elnouby', 'Clinical Engineer', '2016-02-08', 14),
(0, 0, 1, 'Good', 'Mohammed Hossam', 'Sales man', '2016-02-08', 'Ahmed Elnouby', 'Clinical Engineer', '2016-02-08', 15),
(0, 0, 1, 'Good', 'Donia Salah', 'Sales man', '2016-02-08', 'Ahmed Adel', 'Clinical Engineer', '2016-02-08', 16),
(0, 0, 1, 'Good', 'Ahmed Hossam', 'Sales man', '2016-02-08', 'Ahmed Adel', 'Clinical Engineer', '2016-02-08', 17),
(0, 0, 1, 'Good', 'Ahmed Hosny', 'Sales man', '2016-02-08', 'Ahmed Adel', 'Clinical Engineer', '2016-02-08', 18),
(0, 0, 0, 'Good', 'Ziad Salem', 'Sales Man', '2019-06-10', 'Karim Hamdy', 'Clinical Engineer', '2019-06-10', 19),
(0, 0, 0, 'Good', 'Ali Abdelrahman', 'Sales Man', '2019-07-01', 'Karim Hamdy', 'Clinical Engineer', '2019-07-01', 20),
(0, 0, 0, 'Good', 'Alaa Mohsen', 'Sales Man', '2019-07-10', 'Karim Hamdy', 'Clinical Engineer', '2019-07-10', 21),
(0, 0, 0, 'Good', 'Alaa Mohsen', 'Sales Man', '2019-07-18', 'Karim Hamdy', 'Clinical Engineer', '2019-07-18', 22),
(0, 0, 0, 'Good', 'Haitham Ahmed', 'Sales Man', '2016-02-10', 'Amgad Ezzat', 'Clinical Engineer', '2016-02-10', 23),
(0, 0, 0, 'Good', 'Sameh Farag', 'Sales Man', '2017-03-10', 'Mahmoud Fathi', 'Clinical Engineer', '2017-03-10', 24),
(0, 0, 0, 'Good', 'Sherif Ahmed', 'Sales Man', '2019-03-10', 'Mazen Salem', 'Clinical Engineer', '2019-03-10', 25),
(0, 0, 0, 'Good', 'Shaker Mahmoud', 'Sales Man', '2019-09-10', 'Hossam Ibrahim', 'Clinical Engineer', '2019-09-10', 26),
(0, 0, 1, 'd', 'd', 'd', '2000-01-01', 'd', 'd', '2000-01-01', 2222222);

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `Dname` varchar(255) NOT NULL,
  `Dnumber` int(11) NOT NULL DEFAULT '0',
  `floor` int(11) NOT NULL,
  `rooms` int(11) NOT NULL,
  `number of eqs` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`Dname`, `Dnumber`, `floor`, `rooms`, `number of eqs`) VALUES
('Emergency', 0, 0, 2, 10),
('Cardiology', 1, 1, 2, 10),
('Surgery', 2, 2, 3, 10);

-- --------------------------------------------------------

--
-- Table structure for table `dialy_inspection`
--

CREATE TABLE `dialy_inspection` (
  `row1` int(11) NOT NULL,
  `row2` int(11) NOT NULL,
  `row3` int(11) NOT NULL,
  `row4` int(11) NOT NULL,
  `row5` int(11) NOT NULL,
  `row6` int(11) NOT NULL,
  `row7` int(11) NOT NULL,
  `row8` int(11) NOT NULL,
  `row9` int(11) NOT NULL,
  `row10` int(11) NOT NULL,
  `row11` int(11) NOT NULL,
  `row12` int(11) NOT NULL,
  `row13` int(11) NOT NULL,
  `row14` int(11) NOT NULL,
  `row15` int(11) NOT NULL,
  `row16` int(11) NOT NULL,
  `row17` int(11) NOT NULL,
  `row18` int(11) NOT NULL,
  `row19` int(11) NOT NULL,
  `ins` int(11) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dialy_inspection`
--

INSERT INTO `dialy_inspection` (`row1`, `row2`, `row3`, `row4`, `row5`, `row6`, `row7`, `row8`, `row9`, `row10`, `row11`, `row12`, `row13`, `row14`, `row15`, `row16`, `row17`, `row18`, `row19`, `ins`, `time`) VALUES
(0, 0, 0, 0, 1, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 19, '2020-05-25 00:42:58'),
(0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, '2020-05-25 00:44:15'),
(0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, '2020-05-25 00:45:15'),
(0, 0, 0, 0, 1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, '2020-05-25 00:47:05'),
(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, '2020-05-25 00:48:26'),
(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, '2020-05-25 00:49:14'),
(0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, '2020-05-25 00:51:07'),
(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, '2020-05-25 00:53:01');

-- --------------------------------------------------------

--
-- Table structure for table `equipment`
--

CREATE TABLE `equipment` (
  `serialNumber` int(11) NOT NULL DEFAULT '0',
  `name` varchar(255) NOT NULL,
  `model` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `manufacturer` varchar(255) NOT NULL,
  `riskClassification` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  `department` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `equipment`
--

INSERT INTO `equipment` (`serialNumber`, `name`, `model`, `brand`, `manufacturer`, `riskClassification`, `description`, `department`) VALUES
(1, 'defibrillator', 'HEARTSTART XL', 'Philips', 'china', 2, 'defibrillator', 0),
(3, 'ecg machine', 'CARDIOVIT AT-102', 'Philips', 'china', 1, 'ecg machine', 0),
(4, 'Portable electric suction device', 'MAXI ASPEED 6. 4P', 'Philips', 'china', 2, 'Portable electric suction device', 0),
(5, 'monitor', 'PM 12', 'Philips', 'china', 1, 'monitor', 0),
(6, 'Electric syringe', 'INJECTOMAT AGILIA IS', 'Philips', 'china', 2, 'Electric syringe', 0),
(8, 'Anesthesia Machine', 'AVANCE CS2', 'Philips', 'china', 2, 'Anesthesia Machine', 2),
(9, 'Surgical and Exam Lights', '490 S', 'Philips', 'china', 1, 'Surgical and Exam Lights', 2),
(10, 'Surgical Tables', 'EASY220', 'Philips', 'china', 1, 'Surgical Tables', 2),
(11, 'Monitor', 'B850', 'Philips', 'china', 1, 'Monitor', 2),
(12, 'Defibrillator', 'AED Plus', 'Philips', 'china', 3, 'Defibrillator', 2),
(14, 'Suction Unit', 'MaxiA speed 6.4p', 'Philips', 'china', 2, 'Suction Unit', 1),
(15, 'monitor', 'Ultraview SL2700', 'Philips', 'china', 2, 'monitor', 1),
(16, 'SPO2 Monitoring System', 'premier4000 ', 'Philips', 'china', 2, 'SPO2 Monitoring System', 1),
(17, 'Ventilator', 'Extend XT', 'Philips', 'china', 2, 'Ventilator', 1),
(18, 'ECG', 'Cardiovit At/102', 'Philips', 'china', 2, 'ECG', 1),
(19, 'Ventilator', 'SV 600', 'Medtronic', 'USA', 2, 'Ventilator', 2),
(20, 'Diathermy', 'Force FX-8C', 'Siemens Healthineers', 'Germany', 3, 'Diathermy', 2),
(21, 'Surgical Booms', 'SB 800', 'STERIS', 'USA', 1, 'Surgical Booms', 2),
(22, 'Surgical Aspirator', 'HOSPIVAC 350', 'STERIS', 'USA', 2, 'Surgical Aspirator', 2),
(23, 'Gypsum Saw', 'FMM250Q', 'Philips ', 'USA', 3, 'Gypsum Saw', 0),
(24, 'Ventilator', 'E 360T', 'Medtronic', 'USA', 1, 'Ventilator', 0),
(25, 'Diathermy', 'E 360T', 'Siemens Healthineers', 'Germany', 2, 'Diathermy', 0),
(26, 'Mobile Event', 'Triology 202', 'Steris ', 'USA', 3, 'Mobile Event', 1);

-- --------------------------------------------------------

--
-- Table structure for table `logingin`
--

CREATE TABLE `logingin` (
  `username` varchar(250) DEFAULT NULL,
  `pass` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `logingin`
--

INSERT INTO `logingin` (`username`, `pass`) VALUES
('dola', 'dola'),
('zz', 'zz'),
('zzz', 'zzz'),
('nooby', 'nooby'),
('nooby', 'nooby'),
('aa', 'aa'),
('aam', 'aa'),
('oijk', 'jknjk'),
('nooby0', ',mnm,');

-- --------------------------------------------------------

--
-- Table structure for table `physical inspection`
--

CREATE TABLE `physical inspection` (
  `batchSize` int(11) NOT NULL,
  `sampleSize` int(11) NOT NULL,
  `defectsCount` int(11) NOT NULL,
  `buttongroup1` int(11) NOT NULL,
  `buttongroup2` int(11) NOT NULL,
  `buttongroup3` int(11) NOT NULL,
  `buttongroup4` int(11) NOT NULL,
  `buttongroup5` int(11) NOT NULL,
  `buttongroup6` int(11) NOT NULL,
  `buttongroup7` int(11) NOT NULL,
  `problem` varchar(255) NOT NULL,
  `remarks` varchar(255) NOT NULL,
  `suggestion` varchar(255) NOT NULL,
  `EqSN` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `physical inspection`
--

INSERT INTO `physical inspection` (`batchSize`, `sampleSize`, `defectsCount`, `buttongroup1`, `buttongroup2`, `buttongroup3`, `buttongroup4`, `buttongroup5`, `buttongroup6`, `buttongroup7`, `problem`, `remarks`, `suggestion`, `EqSN`) VALUES
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 0),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 3),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 4),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 5),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 6),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 8),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 9),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 10),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 11),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 12),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 14),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 15),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 16),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 17),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Nothing', 'Nothing', 18),
(1, 1, 0, -1, -1, 0, 0, 0, 0, 0, 'Nothing', 'Good', 'Nothing', 19),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Good', 'Nothing', 20),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Good', 'Nothing', 21),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Good', 'Nothing', 22),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Good', 'Nothing', 23),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Good', 'Nothing', 24),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Good', 'Nothing', 25),
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Nothing', 'Good', 'Nothing', 26),
(3, 3, 3, -1, -1, 0, 0, 0, 0, 0, 'no heart', 'd', 'd', 2222222);

-- --------------------------------------------------------

--
-- Table structure for table `purchase`
--

CREATE TABLE `purchase` (
  `supplier` varchar(255) NOT NULL,
  `supplierAddress` text NOT NULL,
  `supplierContactPerson` varchar(255) NOT NULL,
  `supplierContactNO` int(11) NOT NULL,
  `authorised` varchar(255) NOT NULL,
  `authorisedAddress` text NOT NULL,
  `authorisedContactPerson` varchar(255) NOT NULL,
  `authorisedContactNO` int(11) NOT NULL,
  `localPurchaseOrderNO` int(11) NOT NULL,
  `purchaseDate` date NOT NULL,
  `warrantyStartDate` date NOT NULL,
  `purchasePrice` int(11) NOT NULL,
  `deliveryNO` int(11) NOT NULL,
  `warrantyEndDate` date NOT NULL,
  `EqSN` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `purchase`
--

INSERT INTO `purchase` (`supplier`, `supplierAddress`, `supplierContactPerson`, `supplierContactNO`, `authorised`, `authorisedAddress`, `authorisedContactPerson`, `authorisedContactNO`, `localPurchaseOrderNO`, `purchaseDate`, `warrantyStartDate`, `purchasePrice`, `deliveryNO`, `warrantyEndDate`, `EqSN`) VALUES
('Egyption Group ', '124 Port Said St. sayeda Zainab', 'Ahmed Mohammed', 1111111111, 'Egyption Group ', '124 Port Said St. sayeda Zainab', 'Ahmed Mohammed', 1111111111, 1234, '2016-02-08', '2016-02-08', 44500, 22233, '2018-02-08', 0),
('Glynchi Group ', '144 Port Said St. sayeda Zainab', 'Ahmed Abdulla', 1111111211, 'Glynchi Group ', '144 Port Said St. sayeda Zainab', 'Ahmed Abdulla', 1111111211, 1323, '2016-02-08', '2016-02-08', 19950, 24433, '2018-02-08', 3),
('Floya Group ', '104 Port Said St. sayeda Zainab', 'Ahmed Hossam', 1111111311, 'Glynchi Group ', '144 Port Said St. sayeda Zainab', 'Ahmed Hossam', 1111111311, 1326, '2016-02-08', '2016-02-08', 6290, 24432, '2018-02-08', 4),
('El ezaby ', '104 Port Said St. sayeda Zainab', 'Ahmed hamada', 1111111411, 'None', 'None', 'None', 0, 981326, '2016-02-08', '2016-02-08', 516, 24498, '2016-02-08', 5),
('Egyptian Group', '124 Port Said St. sayeda Zainab', 'Ahmed Mohammed', 1111111111, 'None', 'None', 'None', 0, 9815, '2016-02-08', '2016-02-08', 529, 24667, '2016-02-08', 6),
('GE Healthcare', '123 Port Said St. sayeda Zainab', 'Hossam Mohammed', 1111111121, 'Dreams Medical', '423 Port Said St. sayeda Zainab', 'Gihad', 1111111120, 981567, '2016-02-08', '2016-02-08', 30000, 20667, '2019-02-08', 8),
('STERIS', '13 Port Said St. sayeda Zainab', 'Ahmad Adel', 1111111131, 'Dreams Medical', '423 Port Said St. sayeda Zainab', 'Gihad Mohammed', 1111111120, 6765, '2016-02-08', '2016-02-08', 7000, 20452, '2018-02-08', 9),
('STERIS', '13 Port Said St. sayeda Zainab', 'Ahmad Adel', 1111111131, 'Operating Theatre Specialists', '42 Port Said St. sayeda Zainab', 'Hossam Sadiq', 1111111128, 67651, '2016-02-08', '2016-02-08', 25000, 20432, '2018-02-08', 10),
('GE Healthcare', '123 Port Said St. sayeda Zainab', 'Hossam Mohammed', 1111111121, 'Dreams Medical', '423 Port Said St. sayeda Zainab', 'Gihad Mohammed', 1111111120, 6765231, '2016-02-08', '2016-02-08', 4000, 22432, '2018-02-08', 11),
('Philips Healthcare', '93 Port Said St. sayeda Zainab', 'Malek Ezzat', 1111121121, 'Dreams Medical', '423 Port Said St. sayeda Zainab', 'Gihad Mohammed', 1111111120, 6725231, '2016-02-08', '2016-02-08', 1275, 22482, '2019-02-08', 12),
('Floya Group ', '104 Port Said St. sayeda Zainab', 'Ahmed Hossam', 1111111311, 'Floya Group ', '104 Port Said St. sayeda Zainab', 'Ahmed Hossam', 1111111311, 672631, '2016-02-08', '2016-02-08', 11530, 82482, '2018-02-08', 14),
('Geseka Group ', '194 Port Said St. sayeda Zainab', 'Mohammed Hossam', 1111111311, 'None', 'None', 'None', 0, 67269, '2016-02-08', '2016-02-08', 100, 82489, '2016-02-08', 15),
('international Group ', '184 Port Said St. sayeda Zainab', 'Donia Salah', 1111114411, 'international Group ', '184 Port Said St. sayeda Zainab', 'Nancy Salah', 1111114417, 672998, '2016-02-08', '2016-02-08', 4000, 82535, '2018-02-08', 16),
('Egyption Group ', '124 Port Said St. sayeda Zainab', 'Ahmed Mohammed', 1111111111, 'None', 'None', 'None', 0, 12998, '2016-02-08', '2016-02-08', 9000, 82534, '2016-02-08', 17),
('Glyonji Group ', '16 Port Said St. sayeda Zainab', 'Ahmed Hosny', 1119111118, 'Glyonji Group ', '16 Port Said St. sayeda Zainab', 'Ahmed Hosny', 1119111118, 1292222, '2016-02-08', '2016-02-08', 10000, 82532, '2018-02-08', 18),
('Medtronic Egypt ', 'First New Cairo', 'Malak Abdelrahman', 1223456789, 'Medtronic Egypt ', 'First New Cairo', 'Malak Abdelrahman', 1223456789, 1, '2019-06-25', '2019-06-28', 3000, 1, '2022-06-28', 19),
('Siemens Healthineers Egypt ', 'Maadi Technology Park', 'Tarek El-Ashraf', 1226677889, 'Siemens Healthineers Egypt ', 'Maadi Technology Park', 'Tarek El-Ashraf', 1226677889, 2, '2019-07-01', '2019-07-05', 5000, 2, '2022-07-05', 20),
('Dreams Medical Egypt ', '14 Mokately Ramadan, Hassan Ma\'moun, Nasr City', 'Mohamed Ali', 1018709099, 'Dreams Medical Egypt ', '14 Mokately Ramadan, Hassan Ma\'moun, Nasr City', 'Mohamed Ali', 1018709099, 1, '2019-07-05', '2019-07-10', 2000, 1, '2022-07-10', 21),
('Dreams Medical Egypt ', '14 Mokately Ramadan, Hassan Ma\'moun, Nasr City', 'Mohamed Ali', 1018709099, 'Dreams Medical Egypt ', '14 Mokately Ramadan, Hassan Ma\'moun, Nasr City', 'Mohamed Ali', 1018709099, 2, '2019-07-15', '2019-07-18', 2000, 2, '2022-07-18', 22),
('Dreams Medical Egypt ', '14 Mokately Ramadan, Hassan Ma\'moun, Nasr City', 'Mostafa Ayman', 1017596843, 'Dreams Medical Egypt ', '14 Mokately Ramadan, Hassan Ma\'moun, Nasr City', 'Mostafa Ayman', 1017596843, 3, '2016-02-08', '2016-02-10', 50, 3, '2019-02-10', 23),
('Medtronic Egypt ', 'First, New Cairo', 'Yehia Mohamed', 1005506601, 'Medtronic Egypt ', 'First, New Cairo', 'Yehia Mohamed', 1005506601, 2, '2017-03-08', '2017-03-10', 5000, 2, '2020-03-10', 24),
('Siemens Healthineers Egypt', 'Maadi Technology Park', 'Tarek El-Ashraf', 1226677889, 'Siemens Healthineers Egypt', 'Maadi Technology Park', 'Tarek El-Ashraf', 1226677889, 3, '2018-03-08', '2018-03-10', 4000, 3, '2021-03-10', 25),
('Dreams Care Egypt', '14 Mokately Ramadan, Hassan Ma\'moun, Nasr City', 'Mostafa Mohamed', 1117775689, 'Dreams Care Egypt', '14 Mokately Ramadan, Hassan Ma\'moun, Nasr City', 'Mostafa Mohamed', 1117775689, 3, '2018-09-08', '2018-09-10', 2500, 3, '2021-09-10', 26);

-- --------------------------------------------------------

--
-- Table structure for table `report`
--

CREATE TABLE `report` (
  `data1` varchar(250) DEFAULT NULL,
  `data2` varchar(250) DEFAULT NULL,
  `data3` varchar(250) DEFAULT NULL,
  `data4` varchar(250) DEFAULT NULL,
  `data5` varchar(250) DEFAULT NULL,
  `entering_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `report`
--

INSERT INTO `report` (`data1`, `data2`, `data3`, `data4`, `data5`, `entering_time`) VALUES
('clicked1', 'null', 'null', 'null', 'null', '2020-05-05 09:03:23'),
('clicked1', 'null', 'null', 'clicked4', 'null', '2020-05-05 09:03:23'),
('clicked1', 'clicked2', 'clicked3', 'clicked4', 'clicked5', '2020-05-05 09:04:13');

-- --------------------------------------------------------

--
-- Table structure for table `scrapping`
--

CREATE TABLE `scrapping` (
  `Date` date NOT NULL,
  `Requested By` varchar(255) NOT NULL,
  `Department` varchar(255) NOT NULL,
  `Reasons for Disposition` varchar(500) NOT NULL,
  `Serial Number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `conclusion`
--
ALTER TABLE `conclusion`
  ADD PRIMARY KEY (`EqSN`),
  ADD UNIQUE KEY `EqSN` (`EqSN`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`Dnumber`),
  ADD UNIQUE KEY `Dnumber` (`Dnumber`);

--
-- Indexes for table `dialy_inspection`
--
ALTER TABLE `dialy_inspection`
  ADD PRIMARY KEY (`time`);

--
-- Indexes for table `equipment`
--
ALTER TABLE `equipment`
  ADD PRIMARY KEY (`serialNumber`),
  ADD UNIQUE KEY `serialNumber` (`serialNumber`);

--
-- Indexes for table `physical inspection`
--
ALTER TABLE `physical inspection`
  ADD PRIMARY KEY (`EqSN`),
  ADD UNIQUE KEY `EqSN` (`EqSN`);

--
-- Indexes for table `purchase`
--
ALTER TABLE `purchase`
  ADD PRIMARY KEY (`EqSN`),
  ADD UNIQUE KEY `EqSN` (`EqSN`);

--
-- Indexes for table `scrapping`
--
ALTER TABLE `scrapping`
  ADD PRIMARY KEY (`Serial Number`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
