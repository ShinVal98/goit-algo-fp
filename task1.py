# Описую вузол однозв'язного списку
class Node:
    def __init__(self, data):
        self.data = data      # Зберігаю значення
        self.next = None      # Зберігаю посилання на наступний вузол

    def __repr__(self):
        return f"Node({self.data})"

# Реверсую список, змінюючи посилання між вузлами
def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev  # нова голова

# Вставляю вузол у відсортований підсписок
def _sorted_insert(sorted_head, node):
    if not sorted_head or node.data < sorted_head.data:
        node.next = sorted_head
        return node
    current = sorted_head
    while current.next and current.next.data < node.data:
        current = current.next
    node.next = current.next
    current.next = node
    return sorted_head

# Сортую список сортуванням вставками
def insertion_sort_list(head):
    sorted_head = None
    current = head
    while current:
        nxt = current.next
        current.next = None
        sorted_head = _sorted_insert(sorted_head, current)
        current = nxt
    return sorted_head

# Зливаю два відсортовані списки у один
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next

# Створюю допоміжну функцію для друку всього списку
def print_list(head):
    vals = []
    while head:
        vals.append(str(head.data))
        head = head.next
    print(" -> ".join(vals))

if __name__ == "__main__":
    # демонстраційний приклад
    data1 = [7, 2, 5, 3]
    head1 = None
    for x in reversed(data1):
        node = Node(x)
        node.next = head1
        head1 = node
    print("Оригінал:")
    print_list(head1)

    print("\nРеверс:")
    head1 = reverse_list(head1)
    print_list(head1)

    print("\nСортування вставками:")
    sorted_head = insertion_sort_list(head1)
    print_list(sorted_head)

    # демонстрація merge
    data2 = [1,4,6]
    head2 = None
    for x in reversed(data2):
        n = Node(x); n.next=head2; head2=n
    merged = merge_sorted_lists(sorted_head, head2)
    print("\nЗлиття з [1,4,6]:")
    print_list(merged)

