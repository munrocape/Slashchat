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
This project began as a fork of [llimllib's limbo](https://github.com/llimllib/limbo).

Due to lack of maintenance, this fork was created to carry on and address issues that existed in the original backlog. 

Since then, it has gone on to address a number of other issues.

Furthermore, this fork aims to value PRs on their individual merits - all are welcomed and will be merged provided they pass the CI tests.

The license of this file mirror's the original license. Some background reading can be found in this [informative article](https://gun.io/blog/how-to-github-fork-branch-and-pull-request/).

---
### Backlog & Collaborator Status
An active backlog is maintained on our [Trello board](https://trello.com/slashchat). 

Everyone is encouraged to fork and work on this project. 

If you wish to obtain collaborator status, there are two avenues: 

1. Please contact someone in the Trello group [here](https://trello.com/slashchat/members). 
2. Alternatively, feel free to create an issue with ***Collaborator Status: Request*** in the title.
