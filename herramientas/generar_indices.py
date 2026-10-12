#!/usr/bin/env python3
"""Genera, a partir del front matter de las fichas de 01-leyes/:

  - 00-indice/indice-leyes.md       índice legible (por familia, evidencia y etiqueta)
  - 02-relaciones/matriz-relaciones.md  grafo de refuerzos y tensiones
  - datos/leyes.json                datos estructurados (RAG, herramientas, otros modelos)
  - datos/relaciones.json           aristas del grafo

Las fichas son la única fuente de verdad: edita la ficha y vuelve a ejecutar.
Uso:  python herramientas/generar_indices.py
"""
import json
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import RAIZ, FAMILIAS, EVIDENCIA, todas_las_fichas  # noqa: E402

fichas = todas_las_fichas()
por_id = {f["id"]: f for f in fichas}
AVISO = "<!-- Archivo generado por herramientas/generar_indices.py. No editar a mano. -->\n\n"


def escribir(rel, texto):
    ruta = os.path.join(RAIZ, rel)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)
    print("escrito", rel)


def enlace(f, desde):
    return os.path.relpath(os.path.join(RAIZ, f["_ruta"]), os.path.join(RAIZ, desde)).replace(os.sep, "/")


# ---------- datos/leyes.json ----------
leyes = []
for f in fichas:
    leyes.append({
        "id": f["id"], "nombre": f.get("nombre"), "nombre_en": f.get("nombre_en"),
        "alias": f.get("alias") or [], "familia": f.get("familia"),
        "familia_nombre": FAMILIAS[f["familia"]][1],
        "evidencia": f.get("evidencia"), "evidencia_nombre": EVIDENCIA.get(f.get("evidencia"), ""),
        "etiquetas": f.get("etiquetas") or [], "refuerza": f.get("refuerza") or [],
        "tensiona": f.get("tensiona") or [], "tensiones": f.get("tensiones") or [],
        "enunciado": f["_enunciado"], "archivo": f["_ruta"],
        "fuente_laws_of_ux": f.get("fuente_laws_of_ux"),
    })
escribir("datos/leyes.json", json.dumps({
    "version": "1.0",
    "descripcion": "Leyes de UX (síntesis original basada en lawsofux.com de Jon Yablonski y sus fuentes)",
    "familias": {k: v[1] for k, v in FAMILIAS.items()},
    "niveles_evidencia": EVIDENCIA,
    "leyes": leyes,
}, ensure_ascii=False, indent=2) + "\n")

# ---------- relaciones ----------
aristas = []
for f in fichas:
    for d in f.get("refuerza") or []:
        aristas.append({"de": f["id"], "a": d, "tipo": "refuerza"})
    for d in f.get("tensiona") or []:
        aristas.append({"de": f["id"], "a": d, "tipo": "tensiona"})
escribir("datos/relaciones.json", json.dumps({"aristas": aristas}, ensure_ascii=False, indent=2) + "\n")

# ---------- índice ----------
DEST = "00-indice"
L = [AVISO, "# Índice de leyes\n\n",
     "30 leyes en 6 familias. Id estable · nombre · nivel de evidencia "
     "(`00-indice/niveles-de-evidencia.md`) · enunciado.\n\n"]
for fam, (_, nombre_fam) in FAMILIAS.items():
    L.append(f"## {fam} · {nombre_fam}\n\n| Id | Ley | Evidencia | Enunciado |\n|---|---|---|---|\n")
    for f in fichas:
        if f["familia"] == fam:
            L.append(f"| {f['id']} | [{f['nombre']}]({enlace(f, DEST)}) (*{f['nombre_en']}*) | "
                     f"{f['evidencia']} | {f['_enunciado'].replace('|', '/')} |\n")
    L.append("\n")
L.append("## Por nivel de evidencia\n\n")
for ev, nom in EVIDENCIA.items():
    ids = [f["id"] + " " + f["nombre"] for f in fichas if f.get("evidencia") == ev]
    L.append(f"- **{ev} · {nom}:** {', '.join(ids) if ids else '—'}\n")
L.append("\n## Por etiqueta\n\n")
etq = defaultdict(list)
for f in fichas:
    for e in f.get("etiquetas") or []:
        etq[e].append(f["id"])
for e in sorted(etq):
    L.append(f"- **{e}:** {', '.join(etq[e])}\n")
L.append("\n## Nombres alternativos\n\n")
for f in fichas:
    nombres = [f["nombre_en"]] + list(f.get("alias") or [])
    L.append(f"- {f['id']} {f['nombre']}: {'; '.join(nombres)}\n")
escribir("00-indice/indice-leyes.md", "".join(L))

# ---------- matriz ----------
M = [AVISO, "# Matriz de relaciones\n\n",
     "Generada del front matter de cada ficha (`refuerza`, `tensiona`). El porqué de cada relación "
     "está en la sección *Relaciones* de la ficha; las resoluciones de las tensiones, en "
     "`02-relaciones/tensiones.md`.\n\n## Lista de adyacencia\n\n"
     "| Ley | Refuerza / se apoya en | Tensiona con | Tensiones |\n|---|---|---|---|\n"]
for f in fichas:
    M.append(f"| {f['id']} {f['nombre']} | {', '.join(f.get('refuerza') or []) or '—'} | "
             f"{', '.join(f.get('tensiona') or []) or '—'} | {', '.join(f.get('tensiones') or []) or '—'} |\n")
grado = defaultdict(int)
for a in aristas:
    grado[a["de"]] += 1
    grado[a["a"]] += 1
M.append("\n## Leyes más conectadas (centrales en el mapa)\n\n")
for i, g in sorted(grado.items(), key=lambda x: -x[1])[:10]:
    M.append(f"- {i} {por_id[i]['nombre']}: {g} relaciones\n")
M.append("\n## Grafo de refuerzos\n\n```mermaid\nflowchart LR\n")
for fam, (_, nombre_fam) in FAMILIAS.items():
    M.append(f"  subgraph {fam}[\"{nombre_fam}\"]\n")
    for f in fichas:
        if f["familia"] == fam:
            M.append(f"    {f['id'].replace('-', '')}[\"{f['id']} {f['nombre']}\"]\n")
    M.append("  end\n")
hechas = set()
for a in aristas:
    par = tuple(sorted((a["de"], a["a"]))) + (a["tipo"],)
    if par in hechas:
        continue
    hechas.add(par)
    flecha = "---" if a["tipo"] == "refuerza" else "-.-x"
    M.append(f"  {a['de'].replace('-', '')} {flecha} {a['a'].replace('-', '')}\n")
M.append("```\n\nLínea continua = refuerzo · línea discontinua con x = tensión.\n")
escribir("02-relaciones/matriz-relaciones.md", "".join(M))

# ---------- tabla de leyes del prompt compacto ----------
ruta_prompt = os.path.join(RAIZ, "adaptadores", "prompt-sistema-compacto.md")
if os.path.exists(ruta_prompt):
    with open(ruta_prompt, encoding="utf-8") as fh:
        p = fh.read()
    ini, fin = "<!-- LEYES:INICIO -->", "<!-- LEYES:FIN -->"
    if ini in p and fin in p:
        filas = []
        for fam, (_, nombre_fam) in FAMILIAS.items():
            filas.append(f"\n**{fam} · {nombre_fam}**\n")
            for f in fichas:
                if f["familia"] == fam:
                    filas.append(f"- {f['id']} {f['nombre']} ({f['nombre_en']}) · {f['evidencia']} · {f['_enunciado']}")
        nuevo = p[:p.index(ini) + len(ini)] + "\n" + "\n".join(filas) + "\n" + p[p.index(fin):]
        with open(ruta_prompt, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(nuevo)
        print("actualizado adaptadores/prompt-sistema-compacto.md")

# ---------- bibliografía (fuentes primarias de todas las fichas) ----------
import re as _re
biblio = {}
for f in fichas:
    cuerpo = f["_cuerpo"]
    if "## Fuentes" not in cuerpo:
        continue
    seccion = cuerpo.split("## Fuentes", 1)[1]
    en_primarias = False
    for linea in seccion.splitlines():
        s = linea.strip()
        if _re.match(r"^- \**Primarias", s):
            en_primarias = True
            continue
        if _re.match(r"^- \S", linea):
            en_primarias = False
            continue
        if en_primarias and s.startswith("- "):
            ref = s[2:].strip()
            clave = _re.sub(r"[^a-z0-9]", "", ref.lower())[:45]
            ent = biblio.setdefault(clave, {"ref": ref, "leyes": []})
            if len(ref) > len(ent["ref"]):
                ent["ref"] = ref
            if f["id"] not in ent["leyes"]:
                ent["leyes"].append(f["id"])
B = [AVISO, "# Bibliografía primaria\n\n",
     "Fuentes primarias citadas en las fichas (extraídas automáticamente de sus secciones "
     "*Fuentes → Primarias*), en orden alfabético, con las leyes que las citan. El estado de "
     "verificación de cada referencia se indica en la ficha correspondiente. Fuentes enlazadas "
     "por Laws of UX: `08-fuentes/fuentes-por-ley.md`.\n\n"]
for clave in sorted(biblio, key=lambda k: biblio[k]["ref"].lower().lstrip("*_")):
    e = biblio[clave]
    B.append(f"- {e['ref']} — *{', '.join(e['leyes'])}*\n")
B.append(f"\n{len(biblio)} referencias.\n")
escribir("08-fuentes/bibliografia.md", "".join(B))
