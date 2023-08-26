-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-08-2023 a las 04:55:43
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_prueba`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `id` int(11) NOT NULL,
  `Nombre_completo` varchar(200) NOT NULL,
  `Correo_electronico` varchar(200) NOT NULL,
  `Numero_Telefono` varchar(200) NOT NULL,
  `Trabajo_cargo` varchar(200) NOT NULL,
  `Genero` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id`, `Nombre_completo`, `Correo_electronico`, `Numero_Telefono`, `Trabajo_cargo`, `Genero`) VALUES
(1, 'Fernando Antonio Oliveros Ocampo', 'foliveros@gmail.com', '123123124', 'Ingeniero', 'Hombre'),
(2, 'Maria Concepción Ocampo Dominguez', 'mayo@gmail.com', '3016010685', 'Arquitecto', 'Mujer'),
(4, 'Fernando Olivero Machacon', 'fernando@gmail.com', '3423534534', 'Secretario', 'Hombre'),
(5, 'Maria Fernanda Oliveros Ocampo', 'Mafe@gmail.com', '3242342344', 'Abogado', 'Mujer'),
(7, 'lucellys johanna olivero dominguez', 'luamordefer@gmail.com', '30016455454', 'Auxiliar', 'Mujer'),
(8, 'Anronio', 'anto@gmail.com', '324234235235', 'Auxiliar', 'Hombre'),
(9, 'Jean trujillo', 'jean@gmail.com', '35345345', 'Ingeniero', 'Hombre');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

CREATE TABLE `genero` (
  `id` int(11) NOT NULL,
  `genero` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `genero`
--

INSERT INTO `genero` (`id`, `genero`) VALUES
(1, 'Hombre'),
(2, 'Mujer'),
(3, 'Otro');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `Nombre_producto` varchar(20) NOT NULL,
  `Descripcion` varchar(20) NOT NULL,
  `Precio_producto` varchar(20) NOT NULL,
  `Marca_producto` varchar(20) NOT NULL,
  `Fecha_producto` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `Nombre_producto`, `Descripcion`, `Precio_producto`, `Marca_producto`, `Fecha_producto`) VALUES
(1, 'el pep', 'el pepeeeee', '1234', '12312', '2023-08-22'),
(2, 'tert', 'erte', '0', 'ertert', '2023-08-22'),
(3, 'ewfefsds', 'dfgs', '0', 'gss', '2023-08-23'),
(4, 'fasf', 'safasf', '0', 'ddsd', '2023-08-22'),
(5, 'qewqr', 'qwrqw', '0', '234234', '2023-08-22'),
(6, 'fsdf', 'sdff', '0', '123', '2023-08-22'),
(7, 'fsfds', 'fsafsfgegrg4rgdeggrg', '23424234', 'fsdfsdfsdfsdf', '2023-08-22'),
(8, '234', 'sfdfsf', '12', 'effd', '2023-08-22'),
(9, '113wqdqd', 'sdasd', '12', 'adsaa', '2023-08-22'),
(10, 'qweqwe', 'qweq', '12.000', 'weqwe', '2023-08-22'),
(11, 'acetaminofen', 'para la fiebre', '1200', 'bodega principal', '2023-08-21'),
(12, '2rwer', 'rwer', 'wrw', 'wrew', '2023-08-25'),
(13, 'wef', 'wefw', 'wef', 'fwf', '2023-08-25'),
(14, 'wer', 'wer', 'wer', 'werwer', '2023-08-25'),
(15, 'wer', 'wer', 'wer', 'werwer', '2023-08-25'),
(16, 'rwe', 'wrw', 'ewrwr', 'wewe', '2023-08-25'),
(17, 'wrw', 'wrw', 'wer', 'wr', '2023-08-25'),
(18, 'wer', 'we', 'wer', 'wer', '2023-08-25'),
(19, 'wer', 'wer', 'wer', 'wer', '2023-08-25'),
(20, 'wer', 'wr', 'wer', 'wer', '2023-08-25'),
(21, 'paracetamol', 'para todo tipo de do', '1233', '123', '2023-08-25');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajo`
--

CREATE TABLE `trabajo` (
  `id` int(11) NOT NULL,
  `trabajo` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `trabajo`
--

INSERT INTO `trabajo` (`id`, `trabajo`) VALUES
(1, 'Abogado'),
(2, 'Arquitecto'),
(6, 'Auxiliar'),
(3, 'Ingeniero'),
(4, 'Medico'),
(5, 'Secretario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `usuario` varchar(200) NOT NULL,
  `contraseña` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `usuario`, `contraseña`) VALUES
(15, 'Fernando Oliveros', 'fernando', '123456'),
(16, 'Lucellys Olivero', 'Luce', '123456'),
(17, 'lucellys', 'feramor', '1803');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Trabajo_cargo` (`Trabajo_cargo`),
  ADD KEY `Genero` (`Genero`);

--
-- Indices de la tabla `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`id`),
  ADD KEY `genero` (`genero`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `trabajo`
--
ALTER TABLE `trabajo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `trabajo` (`trabajo`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `genero`
--
ALTER TABLE `genero`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `trabajo`
--
ALTER TABLE `trabajo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`Genero`) REFERENCES `genero` (`genero`),
  ADD CONSTRAINT `prueba` FOREIGN KEY (`Trabajo_cargo`) REFERENCES `trabajo` (`trabajo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
