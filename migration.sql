BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> f9fb59327d61

CREATE TABLE bios (
    id SERIAL NOT NULL, 
    name TEXT, 
    note TEXT, 
    designation TEXT, 
    image_key TEXT, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    updated_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id)
);

CREATE TABLE profiles (
    id SERIAL NOT NULL, 
    organization_name VARCHAR NOT NULL, 
    designation VARCHAR NOT NULL, 
    joining_date TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
    last_working_date TIMESTAMP WITHOUT TIME ZONE, 
    notes TEXT, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    updated_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id)
);

CREATE TABLE registers (
    id SERIAL NOT NULL, 
    email VARCHAR NOT NULL, 
    password VARCHAR NOT NULL, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    updated_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id)
);

CREATE TABLE social_media (
    id SERIAL NOT NULL, 
    media_domain_name VARCHAR NOT NULL, 
    "profile_linK" VARCHAR NOT NULL, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    updated_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id)
);

INSERT INTO alembic_version (version_num) VALUES ('f9fb59327d61') RETURNING alembic_version.version_num;

COMMIT;

