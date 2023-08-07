#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - Checks if a singly-linked list contains a specified cycle
 * @list: A singly-linked type list
 *
 * Return: If there is no cycle return 0
 *         If there is a cycle retuurn - 1
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = list->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);

		turtle = turtle->next;
		hare = hare->next->next;
	}
return (0);
}
