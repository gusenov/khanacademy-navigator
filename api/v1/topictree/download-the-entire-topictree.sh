#!/bin/bash
set -x # echo on

# https://api-explorer.khanacademy.org

function download {  # Retrieve hierarchical organization of all topics in the library, along with their videos.
    if [ "$1" == "Topic" ]; then
        wget --quiet "https://www.khanacademy.org/api/v1/topictree?kind=Topic" -O "Topics only.json"  # use kind=Topic to get Topics only,
    elif [ "$1" == "Exercise" ]; then
        wget --quiet "https://www.khanacademy.org/api/v1/topictree?kind=Exercise" -O "Topics and Exercises.json"  # or kind=Exercise to get Topics and Exercises.
    else
        wget --quiet "https://www.khanacademy.org/api/v1/topictree" -O "topictree.json"
    fi
}

rm "topictree.json"
download

rm "Topics only.json"
download "Topic"

rm "Topics and Exercises.json"
download "Exercise"
