-- db/schema.sql
-- Schema per classificazione rifiuti: metadati immagini (niente immagini nel DB)

CREATE TABLE IF NOT EXISTS images (
  image_id   BIGSERIAL PRIMARY KEY,
  filepath   TEXT NOT NULL,
  label      TEXT NOT NULL,
  split      TEXT NOT NULL CHECK (split IN ('train','val','test','external')),
  source     TEXT NOT NULL CHECK (source IN ('raw','processed','external')),
  file_hash  TEXT,                       -- utile per dedup e controlli
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  CONSTRAINT uq_images_filepath UNIQUE (filepath)
);

-- Indici utili per query frequenti
CREATE INDEX IF NOT EXISTS idx_images_split  ON images(split);
CREATE INDEX IF NOT EXISTS idx_images_label  ON images(label);
CREATE INDEX IF NOT EXISTS idx_images_source ON images(source);
CREATE INDEX IF NOT EXISTS idx_images_hash   ON images(file_hash);

SELECT COUNT(*) FROM images;
