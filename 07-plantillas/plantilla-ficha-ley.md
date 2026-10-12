# Plantilla · Ficha de ley (para ampliar el sistema)

Todas las fichas de `01-leyes/` siguen esta estructura. Para añadir una ley nueva
(p. ej. una que no esté en Laws of UX), copia esta plantilla, asígnale un id libre de su
familia, añádela a `datos/leyes.json` y ejecuta `herramientas/validar.py`.

```markdown
---
id: FAM-NN
nombre: Nombre en español
nombre_en: English name
alias: [otros nombres]
familia: PER | MEM | DEC | ACC | MOT | SIS
evidencia: E1 | E2 | E3 | C | H
etiquetas: [..]
refuerza: [IDs]
tensiona: [IDs]
fuente_laws_of_ux: https://lawsofux.com/...
---

# FAM-NN · Nombre (*English name*)

> Enunciado en una frase.

**Idea clave para quien diseña:** …

## Resumen operativo
- **Qué dice:** …
- **Evidencia:** nivel — por qué (y el matiz que más se olvida)
- **Haz:** 1) … 2) … 3) …
- **Evita:** …
- **Sospecha de esta ley cuando…:** …
- **Mide con:** …
- **Vecinas:** ID (refuerza) · ID (tensiona, Tn)

## Origen
## Mecanismo
## Evidencia y límites
## Aplicación práctica
### Reglas
### Por contexto
## Anti-patrones
## Ética y accesibilidad
## Cómo auditarla
### Señales observables
### Preguntas
### Métricas
## Relaciones
## Fuentes
```
