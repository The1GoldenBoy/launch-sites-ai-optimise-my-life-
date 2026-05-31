# OptimizeMyLife Agent Manager

## FR — Décision

La meilleure structure est:

1. Enzo/Hermes = chef d'orchestre et vérificateur final.
2. Claude Code Manager = manager spécialisé pour Claude Code Opus.
3. Codex Manager = manager spécialisé pour Codex.
4. Claude Code = production premium UX/app/copy.
5. Codex = QA, garde-fous, refactor ciblé, intégration, contre-review.

Le manager ne remplace pas Claude/Codex. Il prépare leur mission, limite le scope, vérifie le contexte, surveille les outputs, demande les corrections, et empêche les collisions.

## EN — Decision

The best structure is:

1. Enzo/Hermes = orchestrator and final verifier.
2. Claude Code Manager = dedicated manager for Claude Code Opus.
3. Codex Manager = dedicated manager for Codex.
4. Claude Code = premium UX/app/copy production.
5. Codex = QA, guardrails, targeted refactors, integration, counter-review.

The manager does not replace Claude/Codex. It prepares the mission, limits scope, verifies runtime context, monitors outputs, requests fixes, and prevents collisions.

## FR — Règles

- Empire OS commande. Le repo exécute. Linear assigne. GitHub implémente. Enzo vérifie.
- Pas de travail direct sur `main`.
- Un agent = une branche = un scope.
- Claude et Codex ne modifient pas les mêmes fichiers en même temps sans branche d'intégration.
- Félix exact seulement.
- Pas de vrai backend/auth/paiement sans approbation de Max.
- Le login visuel est requis, mais reste prototype tant que backend non approuvé.

## EN — Rules

- Empire OS commands. The repo executes. Linear assigns. GitHub implements. Enzo verifies.
- No direct work on `main`.
- One agent = one branch = one scope.
- Claude and Codex must not edit the same files at the same time without an integration branch.
- Exact Félix only.
- No real backend/auth/payment without Max approval.
- Visual login is required, but remains prototype until backend is approved.

## FR — Codex Manager par défaut

Codex sert principalement à review/QA/intégration prudente. Il doit vérifier commandes, branches, ancres, images, responsive, claims, PR conflicts, et recommander merge/no-merge.

## EN — Default Codex Manager

Codex mainly serves review/QA/careful integration. It must verify commands, branches, anchors, images, responsive behavior, claims, PR conflicts, and recommend merge/no-merge.

## FR — Claude Code Manager par défaut

Claude sert principalement à production premium: UX, app mobile/desktop, copy, HTML/CSS/JS, intégration Félix. Le manager lui donne une mission complète et vérifiable.

## EN — Default Claude Code Manager

Claude mainly serves premium production: UX, mobile/desktop app, copy, HTML/CSS/JS, Félix integration. The manager gives it a complete and verifiable mission.
