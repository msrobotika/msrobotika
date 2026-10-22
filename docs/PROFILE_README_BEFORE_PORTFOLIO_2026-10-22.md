<div align="center">

# MS ROBOTIKA · Software abierto e investigación aplicada

**Automatización industrial · Visión artificial · Electrónica · IA reproducible**

[**Catálogo de 17 repositorios**](PROJECTS.md) · [**Guía para contribuir**](CONTRIBUTING.md) · [**Política de seguridad**](SECURITY.md)

</div>

> **Criterio editorial:** las capturas documentan software real cuando su procedencia está verificada; los resultados de investigación se distinguen de las reproducciones independientes; una ejecución de CI correcta no implica certificación industrial, médica ni validación física.

### Herramientas industriales

| Aplicación | Función principal | Evidencias |
|---|---|---|
| [AB-SCL Studio](https://github.com/msrobotika/AB-SCL-Studio) | Análisis ST/SCL → KOP booleano | [CI](https://github.com/msrobotika/AB-SCL-Studio/actions) · [Capturas](https://github.com/msrobotika/AB-SCL-Studio/tree/main/docs/screenshots) |
| [AB-KOP Studio](https://github.com/msrobotika/AB-KOP-Studio-v0.1) | Editor y simulador Ladder/KOP | [CI](https://github.com/msrobotika/AB-KOP-Studio-v0.1/actions) · [Capturas](https://github.com/msrobotika/AB-KOP-Studio-v0.1/tree/main/docs/screenshots) |
| [AB-GRAFCET Studio](https://github.com/msrobotika/AB-GRAFCET-Studio-v0.1-c) | GRAFCET, simulación y diagnóstico | [CI](https://github.com/msrobotika/AB-GRAFCET-Studio-v0.1-c/actions) · repo privado |
| [AB-Serial Analyzer](https://github.com/msrobotika/AB-Serial-Analyzer-v0.1-) | Monitor serie y Modbus RTU | [CI](https://github.com/msrobotika/AB-Serial-Analyzer-v0.1-/actions) · [Capturas](https://github.com/msrobotika/AB-Serial-Analyzer-v0.1-/tree/main/docs/screenshots) |
| [AB-Vision Inspector](https://github.com/msrobotika/-AB-Vision-Inspector) | Inspección y calibración vigilada | [CI](https://github.com/msrobotika/-AB-Vision-Inspector/actions) · [Capturas](https://github.com/msrobotika/-AB-Vision-Inspector/tree/main/docs/screenshots) |
| [AB-Modbus Studio](https://github.com/msrobotika/AB-Modbus-Studio) | Diagnóstico y herramientas Modbus | [CI](https://github.com/msrobotika/AB-Modbus-Studio/actions) · [Capturas](https://github.com/msrobotika/AB-Modbus-Studio/tree/main/docs/screenshots) |
| [AB-BI Studio](https://github.com/msrobotika/AB-BI-Studio) | Informes y visualización de datos | [CI](https://github.com/msrobotika/AB-BI-Studio/actions) · [Galería](https://github.com/msrobotika/AB-BI-Studio/tree/main/docs) |

**No se declara compatibilidad certificada de PLC, seguridad de maquinaria ni precisión metrológica trazable.** Cada programa documenta el alcance realmente implementado.

---

## Investigación y otros proyectos

El perfil original con la investigación de AB-GEN se conserva a continuación. Consulta primero el [catálogo general](PROJECTS.md) para versiones, visibilidad, licencias y próximos trabajos.

---

# Abel Moreno Bermejo
**AI Infrastructure & Sustainable Computing Researcher**

Trabajo en la intersección entre autonomía de agentes de IA, eficiencia computacional y sistemas capaces de ejecutarse en hardware accesible. Mi enfoque se centra en desarrollar arquitecturas que reduzcan coste, consumo y dependencia de infraestructura sin renunciar a trazabilidad y capacidad técnica.

---

## 🏗️ Ecosistema de Desarrollo — AB-Suite

### ⚡ AB-CODE | Autonomous Software Engineering
Agente de codificación local con memoria semántica vectorial y enrutamiento dinámico de modelos.
- **Enfoque:** RAG (Retrieval-Augmented Generation), herramientas y automatización del ciclo de desarrollo.
- **Objetivo:** análisis, modificación y validación de bases de código locales con mínima dependencia externa.

### 🤖 AB-AGENT-Core | Autonomous Reasoning Framework
Núcleo de orquestación basado en ciclos de planificación, ejecución y verificación.
- **Enfoque:** razonamiento autónomo, ejecución local y eficiencia de recursos.
- **Objetivo:** construir agentes auditables y útiles en entornos reales, incluidos escenarios Edge.

### 🧬 AB-GEN | Sustainable Model Architecture
Línea de investigación en clasificación visual mediante geometría, análisis espectral y meta-aprendizaje polinómico, sin una arquitectura CNN convencional.

**Resultado interno actualmente bajo reproducción:**
- CIFAR-10 — **80.14%** registrado para **V24 Slow Burn**.
- El benchmark energético publicado previamente está siendo sometido a una nueva validación reproducible y comparable antes de considerarse resultado confirmado.

**Estado actual:** auditoría de reproducibilidad, leakage, calibración, inferencia end-to-end, benchmark energético y trazabilidad XAI.

- Repositorio: https://github.com/msrobotika/AB-GEN-Green-AI
- Hitos y estado de validación: https://github.com/msrobotika/AB-GEN-Green-AI/blob/main/MILESTONES.md
- Portal público de investigación: https://msrobotikaabgenresearch.wordpress.com/

---

## 🛠️ Stack Técnico & Especialidades

- **IA y agentes:** arquitecturas de agentes, memoria vectorial, RAG, modelos locales y evaluación.
- **Machine Learning:** clasificación, ensembles, reducción dimensional, análisis espectral, métricas y reproducibilidad.
- **Ingeniería de software:** Python, JavaScript/Node.js, Docker, testing y Git.
- **Automatización industrial:** PLC, comunicaciones industriales, integración OT/IT y Edge Computing.
- **Principio de diseño:** resultados medibles, reproducibles y eficientes antes que fuerza bruta computacional.

---

## 📈 Línea de investigación

La hipótesis de trabajo detrás de AB-Suite es que parte del valor de la IA futura vendrá de arquitecturas mejor diseñadas, no únicamente de aumentar parámetros y consumo. Los proyectos se están estructurando para que los resultados puedan auditarse mediante código, versiones, métricas, pruebas y benchmarks reproducibles.

---

## 📫 Contacto y Recursos
- **Portal de investigación:** https://msrobotikaabgenresearch.wordpress.com/
- **Demos técnicas:** http://www.youtube.com/@MSRobotika
- **GitHub:** https://github.com/msrobotika
- **Email:** abelilloseven@gmail.com

> Los resultados experimentales se distinguen explícitamente entre *reportados* y *reproducidos/validados* hasta completar su evidencia técnica.
