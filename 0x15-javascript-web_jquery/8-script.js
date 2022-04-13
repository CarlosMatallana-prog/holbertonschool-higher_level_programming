const $ = window.$;
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, (data, status) => {
    console.log(data);
    if (status === 'success') {
      for (const film of data.results) {
        $("#list_movies").append(`<li>${film.title}</li>`);
      }
    }
  });
});
