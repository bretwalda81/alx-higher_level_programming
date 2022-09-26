#include "lists.h"

/**
 * is_palindrome - palindrome singly linked list
 * @head: first node
 * Return: 0 if it is not a palindrome or 1 if it is
 */
int is_palindrome(listint_t **head)
{
  if (head == NULL || *head == NULL)
    return (1);
  return (palindrome_check(head, *head));
}

/**
 * palindrome_check - function to check palindrome
 * @head: first node
 * @end: end node
 */
int palindrome_check(listint_t **head, listint_t *end)
{
  if (end == NULL)
    return (1);
  if (palindrome_check(head, end->next) && (*head)->n == end->n)
    {
      *head = (*head)->next;
      return (1);
    }
  return (0);
}
