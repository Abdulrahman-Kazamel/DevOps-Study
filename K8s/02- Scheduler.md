
## What Does Scheduler Do?

The Scheduler:

- Watches for Pods without nodes (which in pending state)
- Chooses best Worker Node

Based on:

- CPU
- Memory
- Taints/Tolerations
- Affinity rules
- Policies

---

## Scheduling Phases

### 1. Filtering

Remove unsuitable nodes.

Example:

- Node lacks CPU

---

### 2. Scoring

Rank remaining nodes.

Example:

- Node A score = 80
- Node B score = 95

---

### 3. Binding

Assign Pod to selected node.