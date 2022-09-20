#include "lists.h"

/**
* insert_nodeint_at_index - inserts a ne wnode at a given position
* @head: first node
* @idx: index where new node should be added
* @n: new element
* Return: address of the new node
*/
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
listint_t *hold = *head;
listint_t *new;
unsigned int i;

new = malloc(sizeof(listint_t));
if (!new || head)
return (NULL);

new->n = n;
new->next = NULL;

if (idx == 0)
{
new->next = *head;
*head = new;
return (new);
}
for (i = 0; hold && i < idx; i++)
{
if (i == idx - 1)
{
new->next = hold->next;
hold->next = new;
return (new);
}
else
hold = hold->next;
}
return (NULL);
}
