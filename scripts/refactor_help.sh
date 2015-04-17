for f in $(ls -R . | grep ":$" | tr -d ":" | tail | find `pwd` | grep .py$); do
	echo $(cat $f | grep Slash)
done
