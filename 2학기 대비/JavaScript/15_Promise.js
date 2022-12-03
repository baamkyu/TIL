const pr = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('OK')
  }, 1000)
})

pr.then((result) => {
  console.log(result)
}).catch((err) => {
  console.log(err)
}). finally(() => {
  console.log('끝')
});