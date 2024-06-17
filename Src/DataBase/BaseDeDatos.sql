--
-- Archivo generado con SQLiteStudio v3.4.4 el lun. jun. 17 17:12:24 2024
--
-- Codificaci�n de texto usada: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabla: CLASES
CREATE TABLE IF NOT EXISTS CLASES (
    ID_Clase     INTEGER       PRIMARY KEY AUTOINCREMENT
                               NOT NULL,
    Nombre_Clase VARCHAR (100) NOT NULL,
    Profesor_ID  INTEGER       NOT NULL,
    Sede_Clase   VARCHAR (100) NOT NULL,
    Grupo_Clase  VARCHAR (100) NOT NULL,
    FOREIGN KEY (
        Profesor_ID
    )
    REFERENCES PROFESORES (ID_Profesor) 
);


-- Tabla: DATOS_BIOMETRICOS
CREATE TABLE IF NOT EXISTS DATOS_BIOMETRICOS (
    ID_Datos_Biometricos INTEGER  PRIMARY KEY AUTOINCREMENT
                                  NOT NULL,
    Datos_Biometricos    LONGBLOB NOT NULL,
    Clase_ID             INTEGER  NOT NULL,
    FOREIGN KEY (
        Clase_ID
    )
    REFERENCES CLASES (ID_Clase) 
);


-- Tabla: ESTUDIANTES
CREATE TABLE IF NOT EXISTS ESTUDIANTES (
    ID_Estudiante        INTEGER       PRIMARY KEY AUTOINCREMENT
                                       NOT NULL,
    Documento_Estudiante INTEGER       NOT NULL,
    Nombre_Estudiante    VARCHAR (100) NOT NULL,
    Carrera_Estudiante   VARCHAR (100) NOT NULL,
    Clase_ID             INTEGER       NOT NULL,
    FOREIGN KEY (
        Clase_ID
    )
    REFERENCES CLASES (ID_Clase) 
);


-- Tabla: PROFESORES
CREATE TABLE IF NOT EXISTS PROFESORES (
    ID_Profesor        INTEGER       PRIMARY KEY AUTOINCREMENT
                                     NOT NULL,
    Documento_Profesor INTEGER       NOT NULL,
    Contrasena         VARCHAR (50)  NOT NULL,
    Nombre_Profesor    VARCHAR (100) 
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
