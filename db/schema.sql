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


SELECT * FROM images;

SELECT width, height, channels, COUNT(*) AS n
FROM images
GROUP BY width, height, channels
ORDER BY n DESC;

SELECT COUNT(*) AS missing_whc
FROM images
WHERE width IS NULL OR height IS NULL OR channels IS NULL;


-- Check distribution of splits per label
SELECT split, label, COUNT(*) AS n
FROM images
GROUP BY split, label
ORDER BY split, label;

-- check splits distribution
SELECT split, COUNT(*) AS n
FROM images
GROUP BY split
ORDER BY split;

SELECT source, label, COUNT(*) AS n
FROM images
WHERE source = 'external'
GROUP BY source, label
ORDER BY label;

SELECT split, label, COUNT(*) AS n
FROM images
WHERE source = 'raw_flat'
  AND split IN ('train','val','test')
GROUP BY split, label
ORDER BY split, label;



