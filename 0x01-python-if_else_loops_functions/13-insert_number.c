#include "lists.h"
/**
 *insert_node - inserts a number into a sorted singly linked list
 *@head: a pointer to the first node in the list
 *@number: the number to insert
 *
 *Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL, *previous = NULL;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!*head)
		*head = new;
	else
		current = *head;

	while (current)
	{
		if (current->n >= new->n)
		{
			if (previous)
				previous->next = new;
			else
				*head = new;
			new->next = current;
			break;
		}

		if (current->next == NULL)
		{
			current->next = new;
			break;
		}
		previous = current;
		current = current->next;
	}
	return (new);
}
