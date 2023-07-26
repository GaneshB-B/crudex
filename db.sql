CREATE TABLE `employees` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `f_name` text NOT NULL,
  `m_name` text,
  `l_name` text NOT NULL,
  `title` text NOT NULL,
  `age` int unsigned NOT NULL,
  `city` text NOT NULL,
  `salary` int unsigned DEFAULT NULL,
  `joining` date NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=6;