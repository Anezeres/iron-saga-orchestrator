const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

const armasPorUsuario = {}; // Estructura: { usuario: { tipo, modo, carga } }

// Simula falla aleatoria (por defecto 25%)
function fallaAleatoria(probabilidad = 0.25) {
  return Math.random() < probabilidad;
}

// Endpoint para activar armas
app.post('/activate', (req, res) => {
  const user = req.body.user;

  if (fallaAleatoria()) {
    return res.status(500).json({ message: `Fallo al activar armas para ${user}` });
  }

  if (!armasPorUsuario[user]) {
    armasPorUsuario[user] = {
      tipo: 'repulsor',    // por defecto
      modo: 'manual',      // por defecto
      carga: 0             // comienza descargada
    };
  }

  res.status(200).json({ message: `Armas activadas para ${user}` });
});

// Endpoint para cancelar armas
app.post('/cancel', (req, res) => {
  const user = req.body.user;

  if (armasPorUsuario[user]) {
    delete armasPorUsuario[user];
    return res.status(200).json({ message: `Activación de armas cancelada para ${user}` });
  } else {
    return res.status(404).json({ message: `No hay armas activadas para ${user}` });
  }
});

// Endpoint para ver estado
app.get('/estado', (req, res) => {
  res.status(200).json({ armas: armasPorUsuario });
});

// Endpoint para cambiar tipo de arma
app.post('/set-weapon-type', (req, res) => {
  const { user, tipo } = req.body;

  if (armasPorUsuario[user]) {
    armasPorUsuario[user].tipo = tipo;
    return res.status(200).json({ message: `Tipo de arma de ${user} cambiado a ${tipo}` });
  } else {
    return res.status(404).json({ message: `El usuario ${user} no tiene armas activadas` });
  }
});

// Endpoint para cambiar modo de ataque
app.post('/set-weapon-mode', (req, res) => {
  const { user, modo } = req.body;

  if (armasPorUsuario[user]) {
    armasPorUsuario[user].modo = modo;
    return res.status(200).json({ message: `Modo de ataque de ${user} cambiado a ${modo}` });
  } else {
    return res.status(404).json({ message: `El usuario ${user} no tiene armas activadas` });
  }
});

// Endpoint para cargar armas
app.post('/cargar', (req, res) => {
  const { user } = req.body;

  if (armasPorUsuario[user]) {
    armasPorUsuario[user].carga = 100;
    return res.status(200).json({ message: `Armas de ${user} cargadas al 100%` });
  } else {
    return res.status(404).json({ message: `El usuario ${user} no tiene armas activadas` });
  }
});

app.listen(5006, () => {
  console.log('Weapon Service listening on port 5004');
});
