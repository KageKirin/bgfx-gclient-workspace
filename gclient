#!/bin/bash

echo "wrapping command '$@' to '$GCLIENT_ROOT'"

former_path=$PATH
PATH="$GCLIENT_ROOT":"$PATH"

gclient "$@"

PATH=$former_path
