#include "lists.h"

/**
 * insert_node - inserts a new node into a sorted linked list
 * @head: pointer to the head node of the linked list
 * @number: the value to be added to the new node
 *
 * Return: pointer to the new node on success, NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *ptr1, *ptr2;

	ptr = malloc(sizeof(listint_t));
	if (ptr == NULL)
	{
		return (NULL);
	}

	ptr->n = number;
	ptr1 = *head;

	while (ptr1)
	{
		if (ptr->n < ptr1->n)
		{
			break;
		}
		else if (ptr->n < ptr1->next->n)
		{
			break;
		}
		else
		{
			ptr1 = ptr1->next;
		}
	}

	ptr2 = ptr1;
	ptr1 = ptr1->next;
	ptr2->next = ptr;
	ptr->next = ptr1;

	return (ptr);
}
