#!/bin/sh

result=`netstat -anp | grep 12001`
result=${result#*LISTEN}
result=${result%%/python*}
echo $result
if [ "$result" != "" ]
then
kill -9 $result
echo The server has been shut down! 
else
echo No server is running!
fi
