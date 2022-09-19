#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: the singly linked list
* Return: 0 if there is no cycle, 1 if there is
*/
int check_cycle(listint_t *list)
{
listint_t *cycle;
unsigned int n;

cycle = list;
n = 0;
while (cycle != NULL)
{
cycle = cycle->next;
n++;
}
if (n <= 1)
return (0);
else
return (1);
}
