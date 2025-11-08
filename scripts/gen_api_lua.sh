#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT_MD="$ROOT/docs/api/external/luafunctions_client.md"
TMP="$ROOT/.lua_api_hits.txt"

mkdir -p "$(dirname "$OUT_MD")"

echo "==> Skany źródeł pod rejestrację Lua…"
# dopisz/zmień wzorce pod swoje makra
rg -n --no-heading \
    -e 'registerLua(Function|Method)' \
    -e 'g_lua\.(bind|register)' \
    -e 'lua_register' \
    -e 'luaL_Reg' \
    src > "$TMP" || true

echo "==> Generowanie Markdown: $OUT_MD"
{
  echo "# Lua API — rejestrowane funkcje (heurystycznie)\n"
  echo "> Wykryto linie rejestracji funkcji/macierzy luaL_Reg itp. Uporządkujemy przy kolejnym kroku (jeśli chcesz, dorobię parser AST)."
  echo
  echo "```text"
  cat "$TMP"
  echo "```"
} > "$OUT_MD"

echo "Wygenerowano: $OUT_MD"
