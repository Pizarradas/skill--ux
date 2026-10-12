# UX Skill · Sistema de conocimiento y habilidades de UX para modelos de IA

Sistema **agnóstico** (sirve para Claude, GPT, Gemini, Llama, Mistral, Copilot, Cursor o
cualquier modelo que lea Markdown) que convierte las **30 leyes de UX** de
[Laws of UX](https://lawsofux.com/) (Jon Yablonski) y sus **fuentes primarias** en:

- un **mapa global** que explica qué describe cada ley, en qué momento de la interacción
  actúa, cómo se relaciona con las demás y dónde chocan;
- **fichas rigurosas** por ley: origen verificado, mecanismo, solidez de la evidencia,
  límites y malentendidos, reglas aplicables, anti-patrones, ética, accesibilidad y cómo auditarla;
- **habilidades operativas** (auditar, diseñar, criticar, justificar, diagnosticar,
  validar, enseñar, revisar código de UI) con procesos paso a paso y plantillas;
- **guías por contexto** (formularios, navegación, onboarding, e-commerce, dashboards,
  búsqueda, rendimiento, contenido, móvil, IA conversacional, sistemas de diseño, errores);
- **datos estructurados** (`datos/*.json`) y **herramientas** para validar y empaquetar.

---

## Estructura

```
ux-skill/
├── README.md                 ← este archivo (para personas)
├── AGENTS.md                 ← punto de entrada para CUALQUIER modelo (instrucciones operativas)
├── SKILL.md                  ← envoltorio para entornos con "skills" (p. ej. Claude); remite a AGENTS.md
├── 00-indice/                ← mapa global, índice de leyes, niveles de evidencia
├── 01-leyes/                 ← 30 fichas en 6 familias
│   ├── per-percepcion-atencion/   PER-01…07  Gestalt, atención selectiva, Von Restorff (+ anexo Gestalt)
│   ├── mem-memoria-carga/         MEM-01…05  carga cognitiva, memoria de trabajo, Miller, chunking, posición serial
│   ├── dec-decision-juicio/       DEC-01…04  Hick, sobrecarga de opciones, sesgos, estética-usabilidad
│   ├── acc-accion-interaccion/    ACC-01…04  Fitts, Doherty, Postel, usuario activo
│   ├── mot-motivacion-tiempo/     MOT-01…05  flow, gradiente de meta, Zeigarnik, Parkinson, pico-final
│   └── sis-sistema-complejidad/   SIS-01…05  Jakob, modelo mental, Tesler, Occam, Pareto
├── 02-relaciones/            ← matriz de relaciones (generada) y tensiones con reglas de resolución
├── 03-aplicacion/            ← router síntoma→leyes y guías por contexto
├── 04-procesos/              ← las 8 habilidades (H1–H8) paso a paso
├── 05-checklists/            ← checklist de auditoría completa y rápida
├── 06-etica-accesibilidad/   ← patrones oscuros, prueba ética, cruce con WCAG 2.2
├── 07-plantillas/            ← informe de auditoría, ficha de decisión, plantilla de ficha de ley
├── 08-fuentes/               ← bibliografía, fuentes por ley, sobre Laws of UX
├── datos/                    ← leyes.json, relaciones.json (generados)
├── adaptadores/              ← cómo usarlo en cada plataforma + prompt de sistema compacto
├── herramientas/             ← validar.py, generar_indices.py, empaquetar.py (Python 3.8+, sin dependencias)
└── dist/                     ← paquetes de un solo archivo (generados)
```

## Uso rápido

| Plataforma | Cómo |
|---|---|
| Agentes que leen `AGENTS.md` (Codex, Cursor, Copilot agent, Windsurf, Claude Code…) | Abre o referencia la carpeta; el agente sigue `AGENTS.md`. |
| Claude (skills) | Copia la carpeta en `~/.claude/skills/ux-skill/` o súbela como skill; `SKILL.md` la activa. |
| ChatGPT (GPT personalizado / Proyectos), Gemini (Gems), NotebookLM | Instrucciones = `adaptadores/prompt-sistema-compacto.md`; conocimiento = `dist/ux-skill-completo.md`. |
| API de cualquier proveedor | Prompt de sistema compacto + recuperación (RAG) sobre `01-leyes/` o `datos/leyes.json`. |
| Modelos locales (Ollama, LM Studio…) | `SYSTEM` = prompt compacto; si el contexto lo permite, añade `dist/ux-skill-nucleo.md`. |

Detalle en [`adaptadores/README.md`](adaptadores/README.md).

## Mantenimiento

```bash
python herramientas/generar_indices.py   # regenera índice, matriz y JSON desde las fichas
python herramientas/validar.py           # comprueba coherencia (30 fichas, secciones, ids, enlaces)
python herramientas/empaquetar.py        # genera dist/ (paquetes de un archivo)
```

En Windows: `py herramientas\validar.py`, etc.
Las **fichas son la fuente de verdad**: para cambiar relaciones o evidencia, edita el front
matter de la ficha y regenera. Para añadir una ley, usa `07-plantillas/plantilla-ficha-ley.md`.

## Rigor y principios del sistema

- **No todas las leyes son iguales.** Cada ficha declara un nivel de evidencia (E1 ley
  cuantitativa · E2 efecto robusto · E3 evidencia mixta · C constructo · H heurística).
- **Se corrigen errores frecuentes** de la divulgación: p. ej. "7±2 elementos por menú" es un
  mal uso de Miller; el umbral de 400 ms de Doherty es una regla derivada (el folleto de IBM
  de 1982 no la enuncia literalmente); el efecto de sobrecarga de opciones tiene efecto medio
  cercano a cero en metaanálisis salvo con ciertos moderadores; la ventaja de memoria del
  efecto Zeigarnik no se replica en el metaanálisis de 2025.
- **Ética y accesibilidad** no son un anexo: cada ficha tiene su sección y hay reglas de oro.
- **Fuentes trazables**: cada ficha distingue fuentes primarias, secundarias y lo no verificado.

## Licencia y atribución

El contenido de lawsofux.com es © Jon Yablonski bajo licencia
[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). Este sistema **no
reproduce ni traduce** sus textos: es una **síntesis original** que estudia las mismas leyes
y sus fuentes académicas, cita Laws of UX como referencia en cada ficha y enlaza a ella.
Las fuentes primarias se citan en `08-fuentes/`. Ver `08-fuentes/sobre-laws-of-ux.md`.

Versión 1.0 · octubre de 2026.
