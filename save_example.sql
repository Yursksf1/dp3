create table paciente
(
    id               int
        constraint paciente_pk
            primary key,
    nombre           char(200),
    apellido         char(200),
    tipo_documento   char(2),
    numero_documento char(15)
);

create table doctor
(
    id           int
        constraint doctor_pk
            primary key,
    nombre       char(200),
    especialidad char(200)
);

create table consultorio
(
    id        int
        constraint consultorio_pk
            primary key,
    nombre    char(100),
    ubicacion char(200)
);

create table cita
(
    id             int
        constraint cita_pk
            primary key,
    fecha          date,
    especialidad   char(200),
    motivo         char(200),
    id_paciente    int
        references paciente,
    id_doctor      int
        references doctor,
    id_consultorio int
        references consultorio
);

