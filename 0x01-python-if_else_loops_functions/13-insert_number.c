<<<<<<< HEAD
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts the node itself
 * @head: the head
 * @number: int to be add
 * Return: the new new node
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *temp = NULL, *node = NULL;

    if (head == NULL)
        return (NULL);

    node = malloc(sizeof(listint_t *));
    if (node == NULL)
        return (NULL);
    node->next = NULL;
    node->n = number;

    temp = *head;
    while (temp)
    {
        if (temp->n >= number)
        {
            node->next = temp;
            *head = node;
            return (node);
        }
        else if (temp->n <= number && temp->next->n >= number)
        {
            if (temp->next != NULL)
            {
                node->next = temp->next;
                temp->next = node;
                return (node);
            }
        }
        temp = temp->next;
    }

    return (NULL);
=======
#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - inserts a number in an ordered linked list
 * @head: double pointer to the linked list
 * @number: number to insert in the new node
 *
 * Return: address of the new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n < number)
		{
			temp = current;
			current = current->next;
		}
		temp->next = new;
		new->next = current;
	}

	return (new);
>>>>>>> 4be34b605cf78051a0ad53da8bac983fdc9b78d8
}
