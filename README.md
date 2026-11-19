# CNIT-381 — Weekly Labs 
Weekly labs for CNIT 381. 
## Week 1 
Created the repository, configured Git, cloned it locally, and made my first commit. 
## Week 2
Practiced team Git collaboration using VS Code and Git commands: feature
branches, commits, pushes, pull requests, code review, squash merging,
and resolving a merge conflict while building the UW-Stout CNIT
Cybersecurity Technology Hub.
## Week 3
Containerized a duplicate-IP checker with Docker and published the image to Docker Hub.
## Week 4 
Built a network config pipeline: an intent file plus a generator, containerized, 
with CI/CD that regenerates and validates the configs on every change. 
## Week 6: IP Plan Check Pipeline 
**What I built:** A Python checker for our IP address plan, packaged in 
Docker, run by GitHub Actions on every push, that opens a GitHub issue 
through the API when the plan has errors. 
**Repo:** https://github.com/stephen-redbird/ip-plan-check 
## Week 11: RESTCONF on a 3650 Switch 
What I did: enabled RESTCONF on the switch, then read and changed its config 
with Postman and a Python script. What I learned: Just how easy it is to remotely configure cisco switches when you have the right tools and knowhow.  IDK how ill want to go back to configuring switches by hand after this.
## Week 11 — AI Network Agent Web App 
**What I built:** I built a webapp that works with claude AI to translate commands
given in plain english into actions conducted on my cisco hardware without a need for knowing 
the exact verbage used.  The webapp also keeps a live picture of the network showing the status
of the network in real time.
**What I learned:** I learned how to leverage AI to manage a network.  By utilizing
an AI agent I can more easily manage a network.
