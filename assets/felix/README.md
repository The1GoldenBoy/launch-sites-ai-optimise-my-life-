# Assets Félix — emplacements à remplir

> **Règle d'identité (non négociable).** Félix doit rester **exactement** le même
> personnage que dans le build pack : même style, même couleur, même design.
> On ne le redessine pas, on ne le transforme pas en mascotte générique.
> On utilise seulement ses **émotions** selon le guide.

## Pourquoi ce dossier est vide

Le build pack original (`docs/claude-opus-4-8-optimizemylife-build-pack/`) et les
assets Félix vivent sur la machine locale et **n'ont pas été commités** dans ce
dépôt cloud. Le code de l'app référence donc ces fichiers ; tant qu'ils sont
absents, un **emplacement marqué** (cadre orange en pointillés) s'affiche à leur
place — rien ne casse.

## Fichiers attendus (dépose-les ici)

Copie les images depuis `assets/felix-character-lock/` du build pack, en
conservant Félix identique, sous ces noms :

| Fichier                      | Émotion / usage                         | Où il apparaît |
|------------------------------|-----------------------------------------|----------------|
| `felix-mentor.png`           | Félix mentor, pose d'accueil            | Hero homepage, bloc vidéo |
| `felix-badge.png`            | Tête / buste cadré serré                | Logo nav + footer + cockpit |
| `felix-wave.png`             | Salut / bienvenue                       | Login, onboarding |
| `felix-thinking.png`         | Réflexion / analyse                     | Agent Lab |
| `felix-celebrate.png`        | Félicitations / réussite                | Cockpit (jalons) |
| `felix-teach.png`            | Explication / cours                     | Section cours, produits |
| `felix-junior.png`           | Variante ton Junior 9–14                | Page Junior |
| `felix-ado.png`              | Variante ton Ado 15–21                  | Page Ado |
| `felix-business.png`         | Variante ton Business adulte            | Page Business IA |

Formats acceptés : `.png` (transparent recommandé), `.webp` ou `.svg`.
Si tu utilises un autre format, ajuste l'attribut `src` dans les pages HTML.

## Screenshots produit / boîtes

- Captures annotées du carousel → `assets/img/shot-*.png`
- Boîtes produit (`assets/product-boxes/`) → `assets/img/box-*.png`
- Références de design des pages → consultées pour la mise en page,
  pas embarquées dans le site.

Tant qu'un fichier manque, l'emplacement reste visible et documenté à l'écran.
