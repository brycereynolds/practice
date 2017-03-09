'use strict'

class Queue{
    constructor(){
        this.queue = []
    }
    enqueue(el){
        this.queue.push(el)
    }
    dequeue(){
        return this.queue.shift()
    }
    print(){
        return this.queue[0];
    }
}

let q = new Queue()
q.enqueue(42)
q.dequeue()
q.enqueue(45)
q.enqueue(12)
console.log(q.print())