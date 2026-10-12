#!/usr/bin/env python3
"""Valida la coherencia del sistema: fichas completas, ids únicos, relaciones válidas,
datos JSON sincronizados y enlaces internos existentes.

Uso:  python herramientas/validar.py
Sale con código 1 si hay errores.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import RAIZ, FAMILIAS, EVIDENCIA, SECCIONES, ID_RE, todas_las_fichas  # noqa: E402

errores, avisos = [], []
fichas = todas_las_fichas()
ids = {f.get("id") for f in fichas}

if len(fichas) != 30:
    errores.append(f"Se esperaban 30 fichas y hay {len(fichas)}")

vistos = set()
for f in fichas:
    i, r = f.get("id", "?"), f["_ruta"]
    if not ID_RE.match(i):
        errores.append(f"{r}: id inválido '{i}'")
    if i in vistos:
        errores.append(f"{r}: id duplicado {i}")
    vistos.add(i)
    fam = i[:3]
    if f.get("familia") != fam:
        errores.append(f"{r}: familia '{f.get('familia')}' no coincide con id {i}")
    if FAMILIAS.get(fam, ("",))[0] not in r:
        errores.append(f"{r}: carpeta incorrecta para {fam}")
    if f.get("evidencia") not in EVIDENCIA:
        errores.append(f"{r}: nivel de evidencia inválido '{f.get('evidencia')}'")
    for k in ("nombre", "nombre_en", "fuente_laws_of_ux"):
        if not f.get(k):
            errores.append(f"{r}: falta '{k}' en el front matter")
    for k in ("refuerza", "tensiona"):
        for ref in f.get(k) or []:
            if ref not in ids:
                errores.append(f"{r}: '{k}' apunta a id inexistente {ref}")
    for s in SECCIONES:
        if s not in f["_cuerpo"]:
            errores.append(f"{r}: falta la sección '{s}'")
    if not f["_enunciado"]:
        errores.append(f"{r}: falta el enunciado (línea '> ...')")
    if f["_palabras"] < 700:
        avisos.append(f"{r}: ficha corta ({f['_palabras']} palabras)")

# Datos JSON sincronizados
ruta_json = os.path.join(RAIZ, "datos", "leyes.json")
if os.path.exists(ruta_json):
    with open(ruta_json, encoding="utf-8") as fh:
        datos = json.load(fh)
    ids_json = {d["id"] for d in datos.get("leyes", [])}
    if ids_json != ids:
        errores.append("datos/leyes.json no está sincronizado: ejecuta herramientas/generar_indices.py")
else:
    errores.append("Falta datos/leyes.json: ejecuta herramientas/generar_indices.py")

# Enlaces internos `ruta/archivo.md` citados en el texto
patron = re.compile(r"`((?:0\d-[\w-]+|datos|adaptadores|herramientas)/[\w./-]+?\.(?:md|json|py))`")
for base, _, archivos in os.walk(RAIZ):
    if os.sep + "dist" in base or os.sep + "." in base:
        continue
    for a in archivos:
        if not a.endswith(".md"):
            continue
        p = os.path.join(base, a)
        with open(p, encoding="utf-8") as fh:
            texto = fh.read()
        for ref in patron.findall(texto):
            if "<" in ref or "{" in ref:
                continue
            if not os.path.exists(os.path.join(RAIZ, ref)):
                errores.append(f"{os.path.relpath(p, RAIZ)}: enlace roto `{ref}`")

# Ids citados en el texto que no existen
cita = re.compile(r"\b(PER|MEM|DEC|ACC|MOT|SIS)-(\d\d)\b")
for base, _, archivos in os.walk(RAIZ):
    if os.sep + "dist" in base:
        continue
    for a in archivos:
        if a.endswith(".md"):
            p = os.path.join(base, a)
            with open(p, encoding="utf-8") as fh:
                for fam, n in set(cita.findall(fh.read())):
                    if f"{fam}-{n}" not in ids and n != "NN":
                        errores.append(f"{os.path.relpath(p, RAIZ)}: cita id inexistente {fam}-{n}")

for a in avisos:
    print("AVISO ", a)
for e in errores:
    print("ERROR ", e)
print(f"\n{len(fichas)} fichas · {len(errores)} errores · {len(avisos)} avisos")
sys.exit(1 if errores else 0)
