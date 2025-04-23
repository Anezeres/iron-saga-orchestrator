# 🚀 Proyecto: Patrón Saga para Activación de Traje de Iron Man

## 📌 Objetivo
Implementar un sistema distribuido que simule el proceso de activación del traje de Iron Man usando el patrón Saga con orquestación centralizada, donde cada microservicio representa un subsistema crítico del traje.

## 🛠 Stack Tecnológico
| Componente       | Tecnología           |
|------------------|----------------------|
| Orquestador      | Python + Flask       |
| Microservicios   | Python/Node.js       |
| Comunicación     | REST API             |
| Contenedores     | Docker + Compose     |
| Persistencia     | In-memory (arrays)   |


## 🔄 Flujo de la Saga
- Activación del reactor ARC (core_service)
- Inicialización del casco (helmet_service)
- Ensamblaje de la armadura (armor_service)
- Carga de armas (weapon_service)
- Diagnóstico de sistemas (diagnostic_service)
- Inicio de la IA (ai_service)
