DROP DATABASE IF EXISTS ValorantDB;

CREATE DATABASE ValorantDB CHARSET utf8mb4;
USE ValorantDB;

CREATE TABLE AppUser(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(255) NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    edad INTEGER NOT NULL,
    sexo VARCHAR(1) NOT NULL
);

CREATE TABLE Matches(
    codigo INTEGER AUTO_INCREMENT PRIMARY KEY,
    idUsuario INTEGER NOT NULL,
    agente VARCHAR(20) NOT NULL,
    muertes INTEGER NOT NULL,
    asesinatos INTEGER NOT NULL,
    FOREIGN KEY (idUsuario) REFERENCES AppUser(id) ON DELETE CASCADE
);

CREATE TABLE PlayerAccount(
    idUsuario INTEGER PRIMARY KEY,
    rango VARCHAR(15) NOT NULL,
    nivel INTEGER NOT NULL,
    totalMuertes INTEGER NOT NULL,
    totalPartidos INTEGER NOT NULL,
    totalAsesinatos INTEGER NOT NULL,
    FOREIGN KEY (idUsuario) REFERENCES AppUser(id) ON DELETE CASCADE
);


DROP TRIGGER IF EXISTS trg_Matches_Insert;

DELIMITER //

CREATE TRIGGER trg_Matches_Insert AFTER INSERT ON Matches
FOR EACH ROW
BEGIN
    UPDATE PlayerAccount
    SET totalMuertes = totalMuertes + NEW.muertes,
        totalPartidos = totalPartidos + 1,
        totalAsesinatos = totalAsesinatos + NEW.asesinatos
    WHERE idUsuario = NEW.idUsuario;
END //

DELIMITER ;
