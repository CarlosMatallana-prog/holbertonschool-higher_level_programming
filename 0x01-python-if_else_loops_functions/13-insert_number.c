#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function that inserts a number into a sorted SLL.
 * @number: integer
 * @head: head of the sll
 * Return:the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t head, int number)
{
	listint_t *new_node, *current;

	current = head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == 0)
	{
		return (0);

	}
	new_node->n = number;
	if (head == 0 || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);

	}

	while (current->next && current->next->n <= number)
		current = current->next;


	new_node->next = current->next;
	current->next = new_node;
	return (new_node);

}
