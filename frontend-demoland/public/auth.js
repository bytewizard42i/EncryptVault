/**
 * EncryptVault — demoLand Authentication Module
 * localStorage-based auth following the DIDzMonolith auth standard.
 */
const EV_STORAGE_KEY = 'encryptvault_demo_users';
const EV_SESSION_KEY = 'encryptvault_session';

function evReadUsers() { try { return JSON.parse(localStorage.getItem(EV_STORAGE_KEY) || '[]'); } catch { return []; } }
function evWriteUsers(u) { localStorage.setItem(EV_STORAGE_KEY, JSON.stringify(u)); }
function evGetSession() { try { return JSON.parse(localStorage.getItem(EV_SESSION_KEY)); } catch { return null; } }
function evSetSession(s) { localStorage.setItem(EV_SESSION_KEY, JSON.stringify(s)); }
function evClearSession() { localStorage.removeItem(EV_SESSION_KEY); }

function evSignup(data) {
  const users = evReadUsers();
  if (users.some(u => u.email.toLowerCase() === data.email.toLowerCase()))
    throw new Error('An account with email "' + data.email + '" already exists.');
  users.push(data);
  evWriteUsers(users);
  const session = { userId: 'demo-' + data.email, displayName: data.firstName + ' ' + data.lastName, email: data.email, authMethod: data.signupMethod, authenticatedAt: new Date().toISOString() };
  evSetSession(session);
  console.log('[demoLand] New user signed up: ' + session.displayName);
  return session;
}

function evLogin(method, email) {
  const users = evReadUsers();
  const found = users.find(u => u.email.toLowerCase() === (email || '').toLowerCase());
  const session = { userId: found ? 'demo-' + found.email : 'user-001', displayName: found ? found.firstName + ' ' + found.lastName : 'Demo User', email: found ? found.email : 'demo@encryptvault.io', authMethod: method, authenticatedAt: new Date().toISOString() };
  evSetSession(session);
  return session;
}

function evLogout() { evClearSession(); window.location.href = '/login.html'; }
function evRequireAuth() { const s = evGetSession(); if (!s) { window.location.href = '/login.html'; return null; } return s; }

const EV_SIM = {
  'email':        ['Deriving Argon2id key...', 'Key derived', 'Session established!'],
  'pgp-key':      ['Scanning for hardware keys...', 'NitroKey detected', 'Reading PGP public key...', 'Fingerprint verified!'],
  'yubikey':      ['Waiting for YubiKey...', 'YubiKey 5 detected', 'FIDO2 challenge...', 'Touch now...', 'Verified!'],
  'did-wallet':   ['Connecting to DID wallet...', 'DID resolved...', 'Identity verified!'],
  'trezor':       ['Scanning for Trezor...', 'Trezor 5 detected', 'Deriving Ed25519 key...', 'Confirm on device...', 'Confirmed!'],
  'biometric':    ['Initializing WebAuthn...', 'Requesting biometric...', 'Scanning...', 'FIDO2 verified!'],
  'chrome-oauth': ['Redirecting to Google...', 'Token received', 'Google confirmed!'],
  'brave-oauth':  ['Connecting to Brave...', 'BAT wallet linked', 'Brave confirmed!'],
};
async function evRunSim(method, cb) { const steps = EV_SIM[method] || ['Connecting...', 'Done!']; for (const m of steps) { cb(m); await new Promise(r => setTimeout(r, 900)); } }
