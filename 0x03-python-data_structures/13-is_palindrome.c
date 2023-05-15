#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 *
 * Return: 1 if list is palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *next = NULL, *tmp = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	tmp = slow;
	while (tmp)
	{
		next = tmp->next;
		tmp->next = prev;
		prev = tmp;
		tmp = next;
	}

	tmp = prev;
	while (tmp)
	{
		if ((*head)->n != tmp->n)
		{
			return (0);
		}
		*head = (*head)->next;
		tmp = tmp->next;
	}

	return (1);
}
