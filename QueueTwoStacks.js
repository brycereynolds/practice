'use strict'

class Queue{
    constructor(){
        this.inbox = []
        this.outbox = []
    }
    enqueue(el){
        this.inbox.push(el)
    }
    dequeue(){
        if(this.outbox.length === 0){
            while(this.inbox.length > 0){
                this.outbox.push(this.inbox.pop())
            }
        }
        return this.outbox.pop()
    }
    print(){
        let ol = this.outbox.length
        return ol > 0 ? this.outbox[ol - 1] : this.inbox[0]
    }
}

let q = new Queue()
q.enqueue(42)
q.dequeue()
q.enqueue(45)
q.enqueue(12)
console.log(q.print())