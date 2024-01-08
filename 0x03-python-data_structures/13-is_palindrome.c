#include "lists.h"
listint_t *reverse_list(listint_t **head);
/**
 *is_palindrome - checks if a singly linked list is a palindrome
 *@head: a pointer to the pointer of the list
 *
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i = 0;
	listint_t *rev_head = NULL;

	if (!head || !*head)
		return (1);
	rev_head = reverse_list(head);

	while (*head && rev_head)
	{
		if ((*head)->n == rev_head->n)
			i = 1;
		else
			i = 0;
		(*head) = (*head)->next;
		rev_head = rev_head->next;
	}
	return (i);
}

/**
 **reverse_list - reverses a list
 *@head: a pointer to the pointer of the list
 *
 *Return: the pointer of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	if (!head || !*head)
		return (NULL);

	listint_t *prev = NULL, *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;

	return (*head);
}
