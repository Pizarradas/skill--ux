#!/usr/bin/env python3
"""Empaqueta el sistema en archivos únicos para plataformas que sólo aceptan un
documento o un prompt (ChatGPT/GPTs, Gemini Gems, Proyectos, Copilot, RAG simple…).

Genera en dist/:
  - ux-skill-nucleo.md     núcleo operativo (instrucciones, mapa, índice, router,
                           tensiones, ética, checklist rápida). ~ para prompt de sistema o
                           "instrucciones" + conocimiento mínimo.
  - ux-skill-completo.md   todo el sistema en orden de carga (para subir como conocimiento).
  - ux-skill-leyes.md      sólo las 30 fichas (para RAG por ley).
  - ux-skill-resumenes.md  enunciado + resumen operativo de las 30 leyes (capa intermedia).

Uso:  python herramientas/empaquetar.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import RAIZ, todas_las_fichas  # noqa: E402

NUCLEO = [
    "AGENTS.md",
    "00-indice/mapa-global.md",
    "00-indice/niveles-de-evidencia.md",
    "00-indice/indice-leyes.md",
    "03-aplicacion/por-sintoma.md",
    "02-relaciones/tensiones.md",
    "06-etica-accesibilidad/etica-y-patrones-oscuros.md",
    "05-checklists/checklist-rapida.md",
]
ORDEN_CARPETAS = ["00-indice", "01-leyes", "02-relaciones", "03-aplicacion", "04-procesos",
                  "05-checklists", "06-etica-accesibilidad", "07-plantillas", "08-fuentes"]


def leer(rel):
    with open(os.path.join(RAIZ, rel), encoding="utf-8") as fh:
        return fh.read()


def bloque(rel):
    return f"\n\n<!-- ===== ARCHIVO: {rel} ===== -->\n\n" + leer(rel).strip() + "\n"


def todos_en_orden():
    lista = ["README.md", "AGENTS.md"]
    for c in ORDEN_CARPETAS:
        for base, dirs, archivos in os.walk(os.path.join(RAIZ, c)):
            dirs.sort()
            for a in sorted(archivos):
                if a.endswith(".md"):
                    lista.append(os.path.relpath(os.path.join(base, a), RAIZ).replace(os.sep, "/"))
    return lista


CABECERA = ("# UX Skill — paquete {nombre}\n\n"
            "Paquete generado de la carpeta `ux-skill`. Cada sección indica su archivo de origen; "
            "las referencias a rutas (`01-leyes/...`) apuntan a secciones de este mismo documento. "
            "Síntesis original basada en *Laws of UX* (lawsofux.com, Jon Yablonski, CC BY-NC-ND 4.0) "
            "y en sus fuentes primarias.\n")

def resumenes():
    """Enunciado + resumen operativo de cada ficha: capa intermedia entre el prompt compacto y el sistema completo."""
    partes = []
    for f in todas_las_fichas():
        c = f["_cuerpo"]
        if "## Resumen operativo" not in c:
            continue
        r = c.split("## Resumen operativo", 1)[1].split("\n## ", 1)[0].strip()
        partes.append(f"\n## {f['id']} · {f['nombre']} (*{f['nombre_en']}*) — {f.get('evidencia')}\n\n"
                      f"> {f['_enunciado']}\n\n{r}\n\nFicha completa: `{f['_ruta']}`\n")
    return "".join(partes)


os.makedirs(os.path.join(RAIZ, "dist"), exist_ok=True)
texto_res = CABECERA.format(nombre="resúmenes operativos") + resumenes()
with open(os.path.join(RAIZ, "dist", "ux-skill-resumenes.md"), "w", encoding="utf-8", newline="\n") as fh:
    fh.write(texto_res)
print(f"dist/ux-skill-resumenes.md: {len(texto_res.split())} palabras (~{int(len(texto_res.split()) * 1.6)} tokens)")
salidas = {
    "ux-skill-nucleo.md": ("núcleo", [r for r in NUCLEO if os.path.exists(os.path.join(RAIZ, r))]),
    "ux-skill-completo.md": ("completo", todos_en_orden()),
    "ux-skill-leyes.md": ("leyes", [f["_ruta"] for f in todas_las_fichas()]),
}
for nombre, (etiqueta, rutas) in salidas.items():
    texto = CABECERA.format(nombre=etiqueta) + "".join(bloque(r) for r in rutas)
    with open(os.path.join(RAIZ, "dist", nombre), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)
    palabras = len(texto.split())
    print(f"dist/{nombre}: {len(rutas)} archivos, {palabras} palabras (~{int(palabras * 1.6)} tokens)")
