# Slashchat
### A [Slack](https://slack.com/) chatbot

Build status from pre-fork: [![Build Status](https://travis-ci.org/llimllib/limbo.svg?branch=master)](https://travis-ci.org/llimllib/limbo)

Build status for this fork: [![Build Status](https://travis-ci.org/g2graman/Slashchat.svg?branch=master)](https://travis-ci.org/g2graman/Slashchat) [![Circle CI](https://circleci.com/gh/g2graman/Slashchat/tree/master.svg?style=svg)](https://circleci.com/gh/g2graman/Slashchat/tree/master)

## Installation

1. Clone the repo
2. [Create a bot user](https://my.slack.com/services/new/bot) if you don't have one yet, and copy the API Token
3. Use `echo "API_TOKEN_TO_ACCESS_SLACK" | tee TOKEN`, replacing `API_TOKEN_TO_ACCESS_SLACK` with your token (don't worry, I've added `TOKEN` to `.gitignore` so you won't accidentally commit your token to github)
4. `make run`
5. Invite Limbo into any channels you want it in, or just message it in #general. Try typing `!gif dubstep cat` to test it out

![kitten mittens](http://i.imgur.com/xhmD6QO.png)

## Commands

It's super easy to add your own commands! Just create a python file in the plugins directory with an `on_message` function that returns a string.

You can use the `!help` command to print out all available commands and a brief help message about them. `!help <plugin>` will return just the help for a particular plugin.

These are the current default plugins:

TODO: list and links of links to wikis of current plugins

---

## Contributors

* [@fsalum](https://github.com/fsalum)
* [@rodvodka](https://github.com/rodvodka)
* [@mattfora](https://github.com/mattfora)
* [@dguido](https://github.com/dguido)
* [@JoeGermuska](https://github.com/JoeGermuska)
* [@MathyV](https://github.com/MathyV)
* [@stopspazzing](https://github.com/stopspazzing)
* [@noise](https://github.com/noise)
* [@g2graman](https://github.com/g2graman) 

---
##Miscellaneous
### Reason for fork
You might have noticed that this repository is actually a fork of [llimllib's limbo](https://github.com/llimllib/limbo). This is due to a refusal of accepting pull-requests in the pre-fork which were previously cited as issues but, for whatever reason, were not being accepted, with commits after the fact of the pull-request's submission mimicing commits in pull-requests proper. So instead of waiting around to submit a pull-request that would likely get ignored and have future commits mirroring those pull-requests, this fork was created. Due to the license in the pre-fork, and after reading this very [informative article](https://gun.io/blog/how-to-github-fork-branch-and-pull-request/) it was determined that this fork would remain unmerged from its pre-fork and would accept all reasonable/issue-satisfying pull-requests, pending approval of an admin of this repository after the build is tested against its CI services.

---
### Backlog & Collaborator Status
So as to not have to commit minor adjustments to this `README.md`, backlog tracking can be found at our [Trello](https://trello.com/slashchat). If you should show interest in becoming a collaborator, in addition to potentially being granted collaborator status on this repository (even without which you can still create a fork of this repository and innovate as your heart should desire, as long as you abide by the software's licenses, re: `limbo.LICENSE` and `Slashchat.LICENSE` [**note** that this repository is a fork of limbo so `limbo.LICENSE` is the parent license to `Slashchat.LICENSE`]), you would also potentially be granted membership status in the organization to which the backlog boards belong on Trello. If this option should interest you, get in touch with an admin of this repository from the by finding one from the publicly-visible list on Trello [here](https://trello.com/slashchat/members), or submit an issue on this repository with ***Collaborator Status: Request*** somewhere in the title.
