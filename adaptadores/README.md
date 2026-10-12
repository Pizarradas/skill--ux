# Adaptadores: cómo usar UX Skill en cada plataforma

El sistema es Markdown plano + JSON. No depende de herramientas propietarias. Elige
la vía según lo que admita tu plataforma:

| Capacidad de la plataforma | Qué usar |
|---|---|
| Lee carpetas/repositorios (agentes de código) | La carpeta completa; el agente sigue `AGENTS.md` |
| Admite "skills" con front matter | La carpeta completa; `SKILL.md` la registra |
| Instrucciones + archivos de conocimiento | `prompt-sistema-compacto.md` + `dist/ux-skill-completo.md` |
| Sólo un prompt de sistema | `prompt-sistema-compacto.md` (autosuficiente) |
| API con recuperación (RAG) | Prompt compacto + índice vectorial sobre `01-leyes/*.md` (una ficha = un documento) o `datos/leyes.json` |

Genera los paquetes con `python herramientas/empaquetar.py` (crea `dist/`).

---

## Claude

- **Claude Code / Agent SDK:** copia la carpeta a `~/.claude/skills/ux-skill/` (personal) o
  a `.claude/skills/ux-skill/` dentro de un proyecto. `SKILL.md` contiene la descripción que
  activa la skill; el cuerpo remite a `AGENTS.md`.
- **Claude.ai (Proyectos):** instrucciones del proyecto = `prompt-sistema-compacto.md`;
  conocimiento = `dist/ux-skill-completo.md` (o la carpeta `01-leyes/` + guías).
- **Claude.ai (skills subidas):** comprime la carpeta en .zip con `SKILL.md` en la raíz y súbela.

## OpenAI (ChatGPT, GPTs, Codex)

- **GPT personalizado:** *Instructions* = `prompt-sistema-compacto.md`; *Knowledge* =
  `dist/ux-skill-completo.md` (y opcionalmente `datos/leyes.json`).
- **Proyectos de ChatGPT:** igual que arriba.
- **Codex / agentes que leen `AGENTS.md`:** abre la carpeta o colócala en el repo; `AGENTS.md` se lee automáticamente.

## Google (Gemini, Gems, NotebookLM)

- **Gem:** instrucciones = `prompt-sistema-compacto.md`; archivos = `dist/ux-skill-completo.md`.
- **NotebookLM:** sube `dist/ux-skill-completo.md` o las carpetas `01-leyes/` y `03-aplicacion/`
  como fuentes.
- **Gemini CLI:** admite archivos de contexto; referencia `AGENTS.md` (o cópialo como `GEMINI.md`).

## Editores y asistentes de código

- **Cursor:** copia `adaptadores/cursor/ux-leyes.mdc` a `.cursor/rules/` del proyecto y la
  carpeta `ux-skill/` al repo (o ajusta las rutas).
- **GitHub Copilot:** copia `adaptadores/copilot/copilot-instructions.md` a
  `.github/copilot-instructions.md`.
- **Windsurf, Cline, Continue, Aider, Zed…:** la mayoría lee `AGENTS.md` o un archivo de
  reglas; apunta su regla a `ux-skill/AGENTS.md`.

## API de cualquier proveedor

```text
system: <contenido de adaptadores/prompt-sistema-compacto.md>
        + (opcional) <dist/ux-skill-nucleo.md>
user:   <petición>
```

Con RAG: recupera las fichas por id (`datos/leyes.json` → campo `archivo`) o por similitud
semántica con la petición, y añade la(s) ficha(s) y la guía de contexto relevantes al prompt.
Recomendación: incluye siempre `02-relaciones/tensiones.md` y la ética si la petición
toca persuasión, precios, datos o urgencia.

## Modelos locales (Ollama, LM Studio, llama.cpp…)

Modelfile de ejemplo (Ollama):

```text
FROM <tu-modelo>
SYSTEM """<contenido de adaptadores/prompt-sistema-compacto.md>"""
PARAMETER num_ctx 16384
```

Con contextos pequeños, usa sólo el prompt compacto y pega la ficha de la ley pertinente
en la conversación cuando haga falta.

## Comprobar que funciona

Prueba con las peticiones de `adaptadores/pruebas.md` y compara la respuesta con los
criterios de aceptación que allí se indican.
