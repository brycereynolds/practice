a = {
    'value': 10
}

console.log("A", a.value)

b = a

console.log("B", b.value)

b.value = 20

console.log("A", a.value)
console.log("B", b.value)