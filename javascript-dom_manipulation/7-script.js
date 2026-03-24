fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    data.results.forEach(function (movie) {
      const li = document.createElement('li');
      li.textContent = movie.title;
      document.querySelector('#list_movies').appendChild(li);
    });
  });
