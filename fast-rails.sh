#!/bin/bash

while true; do
  case "$1" in
    -sys | --sysuser ) USER_NAME=$2; shift 2;;
    -rb | --rbversion ) RB_VERSION=$2; shift 2;;
    * ) break ;;
  esac
done

# main

sudo useradd -r $(USER_NAME)
sudo apt-get update && sudo apt-get upgrade

. nodejs.sh
. postgres.sh
. rails.sh
. nginx.sh


