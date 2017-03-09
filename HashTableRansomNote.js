'use strict'

let mag = 'wi z ne we ebixk yvrd qrd ojckw q xe e bcco xb ieqym dwuu w dnapw achkt xqdhs nstms zmqu csqxi rim tvic arq fvjqx x su ty zl zmah y tv rkjq hpvpx ujj f i u fl iv n mnrvx tho diz k tidi gr ptkq z tho su diz yvrd dwuu dnapw xb arq xb mnrvx xe bcco qrd y ptkq rim fvjqx bcco q q wi i tidi gr mnrvx hpvpx tv f y mnrvx we fvjqx tv f wi ptkq ujj rim ebixk tho ptkq rkjq yvrd dwuu zl ujj zl qrd e ieqym'
let note = 'dwuu tvic y dnapw ujj tidi nstms x xe achkt x su zmqu iv zmqu xb ojckw we fvjqx tvic tv ne rkjq diz tvic we rkjq nstms zmah ieqym zmah fl xb wi tho x z ty u i gr ptkq q su tho rim tv iv iv yvrd xe qrd y dnapw q zmah arq we ieqym su zl q xb arq rkjq q e xb zl ty fvjqx ptkq ieqym qrd y wi wi nstms diz dnapw zmah q ebixk su e xb q i mnrvx wi x x tidi w ojckw bcco e tv rkjq tho'

let magArr = []
mag.split(' ').forEach((el) => {
    if(magArr[el]){
        magArr[el]++
    }else{
        magArr[el] = 1            
    }
})

let valid = true

for(let key in note.split(' ')){
    console.log("KEY HERE", key, magArr[key])
    if(!magArr[key] || magArr[key] === 0){
        valid = false
        break
    }else{
        magArr[key] = magArr[key] - 1
        console.log("SET A NEW MAG KEY", magArr[key])
    }
}

console.log("magArr", magArr)


console.log("CAN MAKE ", valid)