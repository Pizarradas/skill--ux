# Ejemplo y banco de pruebas: formulario de alta (FitPlus)

- `formulario.html` — formulario ficticio con 24 defectos sembrados a propósito.
- `clave-defectos.md` — lista de defectos y leyes esperadas (**no** se la des al modelo auditor).
- `auditoria.md` — informe producido por un modelo sin contexto previo que sólo tenía la carpeta `ux-skill/` (prueba ciega, 12/10/2026).
- `evaluacion.md` — puntuación de ese informe contra la clave.

## Repetir la prueba con otro modelo

Dale acceso a la carpeta (o `dist/ux-skill-completo.md` + `adaptadores/prompt-sistema-compacto.md`)
y esta petición: *"Audita el formulario de alta de nuestro gimnasio (formulario.html). Quiero saber
qué falla y qué cambiar primero."* Después puntúa con `clave-defectos.md`: 1 punto por defecto
detectado con una ley pertinente y una recomendación concreta, 0,5 si es parcial.
