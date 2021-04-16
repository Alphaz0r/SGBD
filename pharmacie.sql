-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 16 avr. 2021 à 20:03
-- Version du serveur :  10.4.17-MariaDB
-- Version de PHP : 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `pharmacie`
--

-- --------------------------------------------------------

--
-- Structure de la table `clients`
--

CREATE TABLE `clients` (
  `PK_client_id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(20) COLLATE utf8_bin NOT NULL,
  `first_name` varchar(20) COLLATE utf8_bin NOT NULL,
  `birth_date` date NOT NULL,
  `age` tinyint(4) NOT NULL,
  `rue` varchar(30) COLLATE utf8_bin NOT NULL,
  `house_number` varchar(5) COLLATE utf8_bin NOT NULL,
  `postcode` varchar(6) COLLATE utf8_bin NOT NULL,
  `email` varchar(30) COLLATE utf8_bin NOT NULL,
  `phone_number` varchar(20) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Déchargement des données de la table `clients`
--

INSERT INTO `clients` (`PK_client_id`, `name`, `first_name`, `birth_date`, `age`, `rue`, `house_number`, `postcode`, `email`, `phone_number`) VALUES
(16, 'NULL', 'QZDqzd', '0000-00-00', 127, '95', 'Des l', '5888b', '7855', 'tzeml;mes;f'),
(17, 'Vanbelle', 'Florian', '1997-10-02', 24, 'Rue des qzqzzzzz', '688', '458888', 'qmzdlijqed,sef', '044785203654'),
(18, 'anzkdnk', 'qz,qeld,f', '2020-12-11', 58, 'Des pazldzkd', '2654', '213654', 'dqzd,qlef', '149545212');

-- --------------------------------------------------------

--
-- Structure de la table `concentration`
--

CREATE TABLE `concentration` (
  `PK_concentration_id` bigint(20) UNSIGNED NOT NULL,
  `concentration_mg` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Déchargement des données de la table `concentration`
--

INSERT INTO `concentration` (`PK_concentration_id`, `concentration_mg`) VALUES
(1, 250),
(14, 366),
(15, 588),
(2, 600),
(3, 750),
(4, 1000),
(5, 1250),
(10, 2000),
(16, 26669);

-- --------------------------------------------------------

--
-- Structure de la table `drugs`
--

CREATE TABLE `drugs` (
  `PK_drug_id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(20) COLLATE utf8_bin NOT NULL,
  `description` varchar(60) COLLATE utf8_bin NOT NULL,
  `peremption_date` date NOT NULL,
  `price` double NOT NULL,
  `FK_concentration_id` bigint(20) UNSIGNED NOT NULL,
  `stock` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Déchargement des données de la table `drugs`
--

INSERT INTO `drugs` (`PK_drug_id`, `name`, `description`, `peremption_date`, `price`, `FK_concentration_id`, `stock`) VALUES
(2, 'DAFALGAN', 'Bah du Dafalgan', '2022-03-10', 2.5, 2, 100),
(3, 'DAFALGAN', 'Bah du Dafalgan', '2022-03-10', 5, 4, 500),
(4, 'IMODIUM', 'Bah du Imodium', '2024-06-13', 10, 2, 600),
(5, 'CLAMOXYL', 'Une description du Clamoxyl', '2023-08-10', 23.5, 5, 900),
(11, 'QZdqzd', 'qD', '2020-12-12', 444, 10, 588),
(12, 'issou', 'le issou', '3000-05-05', 999, 10, 5553),
(13, 'qzd', 'qzd', '2012-12-30', 52, 10, 25),
(14, 'lol', 'lol', '2033-05-05', 588, 2, 600);

-- --------------------------------------------------------

--
-- Structure de la table `facture`
--

CREATE TABLE `facture` (
  `PK_facture_id` bigint(20) UNSIGNED NOT NULL,
  `FK_client_id` bigint(20) UNSIGNED DEFAULT NULL,
  `date_creation` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Déchargement des données de la table `facture`
--

INSERT INTO `facture` (`PK_facture_id`, `FK_client_id`, `date_creation`) VALUES
(11, 17, '2021-04-11 12:36:23');

-- --------------------------------------------------------

--
-- Structure de la table `facture_row`
--

CREATE TABLE `facture_row` (
  `PK_fd_id` bigint(20) UNSIGNED NOT NULL,
  `item_count` int(11) NOT NULL,
  `FK_drug_id` bigint(20) UNSIGNED NOT NULL,
  `FK_facture_id` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Déclencheurs `facture_row`
--
DELIMITER $$
CREATE TRIGGER `Stock_Drugs` AFTER INSERT ON `facture_row` FOR EACH ROW UPDATE
    drugs
SET
    drugs.stock = drugs.stock - NEW.item_count
WHERE
    drugs.PK_drug_id = NEW.FK_drug_id
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `PK_user_id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(20) COLLATE utf8_bin NOT NULL,
  `pseudonyme` varchar(20) COLLATE utf8_bin NOT NULL,
  `password` varchar(300) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`PK_user_id`, `name`, `pseudonyme`, `password`) VALUES
(7, 'Vanbelle', 'Admin', '537e2dd24f0a0c9aa8be8367ec563d1920578fb9d55b4ac49694649a5051052297e687c9307ff8824e39ce7a2203ecda74795d964c7e95f20b2ebdb3d7ce5bc6975761b6100b21abcfae5c19c07cd43d195bda2be28bbdabeb03f5111f7d8b3e');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `clients`
--
ALTER TABLE `clients`
  ADD UNIQUE KEY `PK_client_id` (`PK_client_id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `phone_number` (`phone_number`);

--
-- Index pour la table `concentration`
--
ALTER TABLE `concentration`
  ADD UNIQUE KEY `PK_concentration_id` (`PK_concentration_id`),
  ADD UNIQUE KEY `concentration_mg` (`concentration_mg`);

--
-- Index pour la table `drugs`
--
ALTER TABLE `drugs`
  ADD UNIQUE KEY `PK_drug_id` (`PK_drug_id`),
  ADD KEY `FK_concentration_id` (`FK_concentration_id`);

--
-- Index pour la table `facture`
--
ALTER TABLE `facture`
  ADD UNIQUE KEY `PK_facture_id` (`PK_facture_id`),
  ADD KEY `FK_client_id` (`FK_client_id`);

--
-- Index pour la table `facture_row`
--
ALTER TABLE `facture_row`
  ADD UNIQUE KEY `PK_fd_id` (`PK_fd_id`),
  ADD KEY `FK_drug_id` (`FK_drug_id`),
  ADD KEY `FK_facture_id` (`FK_facture_id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD UNIQUE KEY `PK_user_id` (`PK_user_id`),
  ADD UNIQUE KEY `pseudonyme` (`pseudonyme`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `clients`
--
ALTER TABLE `clients`
  MODIFY `PK_client_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT pour la table `concentration`
--
ALTER TABLE `concentration`
  MODIFY `PK_concentration_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT pour la table `drugs`
--
ALTER TABLE `drugs`
  MODIFY `PK_drug_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT pour la table `facture`
--
ALTER TABLE `facture`
  MODIFY `PK_facture_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT pour la table `facture_row`
--
ALTER TABLE `facture_row`
  MODIFY `PK_fd_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `PK_user_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `drugs`
--
ALTER TABLE `drugs`
  ADD CONSTRAINT `drugs_ibfk_1` FOREIGN KEY (`FK_concentration_id`) REFERENCES `concentration` (`PK_concentration_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `facture`
--
ALTER TABLE `facture`
  ADD CONSTRAINT `facture_ibfk_1` FOREIGN KEY (`FK_client_id`) REFERENCES `clients` (`PK_client_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `facture_row`
--
ALTER TABLE `facture_row`
  ADD CONSTRAINT `facture_row_ibfk_1` FOREIGN KEY (`FK_drug_id`) REFERENCES `drugs` (`PK_drug_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `facture_row_ibfk_2` FOREIGN KEY (`FK_facture_id`) REFERENCES `facture` (`PK_facture_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
