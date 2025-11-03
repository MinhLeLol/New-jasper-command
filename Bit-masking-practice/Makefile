CC=gcc
CFLAGS=-std=c11 -g -Wall

all: src/main.c
	$(CC) $(CFLAGS) -I./include src/*.c -o ./mysolution -lm


run: all
	./mysolution 255 16

solution: 
	python ../services/generate_solutions.py

clean:
	rm -f mysolution
