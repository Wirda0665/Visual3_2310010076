-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 22 Okt 2025 pada 10.43
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `visual3_2310010076`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `idAdmin` int(11) NOT NULL,
  `NamaAdmin` varchar(50) NOT NULL,
  `Jk` varchar(10) NOT NULL,
  `Username` varchar(8) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Status` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `mustahik`
--

CREATE TABLE `mustahik` (
  `kdMustahik` varchar(12) NOT NULL,
  `NamaMustahik` varchar(50) NOT NULL,
  `NIK` varchar(12) NOT NULL,
  `Tempat` varchar(25) NOT NULL,
  `tglLahir` varchar(12) NOT NULL,
  `Alamat` text NOT NULL,
  `Jk` varchar(10) NOT NULL,
  `golongan` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `muzaki`
--

CREATE TABLE `muzaki` (
  `kdMuzaki` varchar(12) NOT NULL,
  `namaMuzaki` varchar(50) NOT NULL,
  `tempat` varchar(25) NOT NULL,
  `tglLahir` varchar(15) NOT NULL,
  `alamat` text NOT NULL,
  `Jk` varchar(10) NOT NULL,
  `NIK` varchar(12) NOT NULL,
  `Pekerjaan` varchar(50) NOT NULL,
  `StatusPerkawinan` varchar(7) NOT NULL,
  `Penghasilan` double NOT NULL,
  `Notel` varchar(12) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Username` varchar(8) NOT NULL,
  `Password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `zakat`
--

CREATE TABLE `zakat` (
  `kdZakat` varchar(8) NOT NULL,
  `NamaZakat` varchar(25) NOT NULL,
  `bentuk` varchar(5) NOT NULL,
  `saldo` double NOT NULL,
  `ket` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `zakatkeluar`
--

CREATE TABLE `zakatkeluar` (
  `NoTransKeluar` varchar(15) NOT NULL,
  `kdZakat` varchar(8) DEFAULT NULL,
  `kdMustahik` varchar(12) DEFAULT NULL,
  `JumlahKeluar` double DEFAULT NULL,
  `bentuk` varchar(5) DEFAULT NULL,
  `tglMasuk` date DEFAULT NULL,
  `idAdmin` int(11) DEFAULT NULL,
  `ket` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `zakatmasuk`
--

CREATE TABLE `zakatmasuk` (
  `NoTransMasuk` varchar(15) NOT NULL,
  `kdZakat` varchar(8) DEFAULT NULL,
  `kdMuzaki` varchar(12) DEFAULT NULL,
  `JumlahMasuk` double DEFAULT NULL,
  `bentuk` varchar(5) DEFAULT NULL,
  `tglMasuk` date DEFAULT NULL,
  `norek` varchar(15) DEFAULT NULL,
  `bukti` varchar(30) DEFAULT NULL,
  `ket` text DEFAULT NULL,
  `status` varchar(1) DEFAULT NULL,
  `idAdmin` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`idAdmin`);

--
-- Indeks untuk tabel `mustahik`
--
ALTER TABLE `mustahik`
  ADD PRIMARY KEY (`kdMustahik`);

--
-- Indeks untuk tabel `muzaki`
--
ALTER TABLE `muzaki`
  ADD PRIMARY KEY (`kdMuzaki`);

--
-- Indeks untuk tabel `zakat`
--
ALTER TABLE `zakat`
  ADD PRIMARY KEY (`kdZakat`);

--
-- Indeks untuk tabel `zakatkeluar`
--
ALTER TABLE `zakatkeluar`
  ADD PRIMARY KEY (`NoTransKeluar`),
  ADD KEY `kdZakat` (`kdZakat`),
  ADD KEY `kdMustahik` (`kdMustahik`),
  ADD KEY `idAdmin` (`idAdmin`);

--
-- Indeks untuk tabel `zakatmasuk`
--
ALTER TABLE `zakatmasuk`
  ADD PRIMARY KEY (`NoTransMasuk`),
  ADD KEY `kdZakat` (`kdZakat`),
  ADD KEY `kdMuzaki` (`kdMuzaki`),
  ADD KEY `idAdmin` (`idAdmin`);

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `zakatkeluar`
--
ALTER TABLE `zakatkeluar`
  ADD CONSTRAINT `zakatkeluar_ibfk_1` FOREIGN KEY (`kdZakat`) REFERENCES `zakat` (`kdZakat`),
  ADD CONSTRAINT `zakatkeluar_ibfk_2` FOREIGN KEY (`kdMustahik`) REFERENCES `mustahik` (`kdMustahik`),
  ADD CONSTRAINT `zakatkeluar_ibfk_3` FOREIGN KEY (`idAdmin`) REFERENCES `admin` (`idAdmin`);

--
-- Ketidakleluasaan untuk tabel `zakatmasuk`
--
ALTER TABLE `zakatmasuk`
  ADD CONSTRAINT `zakatmasuk_ibfk_1` FOREIGN KEY (`kdZakat`) REFERENCES `zakat` (`kdZakat`),
  ADD CONSTRAINT `zakatmasuk_ibfk_2` FOREIGN KEY (`kdMuzaki`) REFERENCES `muzaki` (`kdMuzaki`),
  ADD CONSTRAINT `zakatmasuk_ibfk_3` FOREIGN KEY (`idAdmin`) REFERENCES `admin` (`idAdmin`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
