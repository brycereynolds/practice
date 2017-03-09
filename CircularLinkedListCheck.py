def is_circular(head):

     slow = head
     fast = head

     while fast != None:
         slow = slow.next

         if fast.next != None:
              fast = fast.next.next
         else:
              return False

         if slow is fast:
              return True

    return False
