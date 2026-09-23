# AI Agent and Automation Lab

I created this repository to turn my AI-accelerator training into small, testable engineering workflows. My focus is not only on getting an agent to produce an answer, but on making each action traceable, reviewable, and safe before it changes files or code.

## Training and work represented here

- Practiced structured prompting and explicit acceptance criteria.
- Used coding agents with human verification of proposed changes.
- Studied Model Context Protocol (MCP) tool architecture and permission boundaries.
- Reviewed automated Git operations, repository state, commits, and audit trails.
- Built n8n and file-automation concepts around triggers, actions, validation, and error handling.
- Applied human approval to higher-risk actions.
- Designed reusable research-workflow utilities instead of publishing only training notes.

## Repository code

- `src/experiment_scaffold.py` safely creates a standard research-experiment folder structure and refuses to overwrite an existing folder.
- `src/file_manifest.py` inventories files with sizes and SHA-256 hashes for verification and reproducibility.
- `docs/SAFETY.md` records the approval and verification rules I follow.
- `examples/README.md` lists safe example workflows.

## Run the utilities

```bash
python src/experiment_scaffold.py cxr_experiment --dry-run
python src/experiment_scaffold.py cxr_experiment
python src/file_manifest.py cxr_experiment --output manifest.json
```

## Features

- Dry-run support.
- Refusal to overwrite existing work.
- UTC time-stamped manifests.
- File-integrity hashes.
- Clear separation of inputs, outputs, logs, and notes.
- Human-readable JSON for audit and review.

## Next builds

I plan to extend this repository with a biomedical literature organizer, medical-dataset folder validator, and GitHub research-project assistant.

## Author

Hritika Adhikary.

## Rights

Copyright (c) 2026 Hritika Adhikary. All rights reserved. See [LICENSE](LICENSE).
