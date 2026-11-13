# Original practice questions

Choose an answer and explain your reasoning before expanding the explanation. These are original learning checks, not recalled exam questions.

## GHF-001 · basics

You committed a note locally, but your branch on GitHub has not changed. What normally sends the commit to GitHub?

A. git fetch
B. git push
C. git status
D. git add

<details>
<summary>Answer and explanation</summary>

**Correct: B. git push**

- **A:** Fetch downloads remote information.
- **B:** Push sends local commits to the remote.
- **C:** Status reports local state.
- **D:** Add selects content for a commit.

Key idea: Commit is local; push shares commits.

[Official reference](https://git-scm.com/docs/git)

</details>

## GHF-002 · basics

You want to download remote history before deciding how to integrate it. Which command fits?

A. git pull
B. git commit
C. git fetch
D. git init

<details>
<summary>Answer and explanation</summary>

**Correct: C. git fetch**

- **A:** Pull also integrates according to its options.
- **B:** Commit records staged work.
- **C:** Fetch downloads remote history without merging it into your checked-out branch.
- **D:** Init creates a local repository.

Key idea: Fetch lets you inspect before integration.

[Official reference](https://git-scm.com/docs/git-pull)

</details>

## GHF-003 · basics

Which statement correctly distinguishes Git from GitHub?

A. Git tracks versions; GitHub hosts repositories and collaboration tools.
B. Git requires GitHub for every commit.
C. GitHub is the name of the Git staging area.
D. Git and GitHub are interchangeable names.

<details>
<summary>Answer and explanation</summary>

**Correct: A. Git tracks versions; GitHub hosts repositories and collaboration tools.**

- **A:** Git works locally and GitHub adds hosted collaboration.
- **B:** A local commit does not require GitHub.
- **C:** The staging area belongs to Git.
- **D:** They are different tools with connected uses.

Key idea: Local version control can exist without a hosting account.

[Official reference](https://code.visualstudio.com/docs/sourcecontrol/overview)

</details>

## GHF-004 · repositories

A new reader needs setup instructions for this project. Which file is the best starting point?

A. CODEOWNERS
B. LICENSE
C. SECURITY.md
D. README.md

<details>
<summary>Answer and explanation</summary>

**Correct: D. README.md**

- **A:** CODEOWNERS maps paths to owners.
- **B:** LICENSE describes reuse terms.
- **C:** SECURITY describes reporting security concerns.
- **D:** README introduces the project and explains how to use it.

Key idea: README is the project entry point.

[Official reference](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

</details>

## GHF-005 · repositories

Which file identifies people or teams responsible for particular repository paths?

A. CODEOWNERS
B. README.md
C. A local stash
D. A Project view

<details>
<summary>Answer and explanation</summary>

**Correct: A. CODEOWNERS**

- **A:** CODEOWNERS maps file patterns to owners.
- **B:** README describes the project.
- **C:** A stash holds temporary local work.
- **D:** A Project view organizes tracked items.

Key idea: Ownership mapping is separate from review enforcement.

[Official reference](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)

</details>

## GHF-006 · repositories

A repository is public and has no license file. Which conclusion is appropriate?

A. All uses are automatically permitted.
B. Its reuse permissions need to be checked; public visibility is not an open-source license.
C. Starring it gives you a commercial license.
D. Forking removes all copyright restrictions.

<details>
<summary>Answer and explanation</summary>

**Correct: B. Its reuse permissions need to be checked; public visibility is not an open-source license.**

- **A:** Visibility alone does not grant unrestricted reuse.
- **B:** Public access and licensing answer different questions.
- **C:** A star does not grant licensing rights.
- **D:** A fork does not erase the original terms or rights.

Key idea: Visibility is not a license.

[Official reference](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)

</details>

## GHF-007 · collaboration

You want maintainers to review a branch change before integrating it. What should you open?

A. A secret gist
B. A milestone
C. A pull request
D. A star

<details>
<summary>Answer and explanation</summary>

**Correct: C. A pull request**

- **A:** A gist shares a snippet.
- **B:** A milestone groups work.
- **C:** A PR proposes a change for discussion and review.
- **D:** A star saves or signals interest in a repository.

Key idea: A PR is a proposal to integrate a change.

[Official reference](https://docs.github.com/en/get-started/using-github/github-flow)

</details>

## GHF-008 · collaboration

A PR description says Closes #12. Under the normal keyword behavior, when does the referenced issue close?

A. When you stage a file
B. When the PR is merged into the default branch
C. When someone stars the repository
D. When a branch is cloned

<details>
<summary>Answer and explanation</summary>

**Correct: B. When the PR is merged into the default branch**

- **A:** Staging is local Git work.
- **B:** The default-branch merge triggers the closing relationship.
- **C:** Stars do not close linked issues.
- **D:** Cloning does not trigger issue closure.

Key idea: Link the issue and merge to the correct branch.

[Official reference](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)

</details>

## GHF-009 · collaboration

You need a simple static documentation website from repository content. Which feature fits?

A. Git stash
B. A team role
C. GitHub Mobile notifications
D. GitHub Pages

<details>
<summary>Answer and explanation</summary>

**Correct: D. GitHub Pages**

- **A:** Stash stores local work.
- **B:** Roles govern access.
- **C:** Notifications communicate activity.
- **D:** Pages hosts static site content.

Key idea: Pages publishes a static site.

[Official reference](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)

</details>

## GHF-010 · modern

You need a hosted development environment with a terminal to execute tests. Which option fits?

A. A Project board
B. A secret gist
C. GitHub Codespaces
D. A repository star

<details>
<summary>Answer and explanation</summary>

**Correct: C. GitHub Codespaces**

- **A:** A board tracks work.
- **B:** A gist stores snippets.
- **C:** Codespaces supplies a hosted development environment with compute.
- **D:** A star does not supply execution tools.

Key idea: Codespaces can run tools, not just edit text.

[Official reference](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces)

</details>

## GHF-011 · modern

In an Actions workflow, what is a runner?

A. The machine that executes a job
B. The title of a pull request
C. A repository license
D. The person who starred a repository

<details>
<summary>Answer and explanation</summary>

**Correct: A. The machine that executes a job**

- **A:** A runner provides the execution environment for a job.
- **B:** A PR title is metadata.
- **C:** A license describes reuse terms.
- **D:** Starring does not define a runner.

Key idea: The runner executes the job.

[Official reference](https://docs.github.com/en/actions/get-started/understand-github-actions)

</details>

## GHF-012 · modern

Copilot suggests a fix and generated tests. What is the best next step?

A. Merge because AI generated it
B. Delete existing tests
C. Assume the tests ran in chat
D. Review the changes and run appropriate tests

<details>
<summary>Answer and explanation</summary>

**Correct: D. Review the changes and run appropriate tests**

- **A:** Generated code can be incorrect.
- **B:** Existing tests may catch regressions.
- **C:** Generating test text is not proof of execution.
- **D:** Review and execution provide evidence about the proposal.

Key idea: AI suggestions still need verification.

[Official reference](https://docs.github.com/en/copilot)

</details>

## GHF-013 · projects

You want to see the same Project items in columns and in rows. What should you use?

A. Separate repositories for each layout
B. Board and table views of the same Project
C. Two forks
D. Two LICENSE files

<details>
<summary>Answer and explanation</summary>

**Correct: B. Board and table views of the same Project**

- **A:** Repositories are not needed to change a Project layout.
- **B:** Views present the same items in different layouts.
- **C:** Forks copy repositories, not layout settings.
- **D:** License files do not control views.

Key idea: A view changes presentation, not the underlying work.

[Official reference](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)

</details>

## GHF-014 · projects

Your issue closed but its board item stayed In Progress. What should you check first?

A. Whether Git is installed locally
B. The commit author font
C. The Project workflow that updates Status on issue closure
D. The number of stars

<details>
<summary>Answer and explanation</summary>

**Correct: C. The Project workflow that updates Status on issue closure**

- **A:** Local Git installation does not set this Project automation.
- **B:** Font is unrelated.
- **C:** The workflow controls the intended status update.
- **D:** Stars do not drive this workflow.

Key idea: Issue state and Project Status are separate unless connected by automation.

[Official reference](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project)

</details>

## GHF-015 · projects

What is the main purpose of a GitHub Project?

A. Plan and track work using issues, PRs, and fields
B. Replace the Git commit history
C. Store passwords for every member
D. Provide a Python interpreter

<details>
<summary>Answer and explanation</summary>

**Correct: A. Plan and track work using issues, PRs, and fields**

- **A:** Projects organize and visualize work.
- **B:** Git history remains in the repository.
- **C:** Projects are not a password vault.
- **D:** A Project does not provide code execution.

Key idea: Planning tools organize work; they do not replace version control.

[Official reference](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)

</details>

## GHF-016 · security

A contributor needs to organize issues and PRs without pushing code. Which common repository role fits?

A. Admin
B. Write
C. Triage
D. Organization owner

<details>
<summary>Answer and explanation</summary>

**Correct: C. Triage**

- **A:** Admin is broader than the stated task.
- **B:** Write includes code contribution capabilities beyond this need.
- **C:** Triage supports issue and PR management without code write access.
- **D:** Organization ownership is much broader.

Key idea: Match access to the task.

[Official reference](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)

</details>

## GHF-017 · security

What makes an organization team different from a personal repository collaborator?

A. Teams can only contain outside collaborators.
B. Teams group organization members and can receive repository access together.
C. Teams automatically make every repository public.
D. A Project board creates organization membership.

<details>
<summary>Answer and explanation</summary>

**Correct: B. Teams group organization members and can receive repository access together.**

- **A:** Outside collaborators cannot belong to organization teams.
- **B:** Teams provide group-based organization access.
- **C:** A team does not automatically change repository visibility.
- **D:** Project tracking does not create organization membership.

Key idea: Team membership belongs to an organization.

[Official reference](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)

</details>

## GHF-018 · security

Who can read a secret gist if its URL is shared with them?

A. Only the author under all circumstances
B. Only enterprise owners
C. Only users with write access to a separate repository
D. Anyone who obtains the URL

<details>
<summary>Answer and explanation</summary>

**Correct: D. Anyone who obtains the URL**

- **A:** Secret gists are not private.
- **B:** Enterprise ownership is not required.
- **C:** A separate repository role is not the access condition.
- **D:** The URL can expose an unlisted gist to others.

Key idea: Unlisted does not mean access-controlled.

[Official reference](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)

</details>

## GHF-019 · community

You want to contribute to a project where you cannot push branches. Which route fits?

A. Fork, make a branch change, and propose a PR
B. Ask everyone for their password
C. Change the upstream visibility
D. Star the project to receive write access

<details>
<summary>Answer and explanation</summary>

**Correct: A. Fork, make a branch change, and propose a PR**

- **A:** A fork supports proposing a contribution without upstream write access.
- **B:** Sharing passwords is not a contribution workflow.
- **C:** Visibility is not yours to change and does not grant write access.
- **D:** Stars do not grant permissions.

Key idea: A fork lets you prepare a contribution under your own account.

[Official reference](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source)

</details>

## GHF-020 · community

Where can you discover reusable Actions and GitHub apps?

A. Only in a local stash
B. Only in CODEOWNERS
C. GitHub Marketplace
D. Only in a private gist

<details>
<summary>Answer and explanation</summary>

**Correct: C. GitHub Marketplace**

- **A:** A stash holds local changes.
- **B:** CODEOWNERS lists ownership.
- **C:** Marketplace lists Actions and apps.
- **D:** A gist is not the product catalog.

Key idea: Marketplace helps discover integrations.

[Official reference](https://docs.github.com/en/actions/get-started/actions-vs-apps)

</details>

## GHF-021 · community

Before submitting a first contribution, what should you inspect?

A. Only the star count
B. The project contribution guidance and relevant issue context
C. Another contributor’s credentials
D. Only your own profile

<details>
<summary>Answer and explanation</summary>

**Correct: B. The project contribution guidance and relevant issue context**

- **A:** Popularity does not explain contribution expectations.
- **B:** Guidance and issue context help you propose useful work.
- **C:** Credentials are unnecessary and private.
- **D:** Your profile does not explain project requirements.

Key idea: Read the project expectations before proposing a change.

[Official reference](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source)

</details>
