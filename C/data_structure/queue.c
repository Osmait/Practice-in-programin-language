#include "queue.h"
#include <stdio.h>
#include <stdlib.h>

Node *start = NULL;

Node *createNode() {
  struct Node *node;
  node = (struct Node *)malloc(sizeof(struct Node));
  return node;
}

int enque(int value) {
  struct Node *node;
  node = createNode();
  node->value = value;
  node->next = NULL;
  if (start == NULL) {
    start = node;
  } else {
    struct Node *temp = start;
    start = node;
    node->next = temp;
  }
  return 0;
}

int dequeue() {
  struct Node *temp = start;
  while (temp->next->next != NULL) {
    temp = temp->next;
  }
  struct Node *delete = temp->next;
  temp->next = NULL;
  return delete->value;
}

void viewQueue() {
  struct Node *temp = start;
  while (temp != NULL) {
    printf("%d->", temp->value);
    temp = temp->next;
  }
}

int main(int argc, char *argv[]) {
  enque(1);
  enque(2);
  enque(3);
  dequeue();

  viewQueue();

  return EXIT_SUCCESS;
}
