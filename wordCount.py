#!/bin/bash/python

f=open("out.txt","r")

#print(f.read())

data=f.read()

words=data.split()

print(len(words))
