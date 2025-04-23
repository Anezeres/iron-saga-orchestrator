const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

const checkDiagnosticService = [];

// Simular falla aleatoria
function fallaAleatoria(probabilidad = 0.3) {
  return Math.random() < probabilidad;
}

app.post('/run-checks', (req, res) => {
  const diagnostic = req.body.diagnostic;

  if (fallaAleatoria()) {
    return res.status(500).json({ message: `Ocurrió una falla al programar el diagnóstico de los sistemas` });
  }

  checkDiagnosticService.push(diagnostic);
  res.status(200).json({ message: `¡Diagnóstico programado!` });
});

app.post('/notify-failure', (req, res) => {
  const diagnostic = req.body.diagnostic;
  const index = checkDiagnosticService.indexOf(diagnostic);
  if (index !== -1) {
    checkDiagnosticService.splice(index, 1);
    res.status(200).json({ message: `Programación de diangóstico cancelada` });
  } else {
    res.status(404).json({ message: `Este diagnóstico no se ha programado o no se ha encontrado` });
  }
});

app.get('/diagnostics', (req, res) => {
  res.status(200).json(checkDiagnosticService);
});

app.listen(5005, () => {
  console.log('Jarvis Service listening on port 5005');
});