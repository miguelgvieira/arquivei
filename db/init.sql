-- Migração para o banco de dados.
-- É lida e executada automaticamente na primeira vez que o docker subir o banco de dados.

CREATE DATABASE nfes;
use nfes;

CREATE TABLE nfe_value (
    access_key VARCHAR(50),
    total_value DOUBLE
);
