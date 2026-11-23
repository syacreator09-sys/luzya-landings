# LUZYA Commercial Showcase V1

Tres demos HTML/CSS independientes: `saas/`, `ecommerce/` y `servicios/`.

- Sin JS externo, cookies, fuentes remotas, analytics, pagos ni backend.
- Formularios interceptados en cliente; **no se transmiten ni guardan datos**.
- Precios/productos/resultados ilustrativos explícitos; no son ofertas reales.
- Diseño responsive, labels, focus visible, `role=status`, metadatos SEO básicos y preferencia de movimiento reducido.
- Ilustraciones de interfaz CSS, no screenshots reales ni diseño de Figma.
- Solo modifica `commercial-showcase/`; no toca páginas existentes ni Shared/Design System.

## Validación local

```bash
python -m http.server 8000
# Abrir http://localhost:8000/commercial-showcase/
```

Comprobar manualmente navegador escritorio/móvil, foco, formularios y accesibilidad antes de marcar DEMO FUNCIONAL. **Esta implementación aún no acredita revisión visual de navegador**, despliegue, métricas Lighthouse ni integración runtime con Design System.
