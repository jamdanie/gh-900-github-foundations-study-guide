# Choose where to share the work

[Table of contents](../CONTENTS.md)

The audience's task should guide the feature choice. A file in a repository, a website, and a downloadable release can describe the same project while serving different needs.

| Reader needs to… | Start with | Why it fits |
| --- | --- | --- |
| Understand the project and find setup steps | README | Gives an entry point beside the source files |
| Read a collection of project documentation | Repository docs or a Wiki | Keeps related explanations together |
| Share a small snippet | Gist | Provides a focused, shareable item |
| Browse a static project website | GitHub Pages | Publishes website content from a repository |
| Download a named version with release notes | Release | Connects a distributable version with a tag and notes |

## A worked choice

You finished a simulated incident exercise. Put the note and diagram in repository documentation so someone can inspect their history and review the PR. Link the exercise from README. A public-facing website could be useful later if you want a different reading experience, but the note does not need a website to be useful.

If a reader needs a particular packaged version, consider a release. Publishing a release does not by itself create a Pages site, and enabling Pages is not the same as creating a release.

## Scope and visibility

GitHub Pages hosts static website content. It is not a general-purpose backend server. Do not assume a repository's access settings alone describe who can reach a published website; check the configured publishing and access behavior before sharing sensitive material.

A secret gist is unlisted, not a private vault. Keep credentials out of every publishing route. For licenses and repository files, see the [foundations reference](foundations-reference.md).

Sources: [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages), [releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases), and the documentation linked from the foundations reference.
