#!/bin/bash

if [[ -n "${1-}" ]] && [[ -f  "${1-}" ]]; then
	rm -rf $(comm -12 <(ls -a) <(cat .gitignore | sed '/^\s*$/d' | uniq | sort) | grep -v $1)
else
	rm -rf $(comm -12 <(ls -a) <(cat .gitignore | sed '/^\s*$/d' | uniq | sort))
fi
