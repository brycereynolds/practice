'use strict'

class Node{
    constructor(val){
        this.val = val
        this.left = null
        this.right = null
    }

    insert(val){
        if(val < this.val){
            if(this.left)
                return this.left.insert(val)
            else
                this.left = new Node(val)
        }else{
            if(this.right)
                return this.right.insert(val)
            else
                this.right = new Node(val)
        }
    }

    contains(val){
        if(val === this.val)
            return true

        if(val < this.val){
            if(this.left)
                return this.left.contains(val)
            else
                return false
        }else{
            if(this.right)
                return this.right.contains(val)
            else
                return false
        }
    }

    print(){
        return this.val
    }

    inorder(){
        if(this.left)
            this.left.inorder()

        console.log(this.val)

        if(this.right)
            this.right.inorder()
    }

    preorder(){
        console.log(this.val)

        if(this.left)
            this.left.preorder()

        if(this.right)
            this.right.preorder()
    }

    postorder(){
        if(this.left)
            this.left.postorder()

        if(this.right)
            this.right.postorder()

        console.log(this.val)
    }


}

let a = new Node(10)
a.insert(5)
a.insert(15)
a.insert(8)

a.inorder()
a.preorder()
a.postorder()


boolean checkBST(Node root) {
    
}
