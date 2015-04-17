#!/bin/bash
# Must be called from Slashchat root

if [[ "$SLACK_TOKEN" == '' ]]; then
	echo "SLACK_TOKEN was not set"
	if [ $(ls | grep -x TOKEN | wc -w) -lt 1 ]; then
		echo "TOKEN file not found"
		config_vars=$(heroku config --app desolate-fortress-3689 | tail -1)
		while read line
		do
			if [ $(echo $line | cut -d : -f 1 | tr -d '[[:space:]]') == 'SLACK_TOKEN' ]; then
				echo $(echo $line | cut -d : -f 2 | tr -d '[[:space:]]') | tee TOKEN
				break
			fi
		done <<< $config_vars
	else
		echo "TOKEN file found"
	fi
fi
