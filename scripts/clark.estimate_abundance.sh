#!/bin/sh
# new assignment of path to use abundance-script

LDIR="/mnt/prostlocal/programs/clark/1.2.5"

if [ $# -lt 1 ]; then
echo -n "Usage: $0 " 
$LDIR/exe/getAbundance
exit
fi
$LDIR/exe/getAbundance $@
