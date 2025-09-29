# Bridge Integration for Literate-Garden

This directory provides bridge system integration with the meta-project coordination infrastructure.

## Quick Start

### Send a message to another agent
```bash
# Example: Request review from Chat agent
./.bridge/send-message.sh code chat NORMAL \
  "Literate Garden: Review needed" \
  path/to/message.md
```

### Check for incoming messages
```bash
./.bridge/receive-messages.sh
```

## Message Priority Levels
- **CRITICAL**: Blocks other work, immediate attention required
- **HIGH**: Should be addressed in current session
- **NORMAL**: General coordination, handle when convenient
- **LOW**: Informational, no immediate action needed

## Message Format

Create a markdown file with your message content:

```markdown
# Message Title

## Context
Brief background about why you're sending this message.

## Request
What you need from the receiving agent.

## Expected Action
Clear description of what the recipient should do.
```

Then send it:
```bash
./.bridge/send-message.sh code chat HIGH "Title" message.md
```

## Integration Notes

- These scripts are thin wrappers around the meta-project bridge system
- All messages use atomic operations (collision-safe via Bridge v3.0)
- Messages are tracked in meta-project's `bridge/` directory
- See `~/devvyn-meta-project/CLAUDE.md` for full bridge documentation

## Architecture

```
Literate-Garden/
├── .bridge/
│   ├── send-message.sh      → ~/devvyn-meta-project/scripts/bridge-send.sh
│   ├── receive-messages.sh  → ~/devvyn-meta-project/scripts/bridge-receive.sh
│   └── README.md            (this file)
│
└── CLAUDE.md                (coordination instructions)
```

The meta-project provides:
- Collision-safe message queuing
- Agent session tracking
- TLA+ formal verification
- Multi-agent coordination protocols