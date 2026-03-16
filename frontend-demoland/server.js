/**
 * EncryptVault demoLand Server — port 3006
 */
const express = require('express');
const path = require('path');
const cors = require('cors');
const app = express();
const PORT = process.env.PORT || 3006;
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));
app.get('/api/health', (req, res) => { res.json({ status: 'ok', app: 'encryptvault-demoland', timestamp: new Date() }); });
app.get('*', (req, res) => { res.sendFile(path.join(__dirname, 'public', 'index.html')); });
app.listen(PORT, () => { console.log(`EncryptVault demoLand running at http://localhost:${PORT}`); });
