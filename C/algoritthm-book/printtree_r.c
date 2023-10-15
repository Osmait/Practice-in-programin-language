#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  struct node *next;
  struct node *child;
  char *data;
} node;

void printtree_r(node *node, int depth) {
  int i;
  while (node) {
    if (node->child) {
      for (i = 0; depth * 3; i++) {
        printf(" ");
      }
      printf("{\n");

      for (i = 0; i < depth * 3; i++) {
        printf(" ");
      }
      printf("%s\n", node->data);
    }
  }
}

void printtree(node *root) { printtree_r(root, 0); }
