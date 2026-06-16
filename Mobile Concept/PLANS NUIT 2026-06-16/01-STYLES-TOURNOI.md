# 01 — TOURNOI DE STYLES (3e compétition) — OptimizeMyLife mobile

> **Statut :** EXÉCUTÉ le 2026-06-16. La 3e compétition (qui avait planté à 0 KB en local) a été
> rejouée ici via un panel de 9 agents (5 en Phase 1, 4 en Phase 2) + synthèse.
> **Où ça a tourné :** session GitHub remote (repo `launch-sites-ai-optimise-my-life-`).
> Donc PAS d'images générées ici (étape 3 = local, app ChatGPT desktop). Ce doc = les PLANS.
> **À faire de ton bord :** copier ce dossier `Mobile Concept\` dans le vrai projet, et lire ce fichier
> AVANT de flipper le toggle Kids/Teen/Adult sur `/dashboard`.

---

## Format du tournoi

- **Phase 1 — 3 champions + 2 spécialistes :** un champion par style (Warm Minimal, Command Center,
  Wildcard) développe le style sur 4 surfaces (Dashboard, Welcome/Meet Félix, Learn, Product detail)
  + carte high-ticket. Plus un directeur artistique Félix + un ingénieur buildabilité.
- **Phase 2 — 4 critiques adversariaux :** poster/générique · concurrence · identité Félix + honnêteté ·
  UX mobile 390px.
- **Phase 3 — synthèse :** 3 styles affinés + 1 prompt GPT Image par style + verdict.

**Contraintes verrouillées injectées à tous (non négociables) :** vraie app jamais un poster, flat/clean,
ZÉRO golden-hour, palette blanc #ffffff + orange #f4731f + ink #0a0a0a (zéro beige/gris décoratif),
Félix identité-lockée (réf S09-T01 + « flat app lighting »), honnêteté absolue (zéro faux
prix/témoignage/IA/donnée — données honnêtes ou état vide), app role-adaptive (Kids 9-14 / Ados 15-20 / Adultes).

---

## RÉSULTAT EN UNE PHRASE

Le tournoi a fait émerger un **3e prétendant sérieux** — **« Le Dossier » (Clinical Confidence)** — que
**3 critiques sur 4** placent devant les deux favoris pour l'ICP adulte. **Command Center se fait disqualifier
sur l'honnêteté** (boot terminal = fausse IA système). **Warm Minimal** reste le meilleur fit Kids et un solide
défaut, mais seulement après avoir tué son dogme « zéro gris ».

| Critique adversarial | Gagnant désigné |
|---|---|
| Poster / générique | **Warm Minimal** (de justesse, après correction « zéro gris ») |
| Différenciation concurrentielle | **Le Dossier** (et de loin) |
| Identité Félix + honnêteté de marque | **Le Dossier** (Command Center à REJETER) |
| UX mobile 390px quotidienne | **Le Dossier** (corrigé) |

---

## LES 3 STYLES AFFINÉS (après passage adversarial)

### A. WARM MINIMAL v2 — friendly-premium honnête
**ADN :** fond blanc, accent orange chirurgical, géométrie sobre. Identité portée par une **structure de
hiérarchie**, pas par un effet → survit à 200 jours d'usage.
**Corrections imposées par le panel :**
1. **Tuer le dogme « zéro gris ».** Réintroduire un *gris fonctionnel* (texte secondaire, hairlines 6-8 %,
   états désactivés, skeletons). Le « zéro gris » est une règle de mockup, pas d'app — la hiérarchie
   s'effondre dès qu'un écran a 11 modules. Garder le blanc *dominant*, pas *exclusif*.
2. **Casser le radius uniforme** (tout à 20px = signature « bubble » générique type Notion/Linear/Headspace) :
   conteneurs 20px, éléments tactiles internes (chips, stats) 8-12px.
3. **CTA principal en sticky bottom** (zone pouce), jamais en héros qui exige de scroller.
**Meilleur fit :** **Kids 9-14** (chaleur, accueil) et défaut sûr. Pour l'adulte : agréable mais ne *prouve*
rien — dilue le claim « provably good ».
**Risque résiduel :** commodité (ressemble à 80 % des apps wellness/edtech). À s'approprier par l'orange-signature
+ la photo flat de Félix.

### B. COMMAND CENTER v2 — cockpit, gros nettoyage
**ADN :** ink #0a0a0a, bento, sentiment de pilotage. Reframe obligatoire : **pas « terminal de hacker »**
mais **« poste de pilotage de ta carrière à l'ère IA »**.
**Corrections imposées par le panel (sinon REJET) :**
1. **SUPPRIMER la séquence boot terminal.** C'est le point le plus grave : un faux `Initializing AI core…`
   simule une IA système qui n'existe pas = **mensonge sur la nature du produit** (un humain livre le service).
   Violation directe de la règle d'honnêteté. Si on garde un effet d'entrée : 1× au tout premier lancement,
   skippable, jamais rejoué, `prefers-reduced-motion` respecté.
2. **Sortir la mono de la lecture.** Mono réservé aux chiffres/IDs/timestamps ; corps et coaching en sans-serif
   (Inter). Data en `tabular-nums`, pas en mono fétiche.
3. **Lisibilité Félix sur sombre :** jamais sur #0a0a0a pur (peau cireuse/fake = sabotage du moat). Key light
   frontale chaude maintenue + fond dégradé charbon→bleu-nuit (#15171C→#0E0F13) + rim light acier discret +
   container disque. Anti-cerne explicite.
4. **A11y :** forcer `background-color:#0a0a0a` natif avant le 1er paint (sinon flash blanc) ; contraste AA réel
   sur le texte secondaire (le « tout gris sur noir » échoue souvent < 4.5:1) ; dark forcé = problème au soleil
   le matin → prévoir au moins la lisibilité extérieure.
**Meilleur fit :** **Ados 15-20** (esthétique OS/gaming) ; pour l'adulte, défendable seulement reframé
« mission control de carrière » et nettoyé du théâtre faux.
**Risque résiduel :** aliène l'ICP non-technique (marketeux/RH/finance = exactement les Exposed Professionals)
qui lisent « mono = je code, c'est pas pour moi ».

### C. ⭐ LE DOSSIER (Clinical Confidence) — NOUVEAU, recommandé pour l'adulte
**ADN :** fond **blanc** structuré par hairlines ink (≥20 % d'opacité — corrigé depuis 8-12 % jugé invisible),
chiffres **tabulaires**, métaphore **instrument de mesure de soi** (Whoop/Oura/finance) appliquée à la
compétence IA. Zéro carte ombragée, zéro bento. Orange **ultra-rationné** : uniquement l'état live/actif + le
CTA primaire + la signature de Félix.
**Pourquoi ça gagne (synthèse des critiques concurrence + honnêteté + UX) :**
- **Incarne « provably good ».** Le positionnement EST une métaphore de mesure. Comme Whoop ne t'apprend pas à
  dormir mais te *prouve* où tu en es, OML mesure ta **readiness face au remplacement IA** et la fait monter
  15 min/jour. Territoire **non occupé** en edtech IA (les concurrents = chatbots, listes de prompts, cours
  vidéo génériques).
- **L'honnêteté est le défaut natif.** Un dossier en construction avec des champs vides (`—`) se lit comme un
  document honnête, jamais comme une UI cassée. Aucun mécanisme (pas de ring feel-good, pas de boot, pas de
  badge « LIVE ») ne pousse à inventer de la donnée. C'est le **seul** style où l'état vide est élégant par nature.
- **Félix = expert-lecteur.** Dans un instrument, l'humain devient le cardiologue qui lit ton ECG : Félix
  *annote ton dossier* (notes signées + datées). Le high-ticket 10k$ on-site devient l'**escalade logique**
  (« tes métriques justifient une intervention sur site »), pas un upsell.
**Corrections imposées par le panel :**
1. **Hairlines ≥ 20 %** (8-12 % = fantômes au soleil / écran bas de gamme) + rôle hiérarchique (12/20/pleine),
   pas un tapis décoratif uniforme.
2. **Réchauffer le clinique** : l'orange #f4731f en accent humain unique + signature/note manuscrite de Félix,
   sinon le froid fait fuir le non-technique. Félix format passeport reste honnête (= la nature de S09-T01),
   mais ajouter nom écrit + phrase à la 1re personne pour humaniser ; l'agrandir sur le high-ticket.
3. **Pas d'uppercase tracking sur les labels répétés** (lecture 10-15 % plus lente) — réservé aux en-têtes de
   section rares ; sentence case pour tout ce qui se scanne 20×/jour.
4. **Accordéons ouverts par défaut sur le contenu chaud** (un accordéon fermé = 1 tap de plus chaque jour) ;
   cibles ≥ 48px.
**Risque résiduel :** trop clinique = anxiogène pour quelqu'un qui a *déjà* peur → mitiger par le ton des notes
de Félix (« on tient ça », jamais un jugement) ; convergence visuelle possible avec Command Center → garde-fou :
fond blanc non négociable + zéro bento + orange rationné.

---

## DÉCISION ADULTE — ce que le tournoi change

Avant le tournoi, le choix adulte était binaire : **clean (directive Max)** vs **cockpit sombre (panel marketing 70/30)**.
**Le tournoi ajoute une 3e voie qui pourrait être le vrai gagnant adulte : « Le Dossier ».** Il prend la
crédibilité-preuve du cockpit SANS le fond sombre qui salit Félix, sans le mono qui aliène le non-tech, et sans
le théâtre faux qui viole l'honnêteté.

**Reco du tournoi pour l'adulte :** **Le Dossier** (blanc-instrument, orange humain, Félix expert-lecteur).
**Reco par audience :** Kids → Warm Minimal ; Ados → Command Center v2 (nettoyé) ; Adultes → Le Dossier.
**Décision finale = Max**, via le toggle sur `/dashboard` une fois les 3 thèmes prototypés. Rien n'est verrouillé
ici — ceci est une recommandation argumentée, pas une décision.

---

## 1 PROMPT GPT IMAGE PAR STYLE (Dashboard, comme surface de référence)

> Tous : attacher la réf **`Felix Identity\S09-T01.png`**. Cible 390px (ratio portrait mobile ~9:19.5).
> Préfixe identité obligatoire : *« Match exact identity from reference S09-T01, flat app lighting,
> no golden-hour, no cinematic poster, real product UI screenshot. »*

**A — Warm Minimal v2 (Dashboard) :**
> Mobile app dashboard screenshot, 390px wide, pure white #ffffff background, friendly-premium. A hero
> "Next Best Action" card with soft warm tint #fff4ec and one solid orange #f4731f pill button. Below: a
> progress ring (orange arc on light track), three compact stat tiles, a module list with thin orange
> progress bars, and a small coach card with Felix as a clean cut-out portrait (warm soft frontal light,
> gentle floor shadow, no rim glow). Geometric sans-serif, ink #0a0a0a text plus functional grey for secondary
> labels, varied corner radii (20px containers, 10px chips). Flat clean real app, not a poster. Match exact
> identity from reference S09-T01.

**B — Command Center v2 (Dashboard, NETTOYÉ) :**
> Mobile app dashboard screenshot, 390px wide, dark ink #0a0a0a background, "career mission-control" cockpit
> (NOT a hacker terminal). Bento grid tiles (#111111, 1px #1c1c1c borders). One single vivid orange #f4731f
> "Next Action" tile. A 96px progress ring with tabular numerals, two mini-stat tiles, an honest AI-pulse strip.
> Felix in a contained portrait disc with a subtle charcoal-to-navy gradient behind him (#15171C→#0E0F13),
> warm frontal key light preserving natural skin tone, faint cool steel rim light — never on pure black, never
> cireux. Monospace only on numbers/IDs, Inter for text. Flat clean real app UI, not a poster. Match exact
> identity from reference S09-T01.

**C — Le Dossier / Clinical Confidence (Dashboard) :**
> Mobile app dashboard screenshot, 390px wide, pure white #ffffff "instrument" aesthetic like a premium
> health/finance app (Whoop/Oura/Mercury vibe) but warmer. Structure made of ink hairlines (~20% opacity),
> no shadowed cards, no bento. A top measurement banner "Day 14 / 90" with a graduated rule and an orange
> #f4731f live cursor. A vertical list of instrument-lines: label left (sentence case), large tabular numeral
> right, 1px sparkline. Orange used ONLY on the live state and the primary CTA. At the bottom, a small "file
> card" with Felix in a clean passport-style flat portrait, a handwritten-style signature and a short
> first-person dated note. Calm, rigorous, honest, real app UI, not a poster. Match exact identity from
> reference S09-T01.

> **Variantes à générer ensuite (étape 3, local) :** mêmes prompts déclinés par surface (Welcome/Meet Félix,
> Learn liste/leçon/exam, Product detail, carte high-ticket) × audience pertinente. Voir
> `00-GPT-IMAGE-PROMPTS-CONSOLIDÉS.md` pour le pack complet.

---

## VERBATIM DES JUGES (extraits clés à garder)

- **Poster :** « Le 2 et le 3 portent leur identité dans un *effet* — fait pour être vu, pas utilisé. Le 1 la
  porte dans une *structure de hiérarchie* qui survit à 200 jours. Mais tue le "zéro gris". »
- **Concurrence :** « Ton ICP n'achète pas du contenu, il achète de l'*anxiété convertie en preuve*. Whoop a
  bâti une catégorie de 3,6 G$ en mesurant, pas en coachant. Le Dossier fait de Félix un expert-lecteur et du
  10k$ on-site une escalade médicale logique. »
- **Honnêteté/Félix :** « Command Center est à REJETER — le boot terminal est un mensonge sur la nature du
  produit et il salit le visage de ton fondateur. Le Dossier est le seul style où l'honnêteté est le défaut natif. »
- **UX 390px :** « 3 corrections non négociables peu importe le style : (1) CTA principal sticky bottom, jamais
  scrollé ; (2) contraste AA réel + lignes ≥20% + cibles ≥48px ; (3) toute animation skippable ≤300ms,
  désactivée après le 1er run, `prefers-reduced-motion`. »

---

## 3 FAÇONS D'ÉCHOUER (issues du tournoi)

1. **Choisir Command Center pour l'adulte sans le nettoyer** → on viole l'honnêteté (boot terminal), on rend
   Félix cireux, et on aliène l'ICP non-technique. Le moat humain se retourne contre nous.
2. **Garder Warm Minimal « zéro gris » par pureté** → hiérarchie qui fond, scroll interminable, high-ticket
   jamais vu, app qui ressemble à 80 % du store.
3. **Faire Le Dossier froid** (clinique sans chaleur) → on amplifie l'anxiété de quelqu'un qui a déjà peur.
   L'orange humain + les notes signées de Félix sont obligatoires, pas optionnels.
