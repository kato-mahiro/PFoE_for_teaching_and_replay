#!/bin/sh
python ../scripts/Agent > result
diff result ref
echo $?
