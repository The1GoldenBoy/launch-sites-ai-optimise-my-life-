/**
 * OptimizeMyLife — "build" sans dépendance.
 * Le site étant statique (déployé tel quel via GitHub Pages), le build :
 *  1. vérifie que les fichiers cœur existent ;
 *  2. inventorie les références d'assets (Félix / images) et signale
 *     celles encore manquantes (emplacements à remplir) ;
 *  3. écrit un manifeste build-report.json ;
 *  4. confirme que le site est prêt à être déployé.
 * Les assets manquants sont des AVERTISSEMENTS (placeholders prévus),
 * pas des erreurs — le build reste vert.
 */
import { readFileSync, readdirSync, statSync, existsSync, writeFileSync } from "node:fs";
import { join, dirname, resolve, relative } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const errors = [];
const missingAssets = new Set();

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
const rel = (p) => relative(ROOT, p);

// 1. Fichiers cœur
for (const core of ["index.html", "styles.css", "scripts/app.js"]) {
  if (!existsSync(join(ROOT, core))) errors.push(`Fichier cœur manquant : ${core}`);
}

// 2. Inventaire des assets référencés
const files = htmlFiles(ROOT);
const pages = [];
for (const file of files) {
  const src = readFileSync(file, "utf8");
  const dir = dirname(file);
  pages.push(rel(file));
  const assetRe = /(?:src|href)=["']([^"'#?]+\.(?:png|jpe?g|webp|svg|gif))["']/gi;
  let m;
  while ((m = assetRe.exec(src)) !== null) {
    const target = m[1];
    if (/^https?:\/\//i.test(target) || target.startsWith("data:")) continue;
    const resolved = resolve(dir, target);
    if (!existsSync(resolved)) missingAssets.add(rel(resolved));
  }
}

// 3. Manifeste
const report = {
  generatedAt: new Date().toISOString(),
  pages: pages.sort(),
  missingAssets: [...missingAssets].sort(),
  ok: errors.length === 0,
};
writeFileSync(join(ROOT, "build-report.json"), JSON.stringify(report, null, 2));

// Rapport console
console.log(`\n🏗  Build OptimizeMyLife (site statique)\n`);
console.log(`   Pages : ${pages.length}`);
console.log(`   Manifeste : build-report.json`);

if (missingAssets.size) {
  console.log(`\n⚠️  ${missingAssets.size} asset(s) encore à déposer (emplacements prévus) :`);
  for (const a of [...missingAssets].sort()) console.log("   - " + a);
  console.log("   → Voir assets/felix/README.md. Les placeholders s'affichent en attendant.");
}

if (errors.length) {
  console.error(`\n❌ ${errors.length} erreur(s) :`);
  for (const e of errors) console.error("   - " + e);
  process.exit(1);
}
console.log("\n✅ Build réussi : le site est prêt à être déployé.\n");
