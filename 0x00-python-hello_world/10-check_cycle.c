#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check if list has a loop
 * @list: the list to check
 *
 * Return: 1 if there is a loop | 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *before = list;
	listint_t *after = list;

	while (after != NULL && after->next)
	{
		before = before->next;
		after = after->next->next;

		if (before == after)
		{
			return (1);

		}
	}
	return (0);

}
