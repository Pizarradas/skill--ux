"""Utilidades compartidas: lectura de fichas de ley (front matter YAML simple). Solo stdlib, Python 3.8+."""
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEYES = os.path.join(RAIZ, "01-leyes")

FAMILIAS = {
    "PER": ("per-percepcion-atencion", "Percepción y atención"),
    "MEM": ("mem-memoria-carga", "Memoria y carga cognitiva"),
    "DEC": ("dec-decision-juicio", "Decisión y juicio"),
    "ACC": ("acc-accion-interaccion", "Acción e interacción"),
    "MOT": ("mot-motivacion-tiempo", "Motivación y experiencia en el tiempo"),
    "SIS": ("sis-sistema-complejidad", "Modelos mentales y complejidad"),
}
EVIDENCIA = {
    "E1": "Ley cuantitativa",
    "E2": "Efecto robusto",
    "E3": "Evidencia mixta",
    "C": "Constructo teórico",
    "H": "Heurística de diseño",
}
SECCIONES = [
    "## Origen", "## Mecanismo", "## Evidencia y límites", "## Aplicación práctica",
    "## Anti-patrones", "## Ética y accesibilidad", "## Cómo auditarla",
    "## Relaciones", "## Fuentes",
]
ID_RE = re.compile(r"^(PER|MEM|DEC|ACC|MOT|SIS)-\d\d$")


def _valor(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        dentro = v[1:-1].strip()
        return [x.strip().strip("'\"") for x in dentro.split(",") if x.strip()] if dentro else []
    return v.strip("'\"")


def leer_ficha(ruta):
    with open(ruta, encoding="utf-8") as f:
        texto = f.read()
    meta = {}
    cuerpo = texto
    if texto.startswith("---"):
        fin = texto.find("\n---", 3)
        if fin != -1:
            for linea in texto[3:fin].splitlines():
                if ":" in linea and not linea.startswith(" "):
                    k, v = linea.split(":", 1)
                    meta[k.strip()] = _valor(v)
            cuerpo = texto[fin + 4:]
    m = re.search(r"^>\s*(.+?)$", cuerpo, re.M)
    meta["_enunciado"] = m.group(1).strip() if m else ""
    meta["_ruta"] = os.path.relpath(ruta, RAIZ).replace(os.sep, "/")
    meta["_cuerpo"] = cuerpo
    meta["_palabras"] = len(cuerpo.split())
    return meta


def todas_las_fichas():
    fichas = []
    for fam, (carpeta, _) in FAMILIAS.items():
        d = os.path.join(LEYES, carpeta)
        if not os.path.isdir(d):
            continue
        for nombre in sorted(os.listdir(d)):
            if nombre.endswith(".md") and not nombre.startswith("_"):
                fichas.append(leer_ficha(os.path.join(d, nombre)))
    fichas.sort(key=lambda m: m.get("id", ""))
    return fichas
