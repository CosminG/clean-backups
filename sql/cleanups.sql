--
-- Table structure for table `cleanups`
--

CREATE TABLE IF NOT EXISTS `cleanups` (
  `date` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `ip` varchar(16) COLLATE utf8_unicode_ci NOT NULL,
  `free_space` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `c_min_free_gb` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `how_many_dirs` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `c_how_many_keep` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `del_dirs` varchar(255) COLLATE utf8_unicode_ci NOT NULL  
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

