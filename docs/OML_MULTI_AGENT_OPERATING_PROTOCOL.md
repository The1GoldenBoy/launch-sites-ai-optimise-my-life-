# OptimizeMyLife — Bilingual Multi-Agent Operating Protocol

## FR — Décision

La meilleure structure n'est pas de donner un gros prompt directement à Claude ou Codex à chaque fois. La meilleure structure est:

1. **Enzo/Hermes = chef d'orchestre et vérificateur final**
2. **Claude Code Manager = manager spécialisé pour Claude Code Opus**
3. **Codex Manager = manager spécialisé pour Codex**
4. **Claude Code = production premium UX/app/copy**
5. **Codex = QA, garde-fous, refactor ciblé, intégration, contre-review**

Le manager ne remplace pas Claude/Codex. Il prépare leur mission, limite le scope, vérifie le contexte, surveille les outputs, demande les corrections, et empêche les collisions.

## EN — Decision

The best structure is not to paste one huge prompt directly into Claude or Codex every time. The best structure is:

1. **Enzo/Hermes = orchestrator and final verifier**
2. **Claude Code Manager = dedicated manager for Claude Code Opus**
3. **Codex Manager = dedicated manager for Codex**
4. **Claude Code = premium UX/app/copy production**
5. **Codex = QA, guardrails, targeted refactors, integration, counter-review**

The manager does not replace Claude/Codex. It prepares the mission, limits scope, verifies runtime context, monitors outputs, requests fixes, and prevents collisions.

## FR — Règles permanentes

- Empire OS commande. Le repo exécute. Linear assigne. GitHub implémente. Enzo vérifie.
- Pas de travail direct sur `main`.
- Un agent = une branche = un scope.
- Claude et Codex ne modifient pas les mêmes fichiers en même temps sans branche d'intégration.
- Félix exact seulement: aucune recréation, aucun redesign.
- Pas de vrai backend/auth/paiement sans approbation de Max.
- Le login doit exister visuellement, mais rester clairement prototype tant que backend non approuvé.
- Toute affirmation “done” doit être appuyée par commandes, PR, diff, tests/checks, et preview si applicable.

## EN — Permanent rules

- Empire OS commands. The repo executes. Linear assigns. GitHub implements. Enzo verifies.
- No direct work on `main`.
- One agent = one branch = one scope.
- Claude and Codex must not edit the same files at the same time without an integration branch.
- Exact Félix only: no recreation, no redesign.
- No real backend/auth/payment without Max's approval.
- Login must exist visually, but remain clearly prototype until backend is approved.
- Every “done” claim must be backed by commands, PR, diff, checks/tests, and preview when applicable.
