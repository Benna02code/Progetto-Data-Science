-- db/schema.sql

CREATE TABLE IF NOT EXISTS images (
    image_id        BIGSERIAL PRIMARY KEY,
    filepath        TEXT NOT NULL UNIQUE,   -- es: data/raw/raw_flat/cardboard/cardboard1.jpg

    label           TEXT NOT NULL,          -- cardboard, glass, ...
    split           TEXT NOT NULL CHECK (split IN ('train','val','test')),
    source          TEXT NOT NULL DEFAULT 'raw_flat' CHECK (source IN ('raw_flat','external','processed')),

    width           INTEGER, -- opzionali (li possiamo riempire dopo)
    height          INTEGER,
    channels        INTEGER,
    file_hash       TEXT,

    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);


SELECT COUNT(*) FROM images;
