#!/usr/bin/env bash
echo "Creating base .txt files"
echo "Creating corpus"
python3 read.py
echo "Classifying the comments"
python3 ngram.py
python3 bot.py
echo "Reply to Negative comments"
python3 reply.py
echo "Removing unwanted .txt files"
echo "Thank you - Script made by Akash and Maruthi"

