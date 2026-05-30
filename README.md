# OptimizeMyLife

OptimizeMyLife est une plateforme premium pour **apprendre l'IA en famille**, avec
**Félix**, un mentor IA qui accompagne chaque apprenant selon son âge. Site statique
(HTML / CSS / JS, sans framework), déployé via GitHub Pages.

## Pages & sections

| Fichier | Rôle |
|---------|------|
| `index.html` | Homepage premium : hero, bloc vidéo (Félix mentor), présentation produit, section cours, carousel de screenshots annotés, cours vivants + plan de veille IA, CTA. |
| `produits/junior.html` | Parcours Junior 9–14 ans. |
| `produits/ado.html` | Parcours Ado 15–21 ans. |
| `produits/business-ia.html` | Parcours Business IA (adultes). |
| `produits/package-cours.html` | Package de cours tout-en-un + formules. |
| `cockpit.html` | Cockpit / dashboard apprenant (progression, stats, suggestions de Félix). |
| `rapport-parent.html` | Rapport parent, **mode foncé/clair** commutable. |
| `login.html` | Connexion + volet « modèles / références » de Félix. |
| `agent-lab.html` | Agent Lab : évolution des capacités de Félix. |

Code partagé : `styles.css` (design system + thème foncé) et `scripts/app.js`
(nav mobile, dropdown, carousel, modale vidéo, thème, reveal, détection des assets Félix).

## Félix — règle d'identité

Félix doit rester **exactement** le même personnage que dans les références :
même style, même couleur, même design. On n'utilise que ses **émotions**.
Les images vivent dans `assets/felix/` — voir **`assets/felix/README.md`** pour la
liste des fichiers attendus. Tant qu'un asset manque, un **emplacement marqué**
s'affiche (le site ne casse pas).

## Règles de copy

- Texte principal en **français**.
- Parent / admin : **vouvoiement**. Jeunes dans les cours : **tutoiement**.
- **Aucune** promesse de revenus garantis, aucun ton « get rich quick ».

## Développement

```bash
npm run lint    # vérifie structure HTML, liens internes, accessibilité de base
npm run build   # valide le site, inventorie les assets manquants, écrit build-report.json
npm run check   # lint + build
```

Le site est statique : ouvrez `index.html` dans un navigateur, ou servez le dossier
(`python3 -m http.server`). Le déploiement GitHub Pages publie le dépôt tel quel.
