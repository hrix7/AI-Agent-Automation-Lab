# AI Agent Automation Lab

Small, auditable automation projects exploring MCP, Git workflows, n8n, coding agents, experiment organization, and human-in-the-loop controls.

## Design principles

- Least privilege
- Dry-run by default
- Explicit approval for higher-risk actions
- Deterministic logs and reproducible inputs
- Human review for code, data, and external side effects
- No secrets in source control

## Included project

`src/experiment_scaffold.py` generates a consistent research experiment directory with a manifest, notes, inputs, outputs, and logs. It refuses to overwrite an existing directory.

```bash
python src/experiment_scaffold.py demo-experiment --dry-run
python src/experiment_scaffold.py demo-experiment
```

## Roadmap

- Biomedical literature assistant
- Dataset inventory and integrity checker
- GitHub research-project assistant
- n8n experiment-notification workflow

## License

MIT.
