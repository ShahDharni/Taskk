let p1=new Promise((resolve,reject)=>{
    console.log("Promise is pending")
    setTimeout(()=>{
        console.log("I am promise and I am fulfiled ")
        resolve(true)
        // reject(new Error('I am an error'))

    },5000)

})


let p2=new Promise((resolve,reject)=>{
    console.log("Promise is pending")
    setTimeout(()=>{
        console.log("I am promise and I am rejected ")
        // resolve(true)
        reject(new Error('I am an error'))

    },5000)

})

// These both promises will execute parallel

// To get the value

p1.then((value)=>{
    console.log(value)
})


// To catch the error

p2.catch((error)=>{
    console.log('some error occured in p2')
})