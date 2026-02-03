# src/garbagecls/db.py
import os
from contextlib import contextmanager

import pandas as pd
import psycopg2
from dotenv import load_dotenv


def load_env():
    """
    Carica le variabili da .env (se presente) + env di sistema.
    Chiamala una volta nei notebook prima di usare get_conn().
    """
    load_dotenv()


@contextmanager
def get_conn():
    """
    Context manager per ottenere una connessione PostgreSQL e chiuderla automaticamente.
    Usa variabili d'ambiente:
      DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
    """
    host = os.getenv("DB_HOST", "127.0.0.1")
    port = os.getenv("DB_PORT", "5432")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    missing = [k for k, v in {
        "DB_NAME": dbname,
        "DB_USER": user,
        "DB_PASSWORD": password,
    }.items() if not v]

    if missing:
        raise RuntimeError(
            f"Missing environment variables: {missing}. "
            "Check your .env file or environment configuration."
        )

    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    try:
        yield conn
    finally:
        conn.close()


def read_images_df(source: str | None = None) -> pd.DataFrame:
    """
    Legge i metadati immagini dalla tabella `images` e restituisce un DataFrame.

    restituirà:
    pd.DataFrame con colonne:
      image_id, filepath, label, split, width, height, channels, source
    """
    base_query = """
    SELECT image_id, filepath, label, split, width, height, channels, source
    FROM images
    """

    params = []
    if source is not None:
        base_query += " WHERE source = %s"
        params.append(source)

    base_query += " ORDER BY image_id;"

    with get_conn() as conn:
        df = pd.read_sql_query(base_query, conn, params=params if params else None)

    return df


def split_dfs(df: pd.DataFrame):
    """
    Split standard train/val/test dal DataFrame.
    """
    df_train = df[df["split"] == "train"].reset_index(drop=True)
    df_val   = df[df["split"] == "val"].reset_index(drop=True)
    df_test  = df[df["split"] == "test"].reset_index(drop=True)
    # quando avremo df_test_our, aggiungere qui la logica per gestirlo
    return df_train, df_val, df_test
