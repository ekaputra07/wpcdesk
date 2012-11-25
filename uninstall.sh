#!/bin/bash

echo "Deleting all installed files..."
cat $HOME/.wpcdesk.install.log | xargs rm -rf

echo "Deleting installer log file..."
rm $HOME/.wpcdesk.install.log

echo "WpcDesk successfuly removed from system..."
