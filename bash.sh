echo "Harry's led WILL blink" #alot easier for trouble shooting.

for i in {1..20}
do

	/usr/bin/gpio -1 toggle 38 #gpio pins setup
	sleep 1 #long sleep so you could actually see it
done
