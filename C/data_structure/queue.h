#ifndef __QUEUE__

#define __QUEUE__

typedef struct Node {
  int value;
  struct Node *next;
} Node;

Node *createNode();
int enque(int value);
int dequeue();
void viewQueue();
#endif
