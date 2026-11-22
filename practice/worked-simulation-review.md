# Worked review: keep the conclusion within the evidence

[Case study](simulation-case-study.md) · [Table of contents](../CONTENTS.md)

The following text is fictional practice material, not a claim about the author's work.

## Draft sentence

“The test proves that our network has no redundancy and that I repaired a production outage.”

## Review

The supplied exercise tested one disconnection and restoration in a simulation. It did not test every failure path. It also did not involve a production network. Both claims go beyond the evidence.

A suitable revision is: “In the supplied simulation, disconnecting the tested link interrupted the service. Restoring it restored service in this attempt. Other failure paths were not tested.”

## Review the proposed diagram

If the diagram includes backup links not supplied or observed, either remove them or label them as a proposed design. A proposed topology can be useful, but it must not look like a measured starting state.

If an arrow means sequence, label the diagram as a process. If it means a connection, label the connection. Mixing those meanings can make an otherwise neat drawing misleading.

## Review the GitHub evidence

A useful PR description names the documentation problem, the change, and the checks actually performed. For example, a writer who viewed the rendered note and opened its relative links can report those actions. They cannot claim an automated test passed if none ran.

The review is complete when the claim, drawing, and supplied observations agree, and applicable merge requirements are satisfied. It is not necessary to make the note longer merely to make the change look substantial.
