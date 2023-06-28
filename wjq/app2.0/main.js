const searchForm = document.getElementById('search-form')
const resultsDiv = document.getElementById('results')
const saveButton = document.getElementById('save-button')
const downloadLink = document.getElementById('download-link')

searchForm.addEventListener('submit', event => {
  event.preventDefault()
  const query = document.getElementById('query').value
  const directoryPath = document.getElementById('directory_path').value
  fetch('/search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({query, directory_path: directoryPath})
  })
    .then(response => response.json())
    .then(results => {
      resultsDiv.innerHTML = ''
      results.forEach(result => {
        const filePath = result.file_path.replace(/\\/g, '\\\\')
        const fileLink = `<a href="#" onclick="showFile('${filePath}', ${result.line_number})">${result.file_path}</a>`
        const lineLink = `<a href="#" onclick="showFile('${filePath}', ${result.line_number})">${result.line_number}</a>`
        const resultHTML = `
          <div>
            <h3>${fileLink}</h3>
            <p>${lineLink} ${result.line_text}</p>
          </div>
        `
        resultsDiv.innerHTML += resultHTML
      })
    })
})

function showFile(filePath, lineNumber) {
  const url = `/file?file_path=${filePath}&line_number=${lineNumber}`
  window.open(url, '_blank')
}

saveButton.addEventListener('click', event => {
  const results = resultsDiv.innerHTML
  const blob = new Blob([results], {type: 'text/plain'})
  const url = URL.createObjectURL(blob)
 以下是完整的 JavaScript 代码，它将结果保存到文件并提供下载链接。

```javascript
const searchForm = document.getElementById('search-form')
const resultsDiv = document.getElementById('results')
const saveButton = document.getElementById('save-button')
const downloadLink = document.getElementById('download-link')

searchForm.addEventListener('submit', event => {
  event.preventDefault()
  const query = document.getElementById('query').value
  const directoryPath = document.getElementById('directory_path').value
  fetch('/search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({query, directory_path: directoryPath})
  })
    .then(response => response.json())
    .then(results => {
      resultsDiv.innerHTML = ''
      results.forEach(result => {
        const filePath = result.file_path.replace(/\\/g, '\\\\')
        const fileLink = `<a href="#" onclick="showFile('${filePath}', ${result.line_number})">${result.file_path}</a>`
        const lineLink = `<a href="#" onclick="showFile('${filePath}', ${result.line_number})">${result.line_number}</a>`
        const resultHTML = `
          <div>
            <h3>${fileLink}</h3>
            <p>${lineLink} ${result.line_text}</p>
          </div>
        `
        resultsDiv.innerHTML += resultHTML
      })
    })
})

function showFile(filePath, lineNumber) {
  const url = `/file?file_path=${filePath}&line_number=${lineNumber}`
  window.open(url, '_blank')
}

saveButton.addEventListener('click', event => {
  const results = resultsDiv.innerHTML
  const blob = new Blob([results], {type: 'text/plain'})
  const url = URL.createObjectURL(blob)
  downloadLink.href = url
  downloadLink.download = 'results.txt'
  downloadLink.click()
})