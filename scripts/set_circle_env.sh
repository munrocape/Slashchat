#!/bin/bash

user=''
project=''

CIRCLE_TOKEN=`cat CIRCLE_TOKEN`
SLACK_TOKEN=`cat TOKEN` 

while getopts ":u:p:ad" opt; do
  case $opt in
	u)
	  user=$OPTARG
	  echo "Using user: $user"
      ;;
	p)
      project=$OPTARG
	  echo "Using project: $project"
      ;;
    a)
      curl -X POST -H "Content-Type: application/json" -d "{'name':'SLACK_TOKEN', 'value':"$SLACK_TOKEN"}" "https://circleci.com/api/v1/project/$user/$project/envvar?circle-token=$CIRCLE_TOKEN"
      ;;
	d)
      curl -X DELETE https://circleci.com/api/v1/project/$user/$project/envvar/SLACK_TOKEN?circle-token=$CIRCLE_TOKEN
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

exit 0
