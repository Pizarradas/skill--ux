# Instrucciones de UX para GitHub Copilot

Este repositorio incluye `ux-skill/`, un sistema de conocimiento de UX basado en las leyes
de UX y sus fuentes. Al generar o revisar código de interfaz:

- Sigue `ux-skill/AGENTS.md` (reglas R1–R10) y, para revisiones, `ux-skill/04-procesos/revisar-codigo-ui.md`.
- Objetivos táctiles ≥ 44 px (mínimo 24×24 px CSS, WCAG 2.5.8); feedback inmediato en cada acción y estados de carga; formularios con `<label>` visible, `autocomplete`, `inputmode`, validación en línea con mensajes que expliquen cómo corregir; entrada tolerante (normaliza espacios y separadores) que muestre la interpretación.
- Una acción primaria por vista; mismos componentes para la misma función; no comunicar sólo con color; respetar `prefers-reduced-motion`.
- Usa controles nativos o patrones WAI-ARIA APG con comportamiento estándar de teclado.
- No implementes patrones oscuros (casillas preseleccionadas de pago, urgencia falsa, cancelación más difícil que el alta).
- Cuando justifiques una decisión, cita la ley por id (p. ej. `ACC-01 Ley de Fitts`) y su mecanismo.
