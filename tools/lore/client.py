"""
LORE API base client.
Reads LORE_API_KEY from environment (.env file or shell).
All other LORE scripts import this module.
"""

import os
import time
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load .env from repo root (two levels up from this file)
_repo_root = Path(__file__).resolve().parents[2]
load_dotenv(_repo_root / ".env")

BASE_URL = "https://api.loremoney.com"  # adjusted by discover.py if different

_MAX_RETRIES = 4
_RETRY_DELAYS = [2, 4, 8, 16]


def _get_key() -> str:
    key = os.getenv("LORE_API_KEY", "").strip()
    if not key or key == "your_key_here":
        raise EnvironmentError(
            "LORE_API_KEY not set.\n"
            "Copy .env.example to .env and add your key, or export LORE_API_KEY=<key>."
        )
    return key


def get(endpoint: str, params: dict | None = None, base_url: str = BASE_URL) -> dict:
    """
    GET request with retry on 429 (rate limit) and basic error surfacing.
    Returns parsed JSON dict.
    """
    url = base_url.rstrip("/") + "/" + endpoint.lstrip("/")
    headers = {
        "Authorization": f"Bearer {_get_key()}",
        "Accept": "application/json",
    }

    for attempt, delay in enumerate([0] + _RETRY_DELAYS):
        if delay:
            print(f"  Rate limited — retrying in {delay}s...")
            time.sleep(delay)

        try:
            resp = requests.get(url, headers=headers, params=params, timeout=30)
        except requests.RequestException as exc:
            if attempt < _MAX_RETRIES:
                print(f"  Network error ({exc}) — retrying...")
                continue
            raise

        if resp.status_code == 429:
            if attempt < _MAX_RETRIES:
                continue
            resp.raise_for_status()

        if resp.status_code == 401:
            raise PermissionError(
                "API key rejected (401). Check LORE_API_KEY is correct and active."
            )

        if resp.status_code == 403:
            raise PermissionError(
                f"Access denied (403) for {endpoint}. "
                "This endpoint may require a higher subscription tier."
            )

        resp.raise_for_status()
        return resp.json()

    raise RuntimeError(f"Failed after {_MAX_RETRIES} retries: {endpoint}")


def post(endpoint: str, body: dict, base_url: str = BASE_URL) -> dict:
    """POST request with the same retry logic."""
    url = base_url.rstrip("/") + "/" + endpoint.lstrip("/")
    headers = {
        "Authorization": f"Bearer {_get_key()}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    for attempt, delay in enumerate([0] + _RETRY_DELAYS):
        if delay:
            print(f"  Rate limited — retrying in {delay}s...")
            time.sleep(delay)

        try:
            resp = requests.post(url, headers=headers, json=body, timeout=30)
        except requests.RequestException as exc:
            if attempt < _MAX_RETRIES:
                continue
            raise

        if resp.status_code == 429:
            if attempt < _MAX_RETRIES:
                continue
            resp.raise_for_status()

        if resp.status_code in (401, 403):
            raise PermissionError(f"Access denied ({resp.status_code}) for {endpoint}.")

        resp.raise_for_status()
        return resp.json()

    raise RuntimeError(f"Failed after {_MAX_RETRIES} retries: {endpoint}")
