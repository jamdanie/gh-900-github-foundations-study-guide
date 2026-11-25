# Visual and game-based learning resources

[Table of contents](../CONTENTS.md)

Reviewed November 19, 2026. Start with the free Git resources for GH-900. The Steam games below are optional ways to explore infrastructure; buying them is not necessary for this guide.

## Pick a resource by the task

| Resource | Access | What to use it for | What to do afterward |
| --- | --- | --- | --- |
| [Learn Git Branching](https://learngitbranching.js.org/) | Free browser simulator; JavaScript required | See commits, branches, and merges change a graph | Explain the graph, then repeat a small task in a disposable local repository |
| [Oh My Git!](https://ohmygit.org/) | Free downloadable open-source game | Use command cards and a live repository visualization | Describe which command changed history and which changed your position |
| [Introduction to GitHub](https://github.com/skills/introduction-to-github) | Official interactive course; GitHub account needed | Work through GitHub's introductory repository workflow | Explain your branch, commit, and PR |
| [Communicate using Markdown](https://github.com/skills/communicate-using-markdown) | Official interactive course; GitHub account needed | Practice writing structured project communication | Compare the Markdown source with its rendered preview |

GitHub Skills now directs visitors to [GitHub Learn](https://learn.github.com/). The direct course links above make the starting point easier to find. Check account and Actions usage settings before running repository-based exercises; these are real repositories, not isolated browser simulations.

Oh My Git! provides a card interface, an integrated terminal, and visual feedback. Its [download page](https://blinry.itch.io/oh-my-git) lists Windows, macOS, and Linux builds. If an older build does not work on your system, use the browser option instead.

## The Steam data-center games

These are two different products. We have reviewed their publisher descriptions, not independently tested their training accuracy.

| Title | Publisher description | Fit for this guide |
| --- | --- | --- |
| [Data Center, by Waseku](https://store.steampowered.com/app/4170200/Data_Center/) | Build racks, connect servers and switches, observe colored packet flow, and manage capacity and failures | A visual source of problems you can document and track in GitHub |
| [Data Center Simulator, by Nicolas Ray](https://store.steampowered.com/app/4535710/Data_Center_Simulator/) | Technician tasks involving diagnostics, cabling, hardware, and facility operations | An optional source of simulated maintenance scenarios for issues and review notes |

Both full games are paid. The Data Center Simulator listing offered a demo when reviewed. Check the current store listing, system requirements, and regional price before deciding; no purchase is required here.

The Data Center listing emphasizes visual building without complex command lines. Do not treat it as a Linux shell lab. Neither listing establishes GH-900 exam coverage. Game results are simulated results, not workplace experience or proof that a real facility procedure is safe.

## Turn a game session into GitHub practice

Choose one observed problem, describe the expected and actual result in an issue in your own sandbox, and propose an explanation or diagram in a branch. Review and merge that documentation through a PR. The GitHub workflow is the relevant practice; the game's score is not an exam score.

Use the [observation-to-PR lab](../labs/13-observation-to-pull-request.md) even if you do not own a game. It includes a free Git-based alternative.

Sources: the linked resource maintainers and Steam publisher listings; [GitHub's learning resource directory](https://docs.github.com/en/get-started/start-your-journey/git-and-github-learning-resources).

## Use the resource in a complete session

The [learning routes](../practice/choose-your-learning-route.md) connect each resource type to a task and a finish condition. After a session, use the [troubleshooting challenges](../practice/troubleshooting-challenges.md) to check whether you can explain an unfamiliar outcome. Resource availability and game features remain subject to the linked publishers' current information; a completed level is not a verified certification result.

## No game available? Use the supplied case

The [simulation case study](../practice/simulation-case-study.md) includes fictional observations you can analyze without installing anything. Its topology and result are exercise material, not verified behavior of either Steam title above. Use it to practice a diagram, issue, branch, and PR. If you later use a game, replace the supplied observations only with what you actually saw.

## Give the session a specific goal

Use [the controlled observation challenge](../practice/hands-on-challenges/04-game-experiment.md) to plan one change and compare its result. It includes fictional trials for readers without a game. Then use [the visual evidence challenge](../practice/hands-on-challenges/07-readable-evidence.md) to write a caption that explains what the image proves and what it doesn't.

For GitHub practice after playing, [the board-card challenge](../practice/hands-on-challenges/05-project-acceptance.md) turns the note into a task with concrete finish conditions. The [worked diff review](../practice/hands-on-challenges/03-review-the-diff.md) shows how to challenge an unsupported conclusion respectfully.
