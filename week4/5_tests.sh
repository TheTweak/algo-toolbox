#!/bin/sh

res=$(cat 5_test_1.txt | python3.9 5_lottery.py)
if [ "$res" != "1 0 0" ]
then
    echo test 1 failed
fi

res=$(cat 5_test_2.txt | python3.9 5_lottery.py)
if [ "$res" != "0 0 1" ]
then
    echo test 2 failed
fi

res=$(cat 5_test_3.txt | python3.9 5_lottery.py)
if [ "$res" != "2 0" ]
then
    echo test 3 failed
fi

res=$(cat 5_test_3.txt | python3.9 5_lottery.py)
if [ "$res" != "2 0" ]
then
    echo test 3 failed
fi
