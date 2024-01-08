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
	listint_t *rev_head = NULL;

	if (!head || !*head)
		return (1);
	rev_head = reverse_list(head);

	while (*head && rev_head)
	{
		if ((*head)->n != rev_head->n)
			return (0);
		(*head) = (*head)->next;
		rev_head = rev_head->next;
	}
	return (1);
}

/**
 **reverse_list - reverses a list
 *@head: a pointer to the pointer of the list
 *
 *Return: the pointer of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
        listint_t *next = NULL;
	listint_t *current = *head;

	if (!head || !*head)
		return (NULL);

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	current = prev;

	return (current);
}
