#!/bin/bash
curl -i -X PUT --negotiate -u : https://ybolcldrmstr.yotabites.com:14000/webhdfs/v1/user/ssingh1/test?op=mkdirs
curl -i -X PUT --negotiate -u : https://ybolcldrmstr.yotabites.com:14000/webhdfs/v1/user/ssingh1/test?op=delete
curl -i -X PUT --negotiate -u : https://ybolcldrmstr.yotabites.com:14000/webhdfs/v1/user/ssingh1/test?op=mkdirs
curl -i -X PUT --negotiate -u : https://ybolcldrmstr.yotabites.com:14000/webhdfs/v1/user/ssingh1/test?op=setpermissions&permission=777
curl -i -X PUT --negotiate -u : https://ybolcldrmstr.yotabites.com:14000/webhdfs/v1/user/ssingh1/test/test.txt?op=open

