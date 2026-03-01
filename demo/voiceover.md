# Indagine Demo Voiceover (ElevenLabs TTS)

## Settings
- **Voice:** Pick a calm, confident male or female voice (e.g. "Adam", "Rachel", or "Antoni")
- **Stability:** 0.50
- **Clarity + Similarity Enhancement:** 0.75
- **Style:** 0 (neutral — no dramatic flair)
- **Speed:** Slightly slow

## Script

Indagine. An automated AI mechanic that debugs and fixes your AI agents when they fail.

Right now, an AI travel agent is failing to book flights in production. Users are getting generic errors, and developers are digging through logs to find out why. Indagine catches this failure and diagnoses it instantly.

Here's how it works.

When a failure occurs, Indagine captures the full trace. It deploys an analysis swarm: a Trace Analyzer pinpoints the exact point of failure, while a Tool Analyzer checks for schema mismatches. 

They converge on a Diagnosis Engine that identifies the root cause. Then, a Fix Generator writes the exact code diff needed to solve the problem. All of this happens autonomously.

Let me show you. I'm running the debugger now.

The travel agent failed because of a schema validation error. The user asked for February fifteenth, but the API requires a specific date format. 

You can see the agents running in parallel. The Tool Analyzer flags the mismatch. The Diagnosis Engine confirms the root cause with ninety percent confidence.

Here's the result. Indagine didn't just find the error—it wrote the fix. 

It generated a patch to normalize the date strings before calling the flight search tool. What would have taken a developer an hour of debugging is solved in seconds.

From trace to fix. Fully automated root cause analysis and code generation for your multi-agent systems.

Built for the Microsoft AI Dev Days Hackathon twenty twenty-six. Thank you for watching.
