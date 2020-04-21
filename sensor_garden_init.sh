#!/bin/sh
DIR="/home/pi/sensor_garden/tom_project_2020"
DAEMON="$DIR/main.py"
DAEMON_NAME=sensor_garden

DAEMON_OPTS="" #CMD line options for the daemon

DAEMON_USER=pi #CHANGE THIS AFTER TESTING

PIDFILE=/var/run/$DAEMON_NAME.pid
echo $PIDFILE

. /lib/lsb/init-functions 

do_start() {
	. /home/pi/sensor_garden/sensor_garden_venv/bin/activate
	start-stop-daemon --start --background --pidfile "$PIDFILE"  --user "$DAEMON_USER" --chuid "$DAEMON_USER" --startas "$DAEMON"
}

do_stop() {
    log_daemon_msg  "Stopping service $DAEMON_NAME"
}

echo $1
case "$1" in 

    start)
	echo "Starting"
        do_start
        ;;
	stop)
		echo "Stopping"
		do_stop	
		;;
    restart|reload|force-reload) 
        do_stop
        do_start
        ;;

    status)
        status_of_proc "$DAEMON_NAME" "$DAEMON" && exit 0 || exit $?
	;;

    *)
        echo "Used for /etc/init.d/$DAEMON_NAME cmds: {start|stop|restart|status}"
        exit 1
        ;; 

esac 
exit 0
