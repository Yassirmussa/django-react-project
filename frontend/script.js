//insert marina
document.getElementById('marinaform').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
  
    var formData = new FormData(this);
  
    fetch('http://localhost:8000/api/v1/marina', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(formData)),
        headers: {
          'Content-Type': 'application/json'
        }
      })
      
    .then(function(response) {
      if (response.ok) {
        console.log('Data added successfully!');
      } else {
        console.error('Error adding data to API');
      }
    })
    .catch(function(error) {
      console.error('Error:', error);
    });
  });
  
//get marina
fetch('http://localhost:8000/api/v1/getmarina')
  .then(response => response.json())
  .then(data => {
    const tableBody = document.getElementById('listtable');

    data.forEach(item => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${item.Mid}</td>
        <td>${item.Mname}</td>
        <td>${item.location}</td>
      `;
      tableBody.appendChild(row);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });
