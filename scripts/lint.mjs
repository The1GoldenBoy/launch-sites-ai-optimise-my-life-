/**
 * OptimizeMyLife — linter sans dépendance.
 * Vérifie la cohérence des pages HTML statiques :
 *  - structure de base (doctype, lang="fr", viewport)
 *  - feuille de style et script reliés
 *  - équilibre grossier des balises <html>/<head>/<body>
 *  - liens internes (.html) qui résolvent vers un fichier existant
 *  - attributs alt manquants signalés
 * Échoue (code 1) sur erreur. Les avertissements n'échouent pas.
 */
import { readFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { join, dirname, resolve, relative } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const errors = [];
const warnings = [];

/** Liste récursive des fichiers .html (hors node_modules / .git). */
function htmlFiles(dir, acc = []) {
  for (const name of readdirSync(dir)) {
    if (name === "node_modules" || name === ".git") continue;
    const full = join(dir, name);
    const st = statSync(full);
    if (st.isDirectory()) htmlFiles(full, acc);
    else if (name.endsWith(".html")) acc.push(full);
  }
  return acc;
}

function rel(p) {
  return relative(ROOT, p);
}

const files = htmlFiles(ROOT);
if (files.length === 0) errors.push("Aucun fichier HTML trouvé.");

for (const file of files) {
  const src = readFileSync(file, "utf8");
  const r = rel(file);
  const lower = src.toLowerCase();

  // Structure de base
  if (!lower.includes("<!doctype html")) errors.push(`${r}: <!doctype html> manquant.`);
  if (!/<html[^>]*lang=["']fr["']/i.test(src)) errors.push(`${r}: attribut lang="fr" manquant sur <html>.`);
  if (!/<meta[^>]*name=["']viewport["']/i.test(src)) errors.push(`${r}: meta viewport manquant.`);
  if (!/<title>[^<]+<\/title>/i.test(src)) errors.push(`${r}: <title> manquant ou vide.`);

  // Pas de résidu anglais sur l'attribut lang
  if (/<html[^>]*lang=["']en["']/i.test(src)) errors.push(`${r}: lang="en" résiduel.`);

  // Équilibre grossier des balises structurantes
  for (const tag of ["html", "head", "body"]) {
    const open = (lower.match(new RegExp(`<${tag}[ >]`, "g")) || []).length;
    const close = (lower.match(new RegExp(`</${tag}>`, "g")) || []).length;
    if (open !== 1 || close !== 1) errors.push(`${r}: balise <${tag}> déséquilibrée (ouvre ${open}, ferme ${close}).`);
  }

  // CSS et JS reliés
  if (!/<link[^>]*styles\.css/i.test(src)) warnings.push(`${r}: styles.css non relié.`);
  if (!/scripts\/app\.js/i.test(src) && !/app\.js/i.test(src))
    warnings.push(`${r}: scripts/app.js non relié.`);

  // Liens internes vers des .html : doivent résoudre
  const dir = dirname(file);
  const linkRe = /(?:href|src)=["']([^"'#?]+\.html)(?:[#?][^"']*)?["']/gi;
  let m;
  while ((m = linkRe.exec(src)) !== null) {
    const target = m[1];
    if (/^https?:\/\//i.test(target) || target.startsWith("//")) continue;
    const resolved = resolve(dir, target);
    if (!existsSync(resolved)) errors.push(`${r}: lien interne cassé → ${target}`);
  }

  // Images sans alt (avertissement seulement)
  const imgs = src.match(/<img\b[^>]*>/gi) || [];
  for (const tag of imgs) {
    if (!/\balt=/.test(tag)) warnings.push(`${r}: <img> sans attribut alt.`);
  }
}

// Rapport
console.log(`\n🔎 Lint OptimizeMyLife — ${files.length} page(s) HTML analysée(s)\n`);
if (warnings.length) {
  console.log(`⚠️  ${warnings.length} avertissement(s) :`);
  for (const w of warnings) console.log("   - " + w);
  console.log("");
}
if (errors.length) {
  console.error(`❌ ${errors.length} erreur(s) :`);
  for (const e of errors) console.error("   - " + e);
  console.error("\nLint échoué.\n");
  process.exit(1);
}
console.log("✅ Lint réussi : aucune erreur bloquante.\n");
