---
id: "002"
title: "Improve SQLAlchemy Attribute Handling"
stage: "red"
date_iso: "2026-01-29"
surface: "agent"
model: "claude-opus-4-5-20251101"
feature: "none"
branch: "002-ai-chatbot"
user: "HAROON"
command: "manual"
labels: ["sqlalchemy", "debugging", "task-model", "mcp-server", "attribute-handling"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "mcp-server/src/models/task.py"
tests_yaml:
  - "test_improved_sa_handling.py"
---

## PROMPT_TEXT
```
--title "Improve-SQLAlchemy-Attribute-Handling" --stage "red"
```

## RESPONSE_TEXT
Improved the SQLAlchemy attribute handling in the MCP server's Task model to comprehensively handle all _sa_* internal attributes, resolving the recurring _sa_instance_state error.

## OUTCOME_IMPACT
Resolved the recurring 'Task' object has no attribute '_sa_instance_state' error by implementing comprehensive handling of all SQLAlchemy internal attributes that begin with '_sa_', ensuring stable operation of the add_task functionality.

## TESTS_SUMMARY
Created and ran a comprehensive test script to verify the improved fix handles multiple SQLAlchemy internal attributes (_sa_instance_state, _sa_transient, etc.) correctly.

## FILES_SUMMARY
- mcp-server/src/models/task.py: Updated __setattr__ method to handle all _sa_* attributes comprehensively

## NEXT_PROMPTS
- Verify the fix works in the actual application environment
- Test all task-related MCP tools end-to-end

## REFLECTION_NOTE
The initial fix was too narrow, only handling _sa_instance_state specifically. The improved approach handles all SQLAlchemy internal attributes by checking for the _sa_ prefix, making it more robust.

## FAILURE MODES OBSERVED
The original fix only handled _sa_instance_state specifically, but SQLAlchemy may set other internal attributes during ORM operations, causing the same error with different attribute names.

## NEXT EXPERIMENT TO IMPROVE PROMPT QUALITY
Consider creating unit tests for SQLAlchemy models to catch similar issues during development rather than in production.