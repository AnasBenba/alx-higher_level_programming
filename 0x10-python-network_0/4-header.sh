#!/bin/bash
# displays the body of the response and send a header variable
curl -sX GET "$1" -H "X-School-User-Id: 98"
