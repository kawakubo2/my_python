const COLLECTION_SIZE = 1_000_000;
const RANDOM_MAX = COLLECTION_SIZE * 1000;
const LOOP_COUNT = 10000;

let array = [];
let set = new Set();

while(set.size() < COLLECTION_SIZE) {
    let r = Math.floor(Math.random() * RANDOM_MAX);
    if (!set.has(r)) {
        array.push(r);
        set.add(r);
    }
}
console.log('set size=' + set.size());
console.log('array size=' + array.size());