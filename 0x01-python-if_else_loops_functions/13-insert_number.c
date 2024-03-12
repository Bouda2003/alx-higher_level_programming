#include "lists.h"

/**
 * insert_node - inserts a node in a location
 * @head: the head of the list
 * @number: the value number
 *
 * Description: it insertss nodes
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *bign = *head;

	if (head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t));
	node->n = number;
	if (*head == NULL || bign->n > number)
	{
		node->next = bign;
		*head = node;
		return (node);
	}
	while (bign != NULL)
	{
		if (bign->next == NULL || number < bign->next->n)
		{
			node->next = bign->next;
			bign->next = node;
			return (node);
		}
		bign = bign->next;
	}
	return (NULL);
}
