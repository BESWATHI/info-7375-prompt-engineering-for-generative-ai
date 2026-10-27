# Job-Search Agent 1 — The Contract and the Watch

## Known limits

- **Action-surface comparison, agent surface: the text it judged can't be shown.**
  The agent run (`runs/action_surface/agent_2026-10-26T22-54-37-0400.json`,
  commit `4d9a39a`) records each tool call's input but not the WebFetch
  output, so the text the agent actually judged was not saved and can't be
  shown. Its quote does appear word for word in the 12:40 ET Oct 26 saved
  description, and its reply passed the validator, but that does not show
  what WebFetch returned. Claude Code also reported a second model,
  `claude-haiku-5-5`, alongside the pinned `claude-opus-5-5` for that run.
  The runner was deliberately not changed after the run.
