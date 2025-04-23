const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// Datos simulados
const aiStatus = {
  isActive: false,
  currentAI: null,
  personality: null
};

// Endpoint: Iniciar IA
app.post('/boot-ai', (req, res) => {
  const { AI = "JARVIS", language = "en", personality = "default" } = req.body;

  if (Math.random() < 0.2) { // 20% de probabilidad de fallo
    return res.status(500).json({ 
      error: "AI boot sequence failed. Rebooting..." 
    });
  }

  aiStatus.isActive = true;
  aiStatus.currentAI = AI;
  aiStatus.personality = personality;

  // Respuestas personalizadas
  const responses = {
    JARVIS: `"Good ${timeOfDay()}, Sir. All systems are ready."`,
    FRIDAY: `"Hello Boss. I'm online and fully operational."`
  };

  res.status(200).json({
    status: "AI_online",
    ai: AI,
    language,
    personality,
    message: responses[AI] || "AI activated."
  });
});

// Endpoint: Apagar IA (compensación)
app.post('/shutdown-ai', (req, res) => {
  aiStatus.isActive = false;
  res.status(200).json({ 
    status: "AI_offline",
    message: "AI system terminated." 
  });
});

// Helper
function timeOfDay() {
  const hour = new Date().getHours();
  return hour < 12 ? "morning" : hour < 18 ? "afternoon" : "evening";
}

app.listen(5003, () => {
  console.log('AI Service running on port 5003 | J.A.R.V.I.S. awaiting...');
});