#!/bin/bash
#
# Script to update data
#
# optional input argument to specify data dir, else in local dir

DATA_DIR=./data

if [ $# -eq 1 ]; then
  DATA_DIR=$1
fi

# declare the download URLs
SRC_URL=https://datasets.imdbws.com/
declare -a DOWNLOAD_FILES=("title.akas.tsv.gz" "title.basics.tsv.gz" "title.crew.tsv.gz" \
    "title.episode.tsv.gz" "title.principals.tsv.gz" "title.ratings.tsv.gz" \
    "name.basics.tsv.gz")

# iter over the array downloading
for FILE in "${DOWNLOAD_FILES[@]}"; do
  if [ ! -f $DATA_DIR/${FILE%.*} ]; then
    # wget each file and decompress
    $(wget -q $SRC_URL$FILE -P $DATA_DIR)
    $(gzip -d $DATA_DIR/$FILE)
  fi
done