---
description: End-of-session wrap-up — review changes, log the session, run the project's checks, then commit & push
---

You are wrapping up a work session on this project. Adapt every step to the conventions
this project actually uses (check its `README` / `CLAUDE.md` / `AGENTS.md` first); skip any
step that doesn't apply, and don't invent process the project doesn't have. Do these in order:

1. **Review what changed.** Skim `git log` since the session started and the current diff so
   your summary is accurate — do not invent work.

2. **Log the session.** If the project keeps a session log / changelog / journal, append a
   dated entry: what was done, key decisions (one line each + why), what changed
   (files / versions), and numbered next steps to start from next time. If there's no such log
   and one would clearly help, ask before creating it.

3. **Update the project's records.** Bring any research / findings / decision log the project
   keeps up to date for this session's work (use the project's self-eval or summary format if
   it has one).

4. **Run the project's definition-of-done.** If the project defines a checklist, tests, linters,
   or a build, run them and record the result. Grade honestly — a real failure surfaced beats a
   false pass. If two or more checks fail, the session isn't done: fix them or hand off with the
   blocker named.

5. **Sanity-check the work.** Confirm the deliverables are internally consistent — counts/totals,
   cross-references, and version numbers/headers matching the actual content.

6. **Commit & push.** Stage the work, commit with a clear message in the project's style, and push
   to the working branch (retry with backoff on network errors). If the project's workflow
   fast-forwards a main/release branch, do so **only on a clean fast-forward**. Do **not** open a
   pull request unless explicitly asked.

7. **Report back:** a short summary of what changed and the top 2–3 "start here next session" items.
